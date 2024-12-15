import cirq

def create_deutsch_jozsa_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits[:2]))
    circuit.append(cirq.X(qubits[1]),cirq.X(qubits[3]))
    circuit.append(cirq.H(qubits[3]))
    circuit.append(cirq.CNOT(qubits[0], qubits[3]), cirq.CNOT(qubits[1],qubits[3],cirq.CNOT(qubits[2],qubits[3])))
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.X(qubits[1]), cirq.H(qubits[1]))
    circuit.append(cirq.H(qubits[2]))
    circuit.append(cirq.measure(*qubits, key='result'))
    return circuit
