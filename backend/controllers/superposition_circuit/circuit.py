from flask import  jsonify
import cirq



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

    except Exception as e:
        return jsonify({"error": str(e)}), 500

