from flask import Flask, jsonify, request
import subprocess
import sys
import numpy as np
from flask_cors import CORS
from controllers.superposition_circuit.circuit import setup_circuit, run_cirq
from controllers.quantum_Single_Qubit_Gates.quantam_gates_info import gates_info

app = Flask(__name__)
CORS(
    app, resources={r"/*": {"origins": "http://localhost:3000"}}
)  # to allow NextJs to fetch data


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


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask server is running!"})


# superposition_circuit
@app.route("/setup-circuit", methods=["POST"])
def handle_setup_circuit():
    return setup_circuit()


# superposition_circuit
@app.route("/run-cirq", methods=["POST"])
def handle_run_cirq():
    return run_cirq()


@app.route("/hadamardGate", methods=["GET"])
def hadamard_gate_info():
    gate_info = gates_info["Hadamard Gate"]
    return jsonify({"name": "Hadamard Gate", **gate_info})


@app.route("/xGate", methods=["GET"])
def x_gate_info():
    gate_info = gates_info["X Gate"]
    return jsonify({"name": "X Gate", **gate_info})


@app.route("/pauliYGate", methods=["GET"])
def pauli_y_gate_info():
    gate_info = gates_info["Pauli-Y Gate"]
    return jsonify({"name": "Pauli-Y Gate", **gate_info})


@app.route("/pauliZGate", methods=["GET"])
def pauli_z_gate_info():
    gate_info = gates_info["Pauli-Z Gate"]
    return jsonify({"name": "Pauli-Z Gate", **gate_info})


@app.route("/phaseGate", methods=["GET"])
def phase_gate_info():
    gate_info = gates_info["Phase Gate"]
    return jsonify({"name": "Phase Gate", **gate_info})


@app.route("/tGate", methods=["GET"])
def t_gate_info():
    gate_info = gates_info["T Gate"]
    return jsonify({"name": "T Gate", **gate_info})


if __name__ == "__main__":
    app.run(debug=True)
