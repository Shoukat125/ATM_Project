from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/pin', methods=['GET', 'POST'])
def pin():
    if request.method == 'POST':
        pin = request.form.get('pin')
        if pin == '1255':
            return redirect(url_for('amount'))
        else:
            return render_template('pin.html', error="❌ Invalid PIN! Try again.")
    return render_template('pin.html')

@app.route('/amount', methods=['GET', 'POST'])
def amount():
    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount'))
            balance = 10000
            if balance - amount < 1000:
                return render_template('result.html', message="⚠️ Insufficient Balance! Minimum balance must be 1000.")
            else:
                balance -= amount
                return render_template('result.html', message=f"✅ Withdrawal Successful! Remaining Balance: {balance}")
        except ValueError:
            return render_template('result.html', message="❌ Invalid amount entered.")
    return render_template('amount.html')

@app.route('/result')
def result():
    return render_template('result.html', message="")

if __name__ == '__main__':
    app.run(debug=True)
