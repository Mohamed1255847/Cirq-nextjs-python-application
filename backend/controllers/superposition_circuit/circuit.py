from flask import jsonify
import cirq

stored_circuit = None
stored_qubit = None


def ensure_cirq_installed():
    try:
        import cirq
    except ImportError:
        import subprocess
        import sys

        print("installing cirq...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
        print("installed cirq.")


def setup_circuit():
    global stored_circuit, stored_qubit

    try:
        ensure_cirq_installed()
        stored_qubit = cirq.GridQubit(0, 0)
        stored_circuit = cirq.Circuit(
            cirq.X(stored_qubit) ** 0.5, cirq.measure(stored_qubit, key="m")
        )

        return jsonify(
            {"message": "Circuit created successfully", "circuit": str(stored_circuit)}
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def run_cirq():
    global stored_circuit, stored_qubit

    try:
        if not stored_circuit or not stored_qubit:
            return jsonify(
                {"error": "Circuit not set up. Please call /setup-circuit first."}
            ), 400

        simulator = cirq.Simulator()
        result = simulator.run(stored_circuit, repetitions=20)

        result_json = {"measurements": result.measurements["m"].tolist()}
        return jsonify(
            {"message": "Simulation run successfully", "results": result_json}
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
