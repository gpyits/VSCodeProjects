from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple in‑memory representation of user balances
user_balances = {
    "user01": 1000,
    "user02": 100
}

@app.route('/transfer', methods=['POST'])
def transfer():
    from_account = "user01"
    amount = int(request.form.get('amount', 0))
    to_account = request.form.get('to_account')

    if user_balances.get(from_account, 0) >= amount:
        user_balances[from_account] -= amount
        user_balances[to_account] = user_balances.get(to_account, 0) + amount
        return jsonify({"status": "success", 
                        "message": f"Transferred {amount} from {from_account} to {to_account}",
                        "balances": user_balances})
    else:
        return jsonify({"status": "failure", "message": "Insufficient funds"}), 400

if __name__ == '__main__':
    app.run(debug=True)
