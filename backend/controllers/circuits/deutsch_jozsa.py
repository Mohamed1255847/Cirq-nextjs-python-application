import cirq

def create_deutsch_jozsa_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    circuit.append(cirq.CNOT(qubits[0], qubits[2]))
    circuit.append(cirq.H.on_each(*qubits[:2]))
    circuit.append(cirq.measure(*qubits, key='result'))
    return circuit
