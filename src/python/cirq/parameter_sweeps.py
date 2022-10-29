import cirq

# Gates can have symbols as free parameters w/i the circuit
# e.g. variational algs have parameters to optimize a cost function
# e.g. can be useful in a variety of circumstances

# Using sympy, adds sympy.Symbol as a parameter to a gate or an operation
# Use Sweep to fill in the possible values of each parameter
# Possibilities for a Sweep:
#    Points, Linspace, ListSweep, Zip, Product (Cartesian)

# Sweep an exponent of an X gate

import matplotlib.pyplot as plt
import sympy

# Perform an X gate with variable exponent
q = cirq.GridQubit(1, 1)
circuit = cirq.Circuit(cirq.X(q) ** sympy.Symbol('t'),
                       cirq.measure(q, key="m"))

# Sweep exponent from zero (off) to one (on) and back to two (off)
param_sweep = cirq.Linspace("t", start=0, stop=2, length=200)

# Simulate the sweep
s = cirq.Simulator()
trials = s.run_sweep(circuit, param_sweep, repetitions=1000)

# Plot the results
x_data = [trial.params["t"] for trial in trials]
y_data = [trial.histogram(key="m")[1] / 1000.0 for trial in trials]
plt.scatter("t", "p", data={"t": x_data, "p": y_data})
plt.show()
