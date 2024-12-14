import cirq

circuit_code = """
import cirq
def create_entanglement_swapping_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(4)]
    circuit = cirq.Circuit()

    # Create entanglement: Bell pairs
    circuit.append([cirq.H(qubits[0]), cirq.CX(qubits[0], qubits[1])])
    circuit.append([cirq.H(qubits[2]), cirq.CX(qubits[2], qubits[3])])

    # Bell measurement on qubits 1 and 2
    circuit.append([cirq.CX(qubits[1], qubits[2]), cirq.H(qubits[1])])
    circuit.append([cirq.measure(qubits[1], key='m1'), cirq.measure(qubits[2], key='m2')])

    # Conditional operations based on measurement
    circuit.append([cirq.CNOT(qubits[0], qubits[3]).with_classical_controls('m2')])
    circuit.append([cirq.CZ(qubits[0], qubits[3]).with_classical_controls('m1')])

    return circuit

def run_entanglement_swapping():
    circuit = create_entanglement_swapping_circuit()
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10)
    print(result)
    return {"result": result, "circuit": circuit}
    
    @app.route("/entanglementSwappingCircuit", methods=["GET"])
def entanglement_swapping_circuit():
    data = run_entanglement_swapping()
    result = data["result"]
    circuit = data["circuit"]
    result_dict = result.histogram(key="m1")

    circuit_description =
    This circuit demonstrates entanglement swapping.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    - Conditional gates applied based on measurement outcomes.

    return jsonify(
        {
            "name": "Entanglement Swapping Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
        }
    )
"""


def create_entanglement_swapping_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(4)]
    circuit = cirq.Circuit()

    # Create entanglement: Bell pairs
    circuit.append([cirq.H(qubits[0]), cirq.CX(qubits[0], qubits[1])])
    circuit.append([cirq.H(qubits[2]), cirq.CX(qubits[2], qubits[3])])

    # Bell measurement on qubits 1 and 2
    circuit.append([cirq.CX(qubits[1], qubits[2]), cirq.H(qubits[1])])
    circuit.append(
        [cirq.measure(qubits[1], key="m1"), cirq.measure(qubits[2], key="m2")]
    )

    # Conditional operations based on measurement
    circuit.append([cirq.CNOT(qubits[0], qubits[3]).with_classical_controls("m2")])
    circuit.append([cirq.CZ(qubits[0], qubits[3]).with_classical_controls("m1")])

    return circuit


def run_entanglement_swapping():
    circuit = create_entanglement_swapping_circuit()
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10)
    print(result)
    return {"result": result, "circuit": circuit, "code": circuit_code}
