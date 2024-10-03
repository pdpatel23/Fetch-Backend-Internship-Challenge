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

#return current point balance for each payer
@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(payer_balances), 200

if __name__ == '__main__':
    app.run(port=8000)