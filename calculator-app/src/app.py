from flask import Flask, render_template, request
from calculators.bmi import calculate_bmi
from calculators.dilution import calculate_dilution

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        calculation_type = request.form.get('calculation_type')
        if calculation_type == 'bmi':
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))
            result = calculate_bmi(weight, height)
        elif calculation_type == 'dilution':
            concentration1 = float(request.form.get('concentration1'))
            volume1 = float(request.form.get('volume1'))
            concentration2 = float(request.form.get('concentration2'))
            result = calculate_dilution(concentration1, volume1, concentration2)
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)