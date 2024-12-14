import cirq

code = """
import cirq



def create_teleportation_circuit():
    # Create a simple teleportation circuit
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubits[1]))
    circuit.append(cirq.CNOT(qubits[1], qubits[2]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.measure(qubits[0], key="m_qubit0"))
    circuit.append(cirq.measure(qubits[1], key="m_qubit1"))

    # Apply conditional operations based on measurement results
    circuit.append(cirq.X(qubits[2]).controlled_by(qubits[1]))
    circuit.append(cirq.Z(qubits[2]).controlled_by(qubits[0]))

    return {"circuit":circuit , "code":code}
    
    


@app.route("/teleportationCircuit", methods=["GET"])
def teleportation_circuit():
    circuit = create_teleportation_circuit()
    simulator = cirq.Simulator()
    result = simulator.run(circuit)

    # Get the multi-measurement histogram and convert keys to strings
    raw_result_dict = result.multi_measurement_histogram(keys=["m_qubit0", "m_qubit1"])
    result_dict = {
        " ".join(map(str, key)): value for key, value in raw_result_dict.items()
    }

    circuit_description =  This circuit demonstrates quantum teleportation, transferring a quantum state from one qubit to another. Gate Operations: - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition. - @ (CNOT Gate Control): Control qubit for the CNOT operation. - X (CNOT Gate Target): Target qubit for the CNOT operation. - M (Measurement): Measures the state of the qubit.
    return jsonify(
        {
            "name": "Teleportation Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
        }
    )

"""


def create_teleportation_circuit():
    # Create a simple teleportation circuit
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubits[1]))
    circuit.append(cirq.CNOT(qubits[1], qubits[2]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.measure(qubits[0], key="m_qubit0"))
    circuit.append(cirq.measure(qubits[1], key="m_qubit1"))

    # Apply conditional operations based on measurement results
    circuit.append(cirq.X(qubits[2]).controlled_by(qubits[1]))
    circuit.append(cirq.Z(qubits[2]).controlled_by(qubits[0]))

    return {"circuit": circuit, "code": code}
