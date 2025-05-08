from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_clima', methods=['POST'])
def calcular_clima():
    celcius = float(request.form['celcius'])
    resultado = celcius + 273.15
    result = (celcius * 9/5) + 32

    return render_template('index.html', resultado=resultado , result=result)
if __name__ =='__main__':
    app.run(debug=True)