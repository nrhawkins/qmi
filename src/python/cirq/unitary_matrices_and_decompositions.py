import cirq

# Most quantum operations have a unitary matrix representation
# gates, operations, circuits have a unitary matrix representing the object

print("Unitary of the X gate")
print(cirq.unitary(cirq.X))

print("Unitary of SWAP operator on two qubits.")
q0, q1 = cirq.LineQubit.range(2)
print(cirq.unitary(cirq.SWAP(q0, q1)))

print("Unitary of a sample circuit")
print(cirq.unitary(cirq.Circuit(cirq.X(q0), cirq.SWAP(q0, q1))))

# Decompose a Hadamard gate into X and Y gates
print("Decompose a Hadamard gate into X and Y gates")
print(cirq.decompose(cirq.H(cirq.LineQubit(0))))
cq = cirq.decompose(cirq.H(cirq.LineQubit(0)))
print(type(cq), "length:", len(cq))

# Decompose a 3-qubit Toffoli gate, equiv to a controlled-controlled-X gate
# Many devices do not support a three qubit gate, so it's important
# Decomposes into a simpler set of one-qubit gates and CZ gates at the cost of
# lengthening the circuit considerably
print("Decompose Toffoli gate, creates a much longer circuit")
q0, q1, q2 = cirq.LineQubit.range(3)
print(cirq.Circuit(cirq.decompose(cirq.TOFFOLI(q0, q1, q2))))

# Some devices will automatically decompose gates that they do not support
# For example, the Foxtail device does not support the SWAP gate
print("Foxtail device does not support SWAP, automatically decomposes it")
swap = cirq.SWAP(cirq.GridQubit(0, 0), cirq.GridQubit(0, 1))
print(cirq.Circuit(swap, device=cirq.google.Foxtail))

# Optimizer can take a circuit and modify it
# Make it more efficient and shorter by combining or modifying operations
# In theory, the optimizer can do any sort of circuit manipulation
# eg. MergeSingleQubitGates optimizer merges consecutive single-qubit
# operations into a single PhasedXZ operation
q = cirq.GridQubit(1, 1)
optimizer = cirq.MergeSingleQubitGates()
c = cirq.Circuit(cirq.X(q)**0.25, cirq.Y(q)**0.25, cirq.Z(q)**0.25)
print("X, Y, Z")
print(c)
print("optimize the circuit")
optimizer.optimize_circuit(c)
print(c)

# See documentation:
# Other optimizers can assist in transforming a circuit into operations
# that are native operations on specific hardware devices
# You can create your own optimizers
