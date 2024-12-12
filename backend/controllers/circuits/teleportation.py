import cirq

def create_teleportation_circuit():
    # Create a simple teleportation circuit
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubits[1]))
    circuit.append(cirq.CNOT(qubits[1], qubits[2]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.measure(qubits[0], key='m0'))
    circuit.append(cirq.measure(qubits[1], key='m1'))
    circuit.append(cirq.CNOT(qubits[1], qubits[2]).controlled_by(cirq.MeasurementGate(1, 'm1')))
    circuit.append(cirq.CZ(qubits[0], qubits[2]).controlled_by(cirq.MeasurementGate(1, 'm0')))
    return circuit
