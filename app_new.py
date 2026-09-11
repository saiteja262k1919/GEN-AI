from flask import Flask, request

app = Flask(__name__)

@app.route('/factorial', methods=['GET'])
def factorial():
    num = int(request.args.get('num'))

    fact = 1
    for i in range(1, num + 1):
        fact *= i

    return f"Factorial = {fact}"

if __name__ == "__main__":
    app.run(debug=True)