import cirq

def create_bell_state_circuit():
    qubits = [cirq.NamedQubit('q0'), cirq.NamedQubit('q1')]
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  
        cirq.CNOT(qubits[0], qubits[1]),  
        cirq.measure(*qubits, key='result')  
    )
    return circuit


