import cirq

def create_entanglement_swapping_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(4)]
    circuit = cirq.Circuit()
    circuit.append([cirq.H(qubits[0]), cirq.H(qubits[1]), cirq.CX(qubits[0], qubits[2]), cirq.CX(qubits[1], qubits[3])])
    return circuit
