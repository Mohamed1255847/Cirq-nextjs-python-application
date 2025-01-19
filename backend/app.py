from flask import Flask, jsonify, request
import subprocess
import sys
import numpy as np
from flask_cors import CORS
import cirq
from controllers.superposition_circuit.circuit import simple_quantum_circuit
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
from controllers.helpers.qiskit import (
    convertCirqCircuitToQiskitForVisualization,
    convertCirqCircuitToQiskitForVisualizationForBellState,
)
from controllers.qfm.app import (
    simulate_mm_qfa,
    simulate_mo_qfa,
    simulate_one_way_qfa,
    simulate_qfa_control_language,
    simulate_qfa_restart,
    simulate_two_way_qfa,
)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


def ensure_cirq_installed():
    """Ensure Cirq is installed. If not, install it."""
    try:
        import cirq
    except ImportError:
        print("Installing Cirq...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
        print("Cirq installed.")


def run_circuit(circuit):
    """Run a Cirq circuit and return the results."""
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=100)
    return result


@app.before_request
def log_request_info():
    """Log incoming requests for debugging."""
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.get_data()}")


@app.route("/", methods=["GET"])
def home():
    """Home endpoint to check if the server is running."""
    return jsonify({"message": "Flask server is running!"})


@app.route("/hadamardGate", methods=["GET"])
def hadamard_gate_info():
    """Endpoint to get information about the Hadamard gate."""
    gate_info = gates_info["Hadamard Gate"]
    return jsonify({"name": "Hadamard Gate", **gate_info})


@app.route("/xGate", methods=["GET"])
def x_gate_info():
    """Endpoint to get information about the Pauli-X gate."""
    gate_info = gates_info["X Gate"]
    return jsonify({"name": "X Gate", **gate_info})


@app.route("/pauliYGate", methods=["GET"])
def pauli_y_gate_info():
    """Endpoint to get information about the Pauli-Y gate."""
    gate_info = gates_info["Pauli-Y Gate"]
    return jsonify({"name": "Pauli-Y Gate", **gate_info})


@app.route("/pauliZGate", methods=["GET"])
def pauli_z_gate_info():
    """Endpoint to get information about the Pauli-Z gate."""
    gate_info = gates_info["Pauli-Z Gate"]
    return jsonify({"name": "Pauli-Z Gate", **gate_info})


@app.route("/phaseGate", methods=["GET"])
def phase_gate_info():
    """Endpoint to get information about the Phase gate."""
    gate_info = gates_info["Phase Gate"]
    return jsonify({"name": "Phase Gate", **gate_info})


@app.route("/tGate", methods=["GET"])
def t_gate_info():
    """Endpoint to get information about the T gate."""
    gate_info = gates_info["T Gate"]
    return jsonify({"name": "T Gate", **gate_info})


