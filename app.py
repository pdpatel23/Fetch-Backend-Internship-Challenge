from flask import Flask

app = Flask(__name__)

#store transactions and balances
transactions = []
balances = {}

#home route to make sure server is running
@app.route('/')
def home():
    return "Hello Fetch API!"

if __name__ == "__main__":
    app.run(port=8000)