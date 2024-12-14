import cirq

code = """
import cirq

def create_phase_estimation_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(4)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    for k, q in enumerate(qubits):
        circuit.append(cirq.X(q) ** (2 ** k))
    circuit.append(cirq.measure(*qubits, key='result'))
    return circuit



@app.route("/phaseEstimationCircuit", methods=["GET"])
def phase_estimation_circuit():
    circuit = create_phase_estimation_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = 
    This circuit performs Quantum Phase Estimation.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - Controlled-U: Control operations based on the unitary to estimate its phase.
    

    return jsonify(
        {
            "name": "Phase Estimation Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
        }
    )
"""


def create_phase_estimation_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(4)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    for k, q in enumerate(qubits):
        circuit.append(cirq.X(q) ** (2**k))
    circuit.append(cirq.measure(*qubits, key="result"))
    return {"circuit":circuit , "code":code}
