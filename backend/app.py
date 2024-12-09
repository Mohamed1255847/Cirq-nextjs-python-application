from flask import Flask, jsonify, request
import subprocess
import sys
import numpy as np
from flask_cors import CORS
import cirq
from controllers.superposition_circuit.circuit import setup_circuit, run_cirq
from controllers.quantum_Single_Qubit_Gates.quantam_gates_info import gates_info
from controllers.circuits.circuit_bell_state import create_bell_state_circuit
from controllers.circuits.basic_gates import create_basic_gates_circuit
from controllers.circuits.qft_circuit import create_qft_circuit
from controllers.circuits.teleportation import create_teleportation_circuit
from controllers.circuits.vqe import create_vqe_circuit
from controllers.circuits.phase_estimation import create_phase_estimation_circuit
from controllers.circuits.deutsch_jozsa import create_deutsch_jozsa_circuit
from controllers.circuits.entanglement_swapping import run_entanglement_swapping
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
    return result

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
    
    # Annotated circuit description
    circuit_description = """
    This circuit creates a Bell state, entangling two qubits.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    """

    return jsonify({
        "name": "Bell State Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/basicGatesCircuit", methods=["GET"])
def basic_gates_circuit():
    circuit = create_basic_gates_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    
    # Annotated circuit description
    circuit_description = """
    This circuit demonstrates basic quantum gates.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - X (Pauli-X Gate): Flips the state of a qubit.
    - Z (Pauli-Z Gate): Applies a phase flip.
    """

    return jsonify({
        "name": "Basic Gates Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/qftCircuit", methods=["GET"])
def qft_circuit():
    circuit = create_qft_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    
    # Annotated circuit description
    circuit_description = """
    This circuit performs the Quantum Fourier Transform.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - R (Rotation Gates): Rotations by different angles.
    """

    return jsonify({
        "name": "QFT Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/teleportationCircuit", methods=["GET"])
def teleportation_circuit():
    circuit = create_teleportation_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    
    # Annotated circuit description
    circuit_description = """
    This circuit demonstrates quantum teleportation, transferring a quantum state from one qubit to another.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    """

    return jsonify({
        "name": "Teleportation Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/vqeCircuit", methods=["GET"])
def vqe_circuit():
    circuit = create_vqe_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    
    # Annotated circuit description
    circuit_description = """
    This circuit implements the Variational Quantum Eigensolver.
    Gate Operations:
    - Various parameterized gates applied to prepare and measure a quantum state.
    """

    return jsonify({
        "name": "VQE Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/phaseEstimationCircuit", methods=["GET"])
def phase_estimation_circuit():
    circuit = create_phase_estimation_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    
    # Annotated circuit description
    circuit_description = """
    This circuit performs Quantum Phase Estimation.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - Controlled-U: Control operations based on the unitary to estimate its phase.
    """

    return jsonify({
        "name": "Phase Estimation Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/deutschJozsaCircuit", methods=["GET"])
def deutsch_jozsa_circuit():
    circuit = create_deutsch_jozsa_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    
    # Annotated circuit description
    circuit_description = """
    This circuit implements the Deutsch-Jozsa algorithm to determine if a function is constant or balanced.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - Oracle: Implements the oracle function to be tested.
    """

    return jsonify({
        "name": "Deutsch-Jozsa Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
        "results": result_dict
    })

@app.route("/entanglementSwappingCircuit", methods=["GET"])
def entanglement_swapping_circuit():
    data = run_entanglement_swapping()
    result = data["result"]
    circuit = data["circuit"]
    result_dict = result.histogram(key='m1')  # Ensure the key matches your measurement key

    # Annotated circuit description
    circuit_description = """
    This circuit demonstrates entanglement swapping.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    - Conditional gates applied based on measurement outcomes.
    """

    return jsonify({
        "name": "Entanglement Swapping Circuit",
        "description": circuit_description,
        "circuit": str(circuit),
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