@app.route("/bellStateCircuit", methods=["GET"])
def bell_state_circuit():
    """Endpoint to simulate a Bell State circuit."""
    data = create_bell_state_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    img_base64 = convertCirqCircuitToQiskitForVisualizationForBellState(circuit)

    circuit_description = """
    This circuit creates a Bell state, entangling two qubits.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    """

    return jsonify(
        {
            "name": "Bell State Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/qftCircuit", methods=["GET"])
def qft_circuit():
    """Endpoint to simulate a Quantum Fourier Transform circuit."""
    data = create_qft_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    circuit_description = """
    This circuit performs the Quantum Fourier Transform.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - R (Rotation Gates): Rotations by different angles.
    """

    return jsonify(
        {
            "name": "Quantum Fourier Transform",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/teleportationCircuit", methods=["GET"])
def teleportation_circuit():
    """Endpoint to simulate a Quantum Teleportation circuit."""
    data = create_teleportation_circuit()
    circuit = data["circuit"]
    code = data["code"]
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    # Get the multi-measurement histogram and convert keys to strings
    raw_result_dict = result.multi_measurement_histogram(keys=["m_qubit0", "m_qubit1"])
    result_dict = {
        " ".join(map(str, key)): value for key, value in raw_result_dict.items()
    }

    circuit_description = """
    This circuit demonstrates quantum teleportation, transferring a quantum state from one qubit to another.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    """

    return jsonify(
        {
            "name": "Teleportation Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/vqeCircuit", methods=["GET"])
def vqe_circuit():
    """Endpoint to simulate a Variational Quantum Eigensolver circuit."""
    data = create_vqe_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    circuit_description = """
    This circuit implements the Variational Quantum Eigensolver.
    Gate Operations:
    - Various parameterized gates applied to prepare and measure a quantum state.
    """

    return jsonify(
        {
            "name": "Variational Quantum Eigensolver",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/phaseEstimationCircuit", methods=["GET"])
def phase_estimation_circuit():
    """Endpoint to simulate a Quantum Phase Estimation circuit."""
    data = create_phase_estimation_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    circuit_description = """
    This circuit performs Quantum Phase Estimation.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - Controlled-U: Control operations based on the unitary to estimate its phase.
    """

    return jsonify(
        {
            "name": "Phase Estimation Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/deutschJozsaCircuit", methods=["GET"])
def deutsch_jozsa_circuit():
    """Endpoint to simulate a Deutsch-Jozsa circuit."""
    data = create_deutsch_jozsa_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    circuit_description = """
    This circuit implements the Deutsch-Jozsa algorithm to determine if a function is constant or balanced.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - Oracle: Implements the oracle function to be tested.
    """

    return jsonify(
        {
            "name": "Deutsch-Jozsa Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/entanglementSwappingCircuit", methods=["GET"])
def entanglement_swapping_circuit():
    """Endpoint to simulate an Entanglement Swapping circuit."""
    data = run_entanglement_swapping()
    result = data["result"]
    circuit = data["circuit"]
    code = data["code"]
    result_dict = result.histogram(key="m1")
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    circuit_description = """
    This circuit demonstrates entanglement swapping.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    - Conditional gates applied based on measurement outcomes.
    """

    return jsonify(
        {
            "name": "Entanglement Swapping Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/basicGatesCircuit", methods=["GET"])
def basic_gates_circuit():
    """Endpoint to simulate a basic gates circuit."""
    data = create_basic_gates_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)

    circuit_description = """
    This circuit demonstrates basic quantum gates.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - X (Pauli-X Gate): Flips the state of a qubit.
    - Z (Pauli-Z Gate): Applies a phase flip.
    """

    return jsonify(
        {
            "name": "Basic Gates Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
            "image": img_base64,
        }
    )


@app.route("/simplequantumcircuit", methods=["GET"])
def handle_simple_quantum_circuit():
    """Endpoint to simulate a simple quantum circuit."""
    return simple_quantum_circuit()


@app.route("/info/<circuit_name>", methods=["GET"])
def circuit_info(circuit_name):
    """Endpoint to get information about a specific circuit."""
    info = get_circuit_info(circuit_name)
    if info:
        return jsonify(info)
    else:
        return jsonify({"error": "Circuit not found"}), 404


@app.route("/mo-qfa", methods=["POST"])
def mo_qfa():
    data = request.json
    input_string = data.get("input_string", "")
    return jsonify(simulate_mo_qfa(input_string))


@app.route("/mm-qfa", methods=["POST"])
def mm_qfa():
    data = request.json
    input_string = data.get("input_string", "")
    return jsonify(simulate_mm_qfa(input_string))


@app.route("/one-way-qfa", methods=["POST"])
def one_way_qfa():
    data = request.json
    input_string = data.get("input_string", "")
    return jsonify(simulate_one_way_qfa(input_string))


@app.route("/two-way-qfa", methods=["POST"])
def two_way_qfa():
    data = request.json
    input_string = data.get("input_string", "")
    return jsonify(simulate_two_way_qfa(input_string))


@app.route("/qfa-restart", methods=["POST"])
def qfa_restart():
    data = request.json
    input_string = data.get("input_string", "")
    return jsonify(simulate_qfa_restart(input_string))


@app.route("/qfa-control-language", methods=["POST"])
def qfa_control_language():
    data = request.json
    input_string = data.get("input_string", "")
    return jsonify(simulate_qfa_control_language(input_string))


if __name__ == "__main__":
    ensure_cirq_installed()
    app.run(debug=True)
