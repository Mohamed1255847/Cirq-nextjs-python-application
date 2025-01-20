import numpy as np

def simulate_mo_qfa(input_string):
    """
    Simulate a Measure-Once Quantum Finite Automaton (MO-QFA).
    """
    # Initial state of the automaton: |q0⟩ = [1, 0]
    initial_state = np.array([1, 0], dtype=complex)

    # Transition matrices:
    # transition_0: Hadamard gate (creates superposition)
    transition_0 = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    # transition_1: Pauli-X gate (flips the state)
    transition_1 = np.array([[0, 1], [1, 0]], dtype=complex)

    # Accept state: |q_accept⟩ = [0, 1]
    accept_state = np.array([0, 1], dtype=complex)

    # Start with the initial state
    state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)  # Apply transition_0 for symbol '0'
        elif symbol == '1':
            state = np.dot(transition_1, state)  # Apply transition_1 for symbol '1'
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Calculate the acceptance probability
    acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2

    # Decide to accept or reject based on the probability
    result = "accept" if np.random.rand() < acceptance_probability else "reject"

    # Return the result, acceptance probability, and automaton description
    return {
        "result": result,
        "acceptance_probability": float(acceptance_probability),
        "automata": {
            "states": [
                {"id": "q0", "label": "q0 (Start)", "type": "input"},
                {"id": "q1", "label": "q1 (Accept)", "type": "output"},
            ],
            "transitions": [
                {"id": "e0-1", "source": "q0", "target": "q1", "label": "0, 1"},
            ],
        },
    }


def simulate_mm_qfa(input_string):
    """
    Simulate a Measure-Many Quantum Finite Automaton (MM-QFA).
    """
    # Initial state of the automaton: |q0⟩ = [1, 0, 0]
    initial_state = np.array([1, 0, 0], dtype=complex)

    # Transition matrices:
    # transition_0: Swaps q1 and q2
    transition_0 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    # transition_1: Swaps q0 and q1
    transition_1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

    # Accept state: |q_accept⟩ = [0, 0, 1]
    accept_state = np.array([0, 0, 1], dtype=complex)

    # Start with the initial state
    state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)  # Apply transition_0 for symbol '0'
        elif symbol == '1':
            state = np.dot(transition_1, state)  # Apply transition_1 for symbol '1'
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Calculate the acceptance probability
    acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2

    # Decide to accept or reject based on the probability
    result = "accept" if np.random.rand() < acceptance_probability else "reject"

    # Return the result, acceptance probability, and automaton description
    return {
        "result": result,
        "acceptance_probability": float(acceptance_probability),
        "automata": {
            "states": [
                {"id": "q0", "label": "q0 (Start)", "type": "input"},
                {"id": "q1", "label": "q1", "type": "default"},
                {"id": "q2", "label": "q2 (Accept)", "type": "output"},
            ],
            "transitions": [
                {"id": "e0-1-0", "source": "q0", "target": "q1", "label": "0"},
                {"id": "e0-2-1", "source": "q0", "target": "q2", "label": "1"},
                {"id": "e1-2-0", "source": "q1", "target": "q2", "label": "0"},
                {"id": "e1-0-1", "source": "q1", "target": "q0", "label": "1"},
                {"id": "e2-0-0", "source": "q2", "target": "q0", "label": "0"},
                {"id": "e2-1-1", "source": "q2", "target": "q1", "label": "1"},
            ],
        },
    }


