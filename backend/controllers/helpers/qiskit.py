import base64
import io
import cirq
from qiskit import QuantumCircuit
from cirq.ops import XPowGate, YPowGate, ZPowGate, HPowGate, MeasurementGate
from qiskit.visualization import circuit_drawer


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


def cirq_to_qiskit_for_bellState(cirq_circuit: cirq.Circuit) -> QuantumCircuit:
    # Create a Qiskit circuit with the same number of qubits as in the Cirq circuit
    qubit_count = len(cirq_circuit.all_qubits())
    qiskit_circuit = QuantumCircuit(qubit_count, qubit_count)

    # Map Cirq qubits to Qiskit qubits
    qubit_map = {qubit: index for index, qubit in enumerate(cirq_circuit.all_qubits())}

    # Translate Cirq operations to Qiskit
    for moment in cirq_circuit:
        for op in moment.operations:
            qubit_index = qubit_map[op.qubits[0]]

            # Gate translations
            if isinstance(op.gate, cirq.XPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.x(qubit_index) if exponent == 1 else qiskit_circuit.rx(
                    exponent * 180, qubit_index
                )

            elif isinstance(op.gate, cirq.YPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.y(qubit_index) if exponent == 1 else qiskit_circuit.ry(
                    exponent * 180, qubit_index
                )

            elif isinstance(op.gate, cirq.ZPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.z(qubit_index) if exponent == 1 else qiskit_circuit.rz(
                    exponent * 180, qubit_index
                )

            elif isinstance(op.gate, cirq.HPowGate):
                exponent = op.gate.exponent if op.gate.exponent != 1 else 1
                qiskit_circuit.h(qubit_index) if exponent == 1 else qiskit_circuit.u3(
                    180, 0, exponent * 180, qubit_index
                )

            elif isinstance(op.gate, cirq.MeasurementGate):
                qiskit_circuit.measure(qubit_index, qubit_index)

    return qiskit_circuit


def convertCirqCircuitToQiskitForVisualization(circuit):
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
    return img_base64



def convertCirqCircuitToQiskitForVisualizationForBellState(circuit):
    # Convert Cirq circuit to Qiskit for visualization
    qiskit_circuit = cirq_to_qiskit_for_bellState(circuit)
    # Generate image of the circuit
    circuit_image = circuit_drawer(qiskit_circuit, output="mpl")
    # Save the image to a BytesIO object
    img_byte_arr = io.BytesIO()
    circuit_image.savefig(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    # Encode the image in base64 to include it in the JSON response
    img_base64 = base64.b64encode(img_byte_arr.read()).decode("utf-8")
    return img_base64
