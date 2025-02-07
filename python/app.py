from flask import Flask, request, jsonify
from sieve import sieve as s
from http import HTTPStatus as http

""" 
Basic API Exposing GET endpoint for nth prime number
Example cURL request: curl "http://127.0.0.1:5000/prime?n=0"
"""

app = Flask(__name__)

@app.route('/prime', methods=['GET'])
def get_nth_prime():
    try:
        sieve = s.Sieve()
        n = int(request.args.get('n'))
        if n < 0:
            return jsonify({"error": "Please provide a positive integer for n"}), http.BAD_REQUEST
        
        prime_number = sieve.nth_prime(n)
        return jsonify({"n": n, "nth_prime": prime_number}), http.OK
    
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide a positive integer."}), http.BAD_REQUEST

if __name__ == '__main__':
    app.run(debug=True)
