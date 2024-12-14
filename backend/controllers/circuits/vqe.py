import cirq

code = """
def create_vqe_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(2)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.CX(qubits[0], qubits[1]))
    circuit.append(cirq.measure(*qubits, key='result'))
    return circuit



@app.route("/vqeCircuit", methods=["GET"])
def vqe_circuit():
    circuit = create_vqe_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description =                
    This circuit implements the Variational Quantum Eigensolver.
    Gate Operations:
    - Various parameterized gates applied to prepare and measure a quantum state.


    return jsonify(
        {
            "name": "VQE Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
        }
    )


"""


def create_vqe_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(2)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.CX(qubits[0], qubits[1]))
    circuit.append(cirq.measure(*qubits, key="result"))
    return {"circuit": circuit, "code": code}
