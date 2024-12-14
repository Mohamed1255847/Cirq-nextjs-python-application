import base64
import io
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
from qiskit import QuantumCircuit
from cirq.ops import XPowGate, YPowGate, ZPowGate, HPowGate, MeasurementGate
from qiskit.visualization import circuit_drawer

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


def cirq_to_qiskit(cirq_circuit: cirq.Circuit) -> QuantumCircuit:
    # Create a Qiskit circuit with the same number of qubits as in the Cirq circuit
    qubit_count = max(op.qubits[0].row + 1 for op in cirq_circuit.all_operations())
    qiskit_circuit = QuantumCircuit(
        qubit_count, qubit_count
    )  # Add classical bits to the circuit

    # Translate Cirq operations to Qiskit
    for moment in cirq_circuit:
        for op in moment.operations:
            qubit_index = op.qubits[0].row

            # Gate translations
            if isinstance(op.gate, XPowGate):
                # Cirq XPowGate corresponds to Qiskit X gate (notating power)
                exponent = (
                    op.gate.exponent if op.gate.exponent != 1 else 1
                )  # Handle powers
                qiskit_circuit.x(qubit_index) if exponent == 1 else qiskit_circuit.rx(
                    exponent * 180, qubit_index
                )

            elif isinstance(op.gate, YPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.y(qubit_index) if exponent == 1 else qiskit_circuit.ry(
                    exponent * 180, qubit_index
                )

            elif isinstance(op.gate, ZPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.z(qubit_index) if exponent == 1 else qiskit_circuit.rz(
                    exponent * 180, qubit_index
                )

            elif isinstance(op.gate, HPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.h(qubit_index) if exponent == 1 else qiskit_circuit.u3(
                    180, 0, exponent * 180, qubit_index
                )

            elif isinstance(op.gate, MeasurementGate):
                # In Cirq, measurements are handled differently, so we need to handle this explicitly.
                # Qiskit measures a qubit and stores the result in a classical bit.
                qiskit_circuit.measure(
                    qubit_index, qubit_index
                )  # Store the measurement result in a classical bit

    return qiskit_circuit


@app.before_request
def log_request_info():
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.get_data()}")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask server is running!"})


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
    data = create_bell_state_circuit()
    circuit = data["circuit"]
    code = data["code"]
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

    return jsonify(
        {
            "name": "Bell State Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
        }
    )


@app.route("/qftCircuit", methods=["GET"])
def qft_circuit():
    data = create_qft_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = """
    This circuit performs the Quantum Fourier Transform.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - R (Rotation Gates): Rotations by different angles.
    """

    return jsonify(
        {
            "name": "QFT Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
        }
    )


@app.route("/teleportationCircuit", methods=["GET"])
def teleportation_circuit():
    data = create_teleportation_circuit()
    circuit = data["circuit"]
    code = data["code"]
    simulator = cirq.Simulator()
    result = simulator.run(circuit)

    # Get the multi-measurement histogram and convert keys to strings
    raw_result_dict = result.multi_measurement_histogram(keys=["m_qubit0", "m_qubit1"])
    result_dict = {
        " ".join(map(str, key)): value for key, value in raw_result_dict.items()
    }

    circuit_description = """ This circuit demonstrates quantum teleportation, transferring a quantum state from one qubit to another. Gate Operations: - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition. - @ (CNOT Gate Control): Control qubit for the CNOT operation. - X (CNOT Gate Target): Target qubit for the CNOT operation. - M (Measurement): Measures the state of the qubit. """
    return jsonify(
        {
            "name": "Teleportation Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
        }
    )


@app.route("/vqeCircuit", methods=["GET"])
def vqe_circuit():
    data = create_vqe_circuit()
    circuit = data["circuit"]
    code = data["code"]

    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = """
    This circuit implements the Variational Quantum Eigensolver.
    Gate Operations:
    - Various parameterized gates applied to prepare and measure a quantum state.
    """

    return jsonify(
        {
            "name": "VQE Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
        }
    )


@app.route("/phaseEstimationCircuit", methods=["GET"])
def phase_estimation_circuit():
    data = create_phase_estimation_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
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
        }
    )


@app.route("/deutschJozsaCircuit", methods=["GET"])
def deutsch_jozsa_circuit():
    data = create_deutsch_jozsa_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
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
        }
    )


@app.route("/entanglementSwappingCircuit", methods=["GET"])
def entanglement_swapping_circuit():
    data = run_entanglement_swapping()
    result = data["result"]
    circuit = data["circuit"]
    code = data["code"]
    result_dict = result.histogram(key="m1")

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
        }
    )


@app.route("/basicGatesCircuit", methods=["GET"])
def basic_gates_circuit():
    data = create_basic_gates_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")
    # Convert Cirq circuit to Qiskit for visualization
    qiskit_circuit = cirq_to_qiskit(circuit)
    # Generate image of the circuit
    circuit_image = circuit_drawer(qiskit_circuit, output="mpl")
    # Save the image to a BytesIO object
    img_byte_arr = io.BytesIO()
    circuit_image.savefig(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    # Encode the image in base64 to include it in the JSON response
    img_base64 = base64.b64encode(img_byte_arr.read()).decode("utf-8")
    circuit_description = """ This circuit demonstrates basic quantum gates. Gate Operations: - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition. - X (Pauli-X Gate): Flips the state of a qubit. - Z (Pauli-Z Gate): Applies a phase flip. """
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
    return simple_quantum_circuit()


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
