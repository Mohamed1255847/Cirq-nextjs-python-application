import cirq

def create_vqe_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(2)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.CX(qubits[0], qubits[1]))
    circuit.append(cirq.measure(*qubits, key='result'))
    return circuit
