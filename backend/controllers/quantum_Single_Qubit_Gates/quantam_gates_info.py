from controllers.quantum_Single_Qubit_Gates.app import (
    Hadamard_gate,
    Pauli_Y_gate,
    Pauli_Z_gate,
    Phase_gate,
    T_gate,
    X_gate,
)


def serialize_gate(gate):
    return [
        [complex(cell).real if cell.imag == 0 else str(cell) for cell in row]
        for row in gate
    ]


gates_info = {
    "Hadamard Gate": {
        "description": "The Hadamard gate transforms the basis states |0> and |1> into equal superpositions.",
        "usage": "Useful for creating superpositions, used in algorithms like Grover's search.",
        "example": "In a quantum circuit: qc.h(0) # applies Hadamard gate to qubit 0",
        "gate": serialize_gate(Hadamard_gate()),
    },
    "X Gate": {
        "description": "The X gate (also known as NOT gate) flips the state of a qubit.",
        "usage": "Can be used to create bit flips and forms part of various quantum algorithms.",
        "example": "In a quantum circuit: qc.x(0) # applies X gate to qubit 0",
        "gate": serialize_gate(X_gate()),
    },
    "Pauli-Y Gate": {
        "description": "The Pauli-Y gate introduces a complex phase flip.",
        "usage": "Used in complex quantum operations where phase relationships are crucial.",
        "example": "In a quantum circuit: qc.y(0) # applies Pauli-Y gate to qubit 0",
        "gate": serialize_gate(Pauli_Y_gate()),
    },
    "Pauli-Z Gate": {
        "description": "The Pauli-Z gate flips the phase of the qubit.",
        "usage": "Commonly used in phase kickback operations.",
        "example": "In a quantum circuit: qc.z(0) # applies Pauli-Z gate to qubit 0",
        "gate": serialize_gate(Pauli_Z_gate()),
    },
    "Phase Gate": {
        "description": "The Phase gate shifts the phase of the qubit.",
        "usage": "Used in creating certain types of quantum states and in quantum error correction.",
        "example": "In a quantum circuit: qc.p(π/4, 0) # applies Phase gate with π/4 to qubit 0",
        "gate": serialize_gate(Phase_gate()),
    },
    "T Gate": {
        "description": "The T gate introduces a specific phase change.",
        "usage": "Important for creating advanced quantum circuits, especially for universal quantum computing.",
        "example": "In a quantum circuit: qc.t(0) # applies T gate to qubit 0",
        "gate": serialize_gate(T_gate()),
    },
}
