def get_circuit_info(name):
    circuits_info = {
        "basicGates": {
            "name": "Basic Quantum Gate",
            "description": "Includes fundamental gates like Pauli-X, Pauli-Y, Pauli-Z, and Hadamard (H) gate. These are the basic building blocks for quantum circuits.",
            "example": "Pauli-X (NOT), Pauli-Y, Pauli-Z, Hadamard (H) gates"
        },
        "qft": {
            "name": "Quantum Fourier Transform (QFT)",
            "description": "A key algorithm used in quantum computing, the quantum analogue of the discrete Fourier transform.",
            "example": "Used in Shor's algorithm for factoring integers."
        },
        "teleportation": {
            "name": "Quantum Teleportation",
            "description": "Protocol to transfer quantum information from one location to another without moving the physical qubit.",
            "example": "Entangling two particles and teleporting state information."
        },
        "vqe": {
            "name": "Variational Quantum Eigensolver (VQE)",
            "description": "A hybrid quantum-classical algorithm to find the ground state of a system. Used in quantum chemistry and material science.",
            "example": "Finding the ground state energy of a molecule."
        },
        "phaseEstimation": {
            "name": "Phase Estimation",
            "description": "A fundamental algorithm for quantum computing, used in various other algorithms.",
            "example": "Estimating eigenvalues of unitary operators."
        },
        "deutschJozsa": {
            "name": "Deutsch-Josza Algorithm",
            "description": "An algorithm demonstrating the advantage of quantum computation, solving specific problems exponentially faster than classical algorithms.",
            "example": "Determining if a function is constant or balanced."
        },
        "entanglementSwapping": {
            "name": "Entanglement Swapping",
            "description": "A process that allows two particles to become entangled even if they never interact directly.",
            "example": "Crucial for quantum networks and long-distance quantum communication."
        }
    }
    
    return circuits_info.get(name, {})
