import cirq


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
    return result
