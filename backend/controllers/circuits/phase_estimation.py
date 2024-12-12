import cirq

def create_phase_estimation_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(4)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    for k, q in enumerate(qubits):
        circuit.append(cirq.X(q) ** (2 ** k))
    return circuit
