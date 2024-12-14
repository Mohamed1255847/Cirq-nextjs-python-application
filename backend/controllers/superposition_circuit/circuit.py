from flask import jsonify
import cirq
from controllers.helpers.qiskit import convertCirqCircuitToQiskitForVisualization

code = """


def ensure_cirq_installed():
    try:
        import cirq
    except ImportError:
        import subprocess
        import sys
        print("installing cirq...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
        print("installed cirq.")

def simple_quantum_circuit():
    try:
        ensure_cirq_installed()
        qubit = cirq.GridQubit(0, 0)
        circuit = cirq.Circuit(
            cirq.X(qubit) ** 0.5, 
            cirq.measure(qubit, key="m")
        )
        circuit_description = "A simple quantum circuit"
        
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=20)
        result_json = {"measurements": result.measurements["m"].tolist()}
        
        return jsonify({
            "name": "Simple Quantum Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_json
        })


"""


def ensure_cirq_installed():
    try:
        import cirq
    except ImportError:
        import subprocess
        import sys

        print("installing cirq...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
        print("installed cirq.")


def simple_quantum_circuit():
    try:
        ensure_cirq_installed()
        qubit = cirq.GridQubit(0, 0)
        circuit = cirq.Circuit(cirq.X(qubit) ** 0.5, cirq.measure(qubit, key="m"))
        circuit_description = """

**Circuit: (0, 0): ───X^0.5───M('m')───**

1. **Qubit (0, 0)**: The operation is applied to the qubit labeled as `(0, 0)`.

2. **X^0.5 Gate**: This represents a gate that applies a rotation around the X-axis of the Bloch sphere. The notation `X^0.5` means it applies the square root of the X gate, or equivalently, a 90-degree rotation around the X-axis. This puts the qubit into a superposition state.

3. **M('m') Gate**: This is a measurement operation labeled `'m'`. After the application of the X^0.5 gate, the qubit is measured. The result of the measurement is stored in the classical bit `'m'`.

So, in summary, this circuit first puts the qubit `(0, 0)` into a superposition state with the X^0.5 gate, and then measures the qubit, storing the result in the classical bit `'m'`. 

If you need more details or have another question, feel free to ask!"""

        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=20)
        result_json = {"measurements": result.measurements["m"].tolist()}
        img_base64 = convertCirqCircuitToQiskitForVisualization(circuit)
        return jsonify(
            {
                "name": "Simple Quantum Circuit",
                "description": circuit_description,
                "circuit": str(circuit),
                "results": result_json,
                "code": code,
                "image": img_base64,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
