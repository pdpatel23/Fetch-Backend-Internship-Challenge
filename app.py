from flask import Flask, request, jsonify

app = Flask(__name__)


#home route to make sure server is running
@app.route('/')
def home():
    return "Points API!"

#stores all transactions (payer, points, timestamp)
transactions = [] 

#stores total points of balance for each payer
payer_balances = {} 


#adds points for a specific payer and logs tranaction with timestamp
@app.route('/add', methods=['POST'])
def add_points():

    #extracts payer, points, and timestamp from request
    data = request.get_json()
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']
   
    #update transaction list
    transactions.append({'payer': payer, 'points': points, 'timestamp': timestamp})
    
    #update payer_balances, either add balance or add to the exisiting payer's balance
    if payer in payer_balances:
        payer_balances[payer] += points
    else:
        payer_balances[payer] = points
   
    return "", 200

#spends points starting form oldest transaction without having payer's balance go negative
@app.route('/spend', methods=['POST'])
def spend_points():

    #extract points
    data = request.get_json()
    points_to_spend = data['points']

    #Check if there are enough points
    total_points = sum(payer_balances.values())
    if points_to_spend > total_points:
        return "The user doesn't have enough points", 400

    #sort transactions by time
    spent_points = []
    sorted_transactions = sorted(transactions, key=lambda x: x['timestamp'])
 
    #deduct points from payer starting with oldest transaction
    for transaction in sorted_transactions:
        if points_to_spend <= 0:
            break

        payer = transaction['payer']
        points = transaction['points']

        points_deducted = min(points, points_to_spend)
        transaction['points'] -= points_deducted
        payer_balances[payer] -= points_deducted


        spent_points.append({'payer': payer, 'points': -points_deducted})

        points_to_spend -= points_deducted
        
    output_list = {}

    #add all spent points for each payer
    for transaction in spent_points:
        payer = transaction['payer']
        points = transaction['points']

        if payer in output_list:
            output_list[payer] += points
        else:
            output_list[payer] = points
   
    output_list = [{'payer': payer, 'points': points} for payer, points in output_list.items()]


    return jsonify(output_list), 200


#return current point balance for each payer
@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(payer_balances), 200

if __name__ == '__main__':
    app.run(port=8000)