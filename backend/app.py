from flask import Flask, jsonify, request
import subprocess
import sys
import numpy as np
from flask_cors import CORS
import cirq
from controllers.superposition_circuit.circuit import setup_circuit, run_cirq
from controllers.quantum_Single_Qubit_Gates.quantam_gates_info import gates_info
from controllers.circuits.circuit_bell_state import create_bell_state_circuit

# from controllers.circuits.grover_circuit import create_grover_circuit
from controllers.circuits.basic_gates import create_basic_gates_circuit
from controllers.circuits.qft_circuit import create_qft_circuit
from controllers.circuits.teleportation import create_teleportation_circuit
from controllers.circuits.vqe import create_vqe_circuit
from controllers.circuits.phase_estimation import create_phase_estimation_circuit
from controllers.circuits.deutsch_jozsa import create_deutsch_jozsa_circuit
from controllers.circuits.entanglement_swapping import (
run_entanglement_swapping
)
from controllers.circuits.circuit_info import get_circuit_info


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


def ensure_cirq_installed():
    try:
        import cirq
    except ImportError:
        print("installing cirq...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
        print("installed cirq.")


def run_circuit(circuit):
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=100)
    return result.histogram(key="result")


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


@app.route("/bellStateCircuit", methods=["GET"])
def bell_state_circuit():
    circuit = create_bell_state_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    return jsonify({"circuit": str(circuit), "results": result_dict})


@app.route("/basicGatesCircuit", methods=["GET"])
def basic_gates_circuit():
    circuit = create_basic_gates_circuit()
    result = run_circuit(circuit)
    return jsonify({"circuit": str(circuit), "results": result})


@app.route("/qftCircuit", methods=["GET"])
def qft_circuit():
    circuit = create_qft_circuit()
    result = run_circuit(circuit)
    return jsonify({"circuit": str(circuit), "results": result})


@app.route("/teleportationCircuit", methods=["GET"])
def teleportation_circuit():
    circuit = create_teleportation_circuit()
    result = run_circuit(circuit)
    return jsonify({"circuit": str(circuit), "results": result})


@app.route("/vqeCircuit", methods=["GET"])
def vqe_circuit():
    circuit = create_vqe_circuit()
    result = run_circuit(circuit)
    return jsonify({"circuit": str(circuit), "results": result})


@app.route("/phaseEstimationCircuit", methods=["GET"])
def phase_estimation_circuit():
    circuit = create_phase_estimation_circuit()
    result = run_circuit(circuit)
    return jsonify({"circuit": str(circuit), "results": result})


@app.route("/deutschJozsaCircuit", methods=["GET"])
def deutsch_jozsa_circuit():
    circuit = create_deutsch_jozsa_circuit()
    result = run_circuit(circuit)
    return jsonify({"circuit": str(circuit), "results": result})


@app.route("/entanglementSwappingCircuit", methods=["GET"])
def entanglement_swapping_circuit():
    data = run_entanglement_swapping()
    result = data["result"]
    circuit = data["circuit"]
    result_dict = result.histogram(key='m1')  # Ensure the key matches your measurement key

    # Annotated circuit description
    circuit_description = """
    Qubit Initialization:
    - Qubits [0, 0]: Starting point for the first qubit.
    - Qubits [1, 0]: Starting point for the second qubit.
    - Qubits [2, 0]: Starting point for the third qubit.
    - Qubits [3, 0]: Starting point for the fourth qubit.

    Gate Operations:
    - H (Hadamard Gate): This gate puts a qubit into a superposition of states.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.

    Circuit Symbol Breakdown:
    - H Gate: Applies a Hadamard operation which puts a qubit into an equal superposition state.
    - @ (CNOT Control) and X (CNOT Target): The CNOT (Controlled-NOT) gate flips the target qubit if the control qubit is in state 1.
    - Bell Measurement: The CNOT followed by a Hadamard gate measures in the Bell basis.
    - Measurement (M): Reads the state of the qubit. The results are stored under the keys m1 and m2.

    Annotated Circuit:
    ───H───@─────────────@────@───
           │             ║    ║
    ───────X───@───H────M╫────╫───
               │        ║║    ║
    ───H───@───X───M────╫╫────╫───
           │       ║    ║║    ║
    ───────X───────╫────╫X────@───
                   ║    ║║    ║
    m1: ═══════════╬════@╬════^═══
                   ║     ║
    m2: ═══════════@═════^════════
    """

    return jsonify({
        "circuit": str(circuit),
        "description": circuit_description,
        "results": result_dict
    })


@app.route("/info/<circuit_name>", methods=["GET"])
def circuit_info(circuit_name):
    info = get_circuit_info(circuit_name)
    if info:
        return jsonify(info)
    else:
        return jsonify({"error": "Circuit not found"}), 404


if __name__ == "__main__":
    ensure_cirq_installed()
    app.run(debug=True)
