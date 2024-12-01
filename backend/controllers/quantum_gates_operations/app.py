import numpy as np
import random
from controllers.quantum_Single_Qubit_Gates.app import Hadamard_gate


def compute_determinant(gate):
    gateToArrayNp = np.array(gate)
    return np.linalg.det(gateToArrayNp)

def compute_transpose(matrix):
    matrixToArrayNp = np.array(matrix)
    return np.transpose(matrixToArrayNp)

def is_quantum_valid_state(state):
    stateToArrayNp = np.array(state)
    return np.isclose(np.sum(np.abs(stateToArrayNp)**2), 1)


def compute_adjoint(matrix):
    matrixToArrayNp = np.array(matrix)
    return np.conjugate(matrixToArrayNp).T

def add_gates(gate_list): # compute the sum of a list of quantum gates
    gate_list = [np.array(gate) for gate in gate_list]
    return sum(gate_list)

def multiply_gates(gates):
    gates = [np.array(gate) for gate in gates] 
    result = gates[0]
    for gate in gates[1:]:
        result = np.dot(result, gate)
    return result

def multiply_constant(matrix, constant): # Multiply a Matrix by a Constant  
    matrix = np.array(matrix)  
    return constant * matrix

def compute_rank(matrix):  # Compute Rank of a Matrix
    matrix = np.array(matrix)  
    return np.linalg.matrix_rank(matrix)
# Check Quantum Gate Validity A valid quantum gate is typically a unitary matrix, meaning that its conjugate transpose is also its inverse.

def is_valid_gate(gate):
    gate = np.array(gate) 
    return np.allclose(np.dot(gate, gate.conj().T), np.eye(gate.shape[0]))

def get_Eigenvalues_and_Eigenvectors(gate): 
    gate = np.array(gate) 
    eigenvalues, eigenvectors = np.linalg.eig(gate)
    return eigenvalues, eigenvectors

# Convert from Computational to +/- Basis
def computational_to_plus_minus(state):
    return np.dot(Hadamard_gate, state)

# Convert from +/- to Computational Basis

def plus_minus_to_computational(state):
    return np.dot(Hadamard_gate, state)

# Apply Single Qubit Gate to State
def apply_gate(state, gate):
    state = np.array(state) 
    gate = np.array(gate)  
    return np.dot(gate, state)

# Measure in Computational Basis
def measure_computational(state):
    probabilities = np.abs(state) ** 2
    return np.random.choice([0, 1], p=probabilities)