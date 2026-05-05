from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_tab="hcf")

@app.route('/hcf_lcm', methods=['POST'])
def hcf_lcm():
    a = int(request.form['num1'])
    b = int(request.form['num2'])

    def hcf(x, y):
        while y:
            x, y = y, x % y
        return x

    h = hcf(a, b)
    l = (a * b) // h

    return render_template('index.html', hcf=h, lcm=l, active_tab="hcf")

@app.route('/reverse', methods=['POST'])
def reverse():
    text = request.form['text']
    reversed_text = text[::-1]

    return render_template('index.html', reversed=reversed_text, active_tab="reverse")

@app.route('/factorial', methods=['POST'])
def factorial():
    n = int(request.form['num'])

    f = 1
    for i in range(1, n + 1):
        f *= i

    return render_template('index.html', factorial=f, active_tab="factorial")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
