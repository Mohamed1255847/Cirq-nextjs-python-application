from flask import Flask, jsonify, request
import subprocess
import sys
import cirq
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) # to allow NextJs to fetch data 

# Global variable to store the circuit (for simplicity)
stored_circuit = None
stored_qubit = None


# Function to ensure Cirq is installed
def ensure_cirq_installed():
    try:
        import cirq  # noqa: F401
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

# Endpoint 1: Set up the circuit
@app.route('/setup-circuit', methods=['POST'])
def setup_circuit():
    global stored_circuit, stored_qubit

    try:
        ensure_cirq_installed()

        # Pick a qubit
        stored_qubit = cirq.GridQubit(0, 0)

        # Create a circuit
        stored_circuit = cirq.Circuit(cirq.X(stored_qubit) ** 0.5, cirq.measure(stored_qubit, key='m'))

        # Return the circuit details
        return jsonify({
            "message": "Circuit created successfully",
            "circuit": str(stored_circuit)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 2: Run the circuit
@app.route('/run-cirq', methods=['POST'])
def run_cirq():
    global stored_circuit, stored_qubit

    try:
        if not stored_circuit or not stored_qubit:
            return jsonify({"error": "Circuit not set up. Please call /setup-circuit first."}), 400

        # Simulate the circuit
        simulator = cirq.Simulator()
        result = simulator.run(stored_circuit, repetitions=20)

        # Return the simulation results
        result_json = {"measurements": result.measurements["m"].tolist()}
        return jsonify({
            "message": "Simulation run successfully",
            "results": result_json
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
