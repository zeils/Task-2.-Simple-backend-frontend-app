from flask import Flask, request, jsonify
import os

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'GET':
        try:
            num1 = request.args.get('num1')
            num2 = request.args.get('num2')

            if num1 is None or num2 is None:
                return jsonify({'error': 'Both numbers are required'}), 400

            num1 = float(num1)
            num2 = float(num2)

            result = num1 + num2

            response = {
                'result': result
            }

            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()

            num1 = data.get('num1')
            num2 = data.get('num2')


            if num1 is None or num2 is None:
                return jsonify({'error': 'Both numbers are required'}), 400

 
            num1 = float(num1)
            num2 = float(num2)


            result = num1 + num2

      
            response = {
                'result': result
            }

            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)