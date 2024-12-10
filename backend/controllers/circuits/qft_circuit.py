import cirq

def create_qft_circuit():
    # Create a 3-qubit QFT circuit
    q = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q[2]))
    circuit.append(cirq.CZPowGate(exponent=1/2)(q[1], q[2]))
    circuit.append(cirq.H(q[1]))
    circuit.append(cirq.CZPowGate(exponent=1/4)(q[0], q[2]))
    circuit.append(cirq.CZPowGate(exponent=1/2)(q[0], q[1]))
    circuit.append(cirq.H(q[0]))
    return circuit
