import cirq

code = """

import cirq

def create_deutsch_jozsa_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    circuit.append(cirq.CNOT(qubits[0], qubits[2]))
    circuit.append(cirq.H.on_each(*qubits[:2]))
    circuit.append(cirq.measure(*qubits, key='result'))
    return circuit

@app.route("/deutschJozsaCircuit", methods=["GET"])
def deutsch_jozsa_circuit():
    data = create_deutsch_jozsa_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = 
    This circuit implements the Deutsch-Jozsa algorithm to determine if a function is constant or balanced.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - Oracle: Implements the oracle function to be tested.
    

    return jsonify(
        {
            "name": "Deutsch-Jozsa Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
               "code": code,
        }
    )
"""


def create_deutsch_jozsa_circuit():
    qubits = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    circuit.append(cirq.CNOT(qubits[0], qubits[2]))
    circuit.append(cirq.H.on_each(*qubits[:2]))
    circuit.append(cirq.measure(*qubits, key="result"))
    return {"circuit": circuit, "code": code}
