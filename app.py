from flask import Flask, request

app = Flask(__name__)

# Home Endpoint
@app.route('/')
def home():
    return "Welcome to Flask Application"


# Endpoint 1: Factorial
@app.route('/factorial', methods=['POST'])
def factorial():
    num = int(request.form['num'])

    fact = 1
    for i in range(1, num + 1):
        fact *= i

    return f"Factorial = {fact}"


# Endpoint 2: Sum of Two Numbers
@app.route('/sum', methods=['POST'])
def add():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    result = num1 + num2

    return f"Sum = {result}"


# Endpoint 3: Largest Number
@app.route('/largest', methods=['POST'])
def largest():

    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    if num1 > num2:
        return f"Largest Number = {num1}"
    elif num2 > num1:
        return f"Largest Number = {num2}"
    else:
        return "Both numbers are equal"


if __name__ == "__main__":
    app.run(debug=True)