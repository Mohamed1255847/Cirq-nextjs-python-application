from flask import Flask, jsonify, request
import subprocess
import sys
import numpy as np
from flask_cors import CORS
from controllers.superposition_circuit.circuit import setup_circuit, run_cirq
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) # to allow NextJs to fetch data 


def ensure_cirq_installed(): 
    try:
        import cirq  
    except ImportError:
        print("installing cirq...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
        print("installed cirq.")

@app.before_request
def log_request_info():
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.get_data()}")


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask server is running!"})

# superposition_circuit 
@app.route('/setup-circuit', methods=['POST'])
def handle_setup_circuit():
    return setup_circuit()

# superposition_circuit 
@app.route('/run-cirq', methods=['POST'])
def handle_run_cirq(): 
    return run_cirq()



if __name__ == '__main__':
    app.run(debug=True)
