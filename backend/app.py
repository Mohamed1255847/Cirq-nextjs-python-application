from flask import Flask, jsonify, request
import subprocess
import sys
import numpy as np
from flask_cors import CORS
from controllers.superposition_circuit.circuit import setup_circuit, run_cirq
from controllers.quantum_Single_Qubit_Gates.app import Hadamard_gate,Pauli_Y_gate,Pauli_Z_gate,Phase_gate,T_gate,X_gate

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

@app.route('/hadamardGate', methods=['GET']) 
def hadamard_gate_info(): 
    return {
            "message": "Gate created successfully",
            "gate": Hadamard_gate().tolist() 
        }
@app.route('/xGate', methods=['GET']) 
def x_gate_info(): 
    return jsonify(X_gate().tolist()) 
@app.route('/pauliYGate', methods=['GET']) 
def pauli_y_gate_info(): 
    return jsonify(Pauli_Y_gate().tolist()) 
@app.route('/pauliZGate', methods=['GET']) 
def pauli_z_gate_info(): 
    return jsonify(Pauli_Z_gate().tolist()) 
@app.route('/phaseGate', methods=['GET']) 
def phase_gate_info(): 
    return jsonify(Phase_gate().tolist())
@app.route('/tGate', methods=['GET'])
def t_gate_info(): 
    return jsonify(T_gate().tolist()) 

if __name__ == '__main__':
    app.run(debug=True)
