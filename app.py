from flask import Flask, render_template, request
import finance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/future_value', methods=['GET', 'POST'])
def future_value():
    result = None
    if request.method == 'POST':
        principal = float(request.form.get('principal', 0))
        rate = float(request.form.get('rate', 0))
        periods = int(request.form.get('periods', 0))
        result = finance.future_value(principal, rate, periods)
    return render_template('future_value.html', result=result)

@app.route('/present_value', methods=['GET', 'POST'])
def present_value():
    result = None
    if request.method == 'POST':
        future_val = float(request.form.get('future_val', 0))
        rate = float(request.form.get('rate', 0))
        periods = int(request.form.get('periods', 0))
        result = finance.present_value(future_val, rate, periods)
    return render_template('present_value.html', result=result)

@app.route('/compound_interest', methods=['GET', 'POST'])
def compound_interest():
    result = None
    if request.method == 'POST':
        principal = float(request.form.get('principal', 0))
        rate = float(request.form.get('rate', 0))
        compounding = int(request.form.get('compounding', 1))
        periods = int(request.form.get('periods', 0))
        result = finance.compound_interest(principal, rate, compounding, periods)
    return render_template('compound_interest.html', result=result)

@app.route('/simple_interest', methods=['GET', 'POST'])
def simple_interest():
    result = None
    if request.method == 'POST':
        principal = float(request.form.get('principal', 0))
        rate = float(request.form.get('rate', 0))
        time = float(request.form.get('time', 0))
        result = finance.simple_interest(principal, rate, time)
    return render_template('simple_interest.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
