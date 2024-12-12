import cirq

def create_grover_circuit(num_qubits, oracle):
    qubits = [cirq.GridQubit(i, 0) for i in range(num_qubits)]
    circuit = cirq.Circuit()

    # Apply Hadamard gates
    circuit.append([cirq.H(q) for q in qubits])

    # Apply the oracle
    circuit.append(oracle)

    # Apply the Grover diffusion operator
    circuit.append([cirq.H(q) for q in qubits])
    circuit.append([cirq.X(q) for q in qubits])
    circuit.append(cirq.Z.controlled(num_qubits - 1)(*qubits))
    circuit.append([cirq.X(q) for q in qubits])
    circuit.append([cirq.H(q) for q in qubits])

    return circuit


#@app.route("/groverCircuit", methods=["POST"])
#def grover_circuit():
    #try:
        #print(request.data)  # Add this line to print raw request data
        #data = request.get_json()
        #print(data)  # Add this line to print parsed JSON data
        #num_qubits = data.get('num_qubits', 2)  # Default to 2 qubits if not specified
        #oracle = cirq.Circuit([cirq.Z(cirq.GridQubit(i, 0)) for i in range(num_qubits)])  # Define a simple oracle
        #circuit = create_grover_circuit(num_qubits, oracle)
        #result = run_circuit(circuit)
        #return jsonify({'circuit': str(circuit), 'results': result})
    #except Exception as e:
       # return jsonify({'error': str(e)}), 400