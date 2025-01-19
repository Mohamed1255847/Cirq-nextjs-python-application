import numpy as np

def simulate_qfa(input_string):
    """
    Simulate a Quantum Finite Automaton (QFA).
    Args:
        input_string (str): Input string (e.g., '0101').
    Returns:
        dict: Result of the simulation (accept/reject).
    """
    # Define the initial state |q0⟩
    initial_state = np.array([1, 0], dtype=complex)  # |q0⟩ = [1, 0]

    # Define transition matrices for input symbols '0' and '1'
    # Example: Hadamard gate for '0', Pauli-X gate for '1'
    transition_0 = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)  # Hadamard
    transition_1 = np.array([[0, 1], [1, 0]], dtype=complex)  # Pauli-X

    # Process each symbol in the input string
    state = initial_state
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)
        elif symbol == '1':
            state = np.dot(transition_1, state)
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Define the accepting state |q_accept⟩ = [0, 1]
    accept_state = np.array([0, 1], dtype=complex)

    # Compute the probability of acceptance
    acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2

    # Simulate acceptance/rejection based on the probability
    result = "accept" if np.random.rand() < acceptance_probability else "reject"
    return {"result": result, "acceptance_probability": float(acceptance_probability)}