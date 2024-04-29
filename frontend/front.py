from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)


port = int(os.environ.get('PORT', 8000))


backend_url = 'http://backend:5000/add'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_numbers():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        params = {'num1': num1, 'num2': num2}
        response = requests.post(backend_url, json=params)
        result = response.json()['result']

        return render_template('result.html', result=result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)