def simulate_one_way_qfa(input_string):
    """
    Simulate a One-Way Quantum Finite Automaton (1QFA).
    """
    # Initial state of the automaton: |q0⟩ = [1, 0, 0]
    initial_state = np.array([1, 0, 0], dtype=complex)

    # Transition matrices:
    # transition_0: Swaps q1 and q2
    transition_0 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    # transition_1: Swaps q0 and q1
    transition_1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

    # Accept state: |q_accept⟩ = [0, 0, 1]
    accept_state = np.array([0, 0, 1], dtype=complex)

    # Start with the initial state
    state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)  # Apply transition_0 for symbol '0'
        elif symbol == '1':
            state = np.dot(transition_1, state)  # Apply transition_1 for symbol '1'
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Calculate the acceptance probability
    acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2

    # Decide to accept or reject based on the probability
    result = "accept" if np.random.rand() < acceptance_probability else "reject"

    # Return the result, acceptance probability, and automaton description
    return {
        "result": result,
        "acceptance_probability": float(acceptance_probability),
        "automata": {
            "states": [
                {"id": "q0", "label": "q0 (Start)", "type": "input"},
                {"id": "q1", "label": "q1", "type": "default"},
                {"id": "q2", "label": "q2 (Accept)", "type": "output"},
            ],
            "transitions": [
                {"id": "e0-1-0", "source": "q0", "target": "q1", "label": "0"},
                {"id": "e0-2-1", "source": "q0", "target": "q2", "label": "1"},
                {"id": "e1-2-0", "source": "q1", "target": "q2", "label": "0"},
                {"id": "e1-0-1", "source": "q1", "target": "q0", "label": "1"},
                {"id": "e2-0-0", "source": "q2", "target": "q0", "label": "0"},
                {"id": "e2-1-1", "source": "q2", "target": "q1", "label": "1"},
            ],
        },
    }


def simulate_two_way_qfa(input_string):
    """
    Simulate a Two-Way Quantum Finite Automaton (2QFA).
    """
    # Initial state of the automaton: |q0⟩ = [1, 0, 0]
    initial_state = np.array([1, 0, 0], dtype=complex)

    # Transition matrices:
    # transition_0: Swaps q1 and q2
    transition_0 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    # transition_1: Swaps q0 and q1
    transition_1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

    # Accept state: |q_accept⟩ = [0, 0, 1]
    accept_state = np.array([0, 0, 1], dtype=complex)

    # Start with the initial state
    state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)  # Apply transition_0 for symbol '0'
        elif symbol == '1':
            state = np.dot(transition_1, state)  # Apply transition_1 for symbol '1'
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Calculate the acceptance probability
    acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2

    # Decide to accept or reject based on the probability
    result = "accept" if np.random.rand() < acceptance_probability else "reject"

    # Return the result, acceptance probability, and automaton description
    return {
        "result": result,
        "acceptance_probability": float(acceptance_probability),
        "automata": {
            "states": [
                {"id": "q0", "label": "q0 (Start)", "type": "input"},
                {"id": "q1", "label": "q1", "type": "default"},
                {"id": "q2", "label": "q2 (Accept)", "type": "output"},
            ],
            "transitions": [
                {"id": "e0-1-0", "source": "q0", "target": "q1", "label": "0"},
                {"id": "e0-2-1", "source": "q0", "target": "q2", "label": "1"},
                {"id": "e1-2-0", "source": "q1", "target": "q2", "label": "0"},
                {"id": "e1-0-1", "source": "q1", "target": "q0", "label": "1"},
                {"id": "e2-0-0", "source": "q2", "target": "q0", "label": "0"},
                {"id": "e2-1-1", "source": "q2", "target": "q1", "label": "1"},
            ],
        },
    }


