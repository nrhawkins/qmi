"""Deutsch's Algorithm

Demonstrates quantum parallelism and interference.

Takes a black-box oracle, implementing a Boolean function f(x),
and determines whether f(0) or f(1) have the same parity using
just one query.

=== Example Output ===

Secret function:
f(x) = <0, 1>

Circuit:
0: -------H---@---H---M('result')---
1: ---X---H---X---------------------

Result f(0)+f(1):
result = 1
"""

import random
import cirq
from cirq import H, X, CNOT, measure


def main():
    # Choose qubits to use
    q0, q1 = cirq.LineQubit.range(2)

    # Pick a secret 2-bit function and create a circuit to query the oracle
    # values can be: [0,0], [0,1], [1,0], [1,1]
    secret_function = [random.randint(0, 1) for x in range(2)]
    oracle = make_oracle(q0, q1, secret_function)

    print("Secret function:\nf(x) = <{}>".format(
        ", ".join(str(e) for e in secret_function)))

    # Embed the oracle into a quantum circuit querying it exactly once.
    circuit = make_deutsch_circuit(q0, q1, oracle)
    print("Circuit:")
    print(circuit)

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    print("Result of f(0)+f(1):")
    print(result)


def make_oracle(q0, q1, secret_function):
    """Gates implementing the secret function f(x)."""

    # coverage: ignore
    if secret_function[0]:
        yield [CNOT(q0, q1), X(q1)]

    if secret_function[1]:
        yield CNOT(q0, q1)


def make_deutsch_circuit(q0, q1, oracle):
    c = cirq.Circuit()

    # Initialize qubits
    c.append([X(q1), H(q1), H(q0)])

    # Query oracle
    c.append(oracle)

    # Measure in X basis
    c.append([H(q0), measure(q0, key="result")])
    return c


if __name__ == "__main__":
    main()
