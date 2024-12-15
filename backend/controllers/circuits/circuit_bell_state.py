import cirq

code = """
import cirq

def create_bell_state_circuit():
    qubits = [cirq.NamedQubit('q0'), cirq.NamedQubit('q1')]
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  
        cirq.CNOT(qubits[0], qubits[1]),  
        cirq.measure(*qubits, key='result')  
    )
    return {"circuit": circuit, "code": code}



@app.route("/bellStateCircuit", methods=["GET"])
def bell_state_circuit():
    data = create_bell_state_circuit()
    circuit = data["circuit"]
    code = data["code"]
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = 
    This circuit creates a Bell state, entangling two qubits.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - @ (CNOT Gate Control): Control qubit for the CNOT operation.
    - X (CNOT Gate Target): Target qubit for the CNOT operation.
    - M (Measurement): Measures the state of the qubit.
    

    return jsonify(
        {
            "name": "Bell State Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
            "code": code,
        }
    )

"""


def create_bell_state_circuit():
    qubits = [cirq.NamedQubit("q0"), cirq.NamedQubit("q1")]
    circuit=cirq.Circuit()
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.measure(*qubits, key="result"))
    return {"circuit": circuit, "code": code}
