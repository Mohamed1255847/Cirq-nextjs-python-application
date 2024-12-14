import cirq


code = """

def create_basic_gates_circuit():
    # Create a simple circuit with basic quantum gates
    qubit = cirq.GridQubit(0, 0)
    circuit = cirq.Circuit()
    circuit.append([
        cirq.X(qubit),  # Pauli-X Gate
        cirq.Y(qubit),  # Pauli-Y Gate
        cirq.Z(qubit),  # Pauli-Z Gate
        cirq.H(qubit),  # Hadamard Gate
        cirq.measure(qubit, key="result")  # Add measurement
    ])
    return circuit

def run_circuit(circuit):
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=100)
    return {"result":result , "code": code }
    
    
@app.route("/basicGatesCircuit", methods=["GET"])
def basic_gates_circuit():
    circuit = create_basic_gates_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = 
    This circuit demonstrates basic quantum gates.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - X (Pauli-X Gate): Flips the state of a qubit.
    - Z (Pauli-Z Gate): Applies a phase flip.

    return jsonify(
        {
            "name": "Basic Gates Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
        }
    )

"""


def create_basic_gates_circuit():
    # Create a simple circuit with basic quantum gates
    qubit = cirq.GridQubit(0, 0)
    circuit = cirq.Circuit()
    circuit.append(
        [
            cirq.X(qubit),  # Pauli-X Gate
            cirq.Y(qubit),  # Pauli-Y Gate
            cirq.Z(qubit),  # Pauli-Z Gate
            cirq.H(qubit),  # Hadamard Gate
            cirq.measure(qubit, key="result"),  # Add measurement
        ]
    )
    return {"circuit": circuit, "code": code}