def simulate_qfa_restart(input_string):
    """
    Simulate a Quantum Finite Automaton with Restart (QFA-R).
    """
    # Initial state of the automaton: |q0⟩ = [1, 0, 0]
    initial_state = np.array([1, 0, 0], dtype=complex)

    # Transition matrices:
    # transition_0: Swaps q1 and q2
    transition_0 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    # transition_1: Swaps q0 and q1
    transition_1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

    # Accept state: |q_accept⟩ = [0, 0, 1]
    accept_state = np.array([0, 0, 1], dtype=complex)

    # Start with the initial state
    state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)  # Apply transition_0 for symbol '0'
        elif symbol == '1':
            state = np.dot(transition_1, state)  # Apply transition_1 for symbol '1'
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Restart condition: If the automaton is in state q1 after processing the input, it restarts.
    if np.argmax(state) == 1:  # If the state is q1
        return {
            "result": "restart",
            "acceptance_probability": 0,
            "automata": {
                "states": [
                    {"id": "q0", "label": "q0 (Start)", "type": "input"},
                    {"id": "q1", "label": "q1", "type": "default"},
                    {"id": "q2", "label": "q2 (Accept)", "type": "output"},
                ],
                "transitions": [
                    {"id": "e0-1-0", "source": "q0", "target": "q1", "label": "0"},
                    {"id": "e0-2-1", "source": "q0", "target": "q2", "label": "1"},
                    {"id": "e1-2-0", "source": "q1", "target": "q2", "label": "0"},
                    {"id": "e1-0-1", "source": "q1", "target": "q0", "label": "1 (Restart)"},
                    {"id": "e2-0-0", "source": "q2", "target": "q0", "label": "0"},
                    {"id": "e2-1-1", "source": "q2", "target": "q1", "label": "1"},
                ],
            },
        }

    # Calculate the acceptance probability
    acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2

    # Decide to accept or reject based on the probability
    result = "accept" if np.random.rand() < acceptance_probability else "reject"

    # Return the result, acceptance probability, and automaton description
    return {
        "result": result,
        "acceptance_probability": float(acceptance_probability),
        "automata": {
            "states": [
                {"id": "q0", "label": "q0 (Start)", "type": "input"},
                {"id": "q1", "label": "q1", "type": "default"},
                {"id": "q2", "label": "q2 (Accept)", "type": "output"},
            ],
            "transitions": [
                {"id": "e0-1-0", "source": "q0", "target": "q1", "label": "0"},
                {"id": "e0-2-1", "source": "q0", "target": "q2", "label": "1"},
                {"id": "e1-2-0", "source": "q1", "target": "q2", "label": "0"},
                {"id": "e1-0-1", "source": "q1", "target": "q0", "label": "1 (Restart)"},
                {"id": "e2-0-0", "source": "q2", "target": "q0", "label": "0"},
                {"id": "e2-1-1", "source": "q2", "target": "q1", "label": "1"},
            ],
        },
    }


def simulate_qfa_control_language(input_string):
    """
    Simulate a Quantum Finite Automaton with Control Language (QFA-CL).
    """
    # Initial state of the automaton: |q0⟩ = [1, 0, 0]
    initial_state = np.array([1, 0, 0], dtype=complex)

    # Transition matrices:
    # transition_0: Swaps q1 and q2
    transition_0 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    # transition_1: Swaps q0 and q1
    transition_1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

    # Accept state: |q_accept⟩ = [0, 0, 1]
    accept_state = np.array([0, 0, 1], dtype=complex)

    # Start with the initial state
    state = initial_state

    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            state = np.dot(transition_0, state)  # Apply transition_0 for symbol '0'
        elif symbol == '1':
            state = np.dot(transition_1, state)  # Apply transition_1 for symbol '1'
        else:
            return {"error": "Invalid input symbol. Only '0' and '1' are allowed."}

    # Control language condition: Accept if the input string is of the form 0^n 1^n
    if input_string.count('0') == input_string.count('1'):
        acceptance_probability = np.abs(np.dot(accept_state.conj().T, state)) ** 2
        result = "accept" if np.random.rand() < acceptance_probability else "reject"
    else:
        result = "reject"
        acceptance_probability = 0

    # Return the result, acceptance probability, and automaton description
    return {
        "result": result,
        "acceptance_probability": float(acceptance_probability),
        "automata": {
            "states": [
                {"id": "q0", "label": "q0 (Start)", "type": "input"},
                {"id": "q1", "label": "q1", "type": "default"},
                {"id": "q2", "label": "q2 (Accept)", "type": "output"},
            ],
            "transitions": [
                {"id": "e0-1-0", "source": "q0", "target": "q1", "label": "0"},
                {"id": "e0-2-1", "source": "q0", "target": "q2", "label": "1"},
                {"id": "e1-2-0", "source": "q1", "target": "q2", "label": "0"},
                {"id": "e1-0-1", "source": "q1", "target": "q0", "label": "1"},
                {"id": "e2-0-0", "source": "q2", "target": "q0", "label": "0"},
                {"id": "e2-1-1", "source": "q2", "target": "q1", "label": "1"},
            ],
        },
    }