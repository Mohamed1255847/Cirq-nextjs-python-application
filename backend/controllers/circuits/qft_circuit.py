import cirq

code = """
import cirq

def create_qft_circuit():
    q = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q[2]))
    circuit.append(cirq.CZPowGate(exponent=1/2)(q[1], q[2]))
    circuit.append(cirq.H(q[1]))
    circuit.append(cirq.CZPowGate(exponent=1/4)(q[0], q[2]))
    circuit.append(cirq.CZPowGate(exponent=1/2)(q[0], q[1]))
    circuit.append(cirq.H(q[0]))
    circuit.append(cirq.measure(*q, key="result"))
    return circuit
@app.route("/qftCircuit", methods=["GET"])
def qft_circuit():
    circuit = create_qft_circuit()
    result = run_circuit(circuit)
    result_dict = result.histogram(key="result")

    # Annotated circuit description
    circuit_description = 
    This circuit performs the Quantum Fourier Transform.
    Gate Operations:
    - H (Hadamard Gate): Applies a Hadamard operation putting a qubit into superposition.
    - R (Rotation Gates): Rotations by different angles.
    

    return jsonify(
        {
            "name": "QFT Circuit",
            "description": circuit_description,
            "circuit": str(circuit),
            "results": result_dict,
        }
    )

"""


def create_qft_circuit():
    q = [cirq.GridQubit(i, 0) for i in range(3)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q[2]))
    circuit.append(cirq.CZPowGate(exponent=1 / 2)(q[1], q[2]))
    circuit.append(cirq.H(q[1]))
    circuit.append(cirq.CZPowGate(exponent=1 / 4)(q[0], q[2]))
    circuit.append(cirq.CZPowGate(exponent=1 / 2)(q[0], q[1]))
    circuit.append(cirq.H(q[0]))
    circuit.append(cirq.measure(*q, key="result"))
    return {"circuit": circuit, "code": code}
