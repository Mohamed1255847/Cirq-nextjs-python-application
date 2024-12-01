import numpy as np


def X_gate(): return np.array([[0, 1], [1, 0]])

def Pauli_Y_gate():
    return np.array([[0, -1j], [1j, 0]])

def Pauli_Z_gate(): 
    return np.array([[1, 0], [0, -1]])

def Hadamard_gate(): 
    return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def Phase_gate():
    return np.array([[1, 0], [0, 1j]])

def T_gate():  # T (π/4 Phase gate)
    return np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])

