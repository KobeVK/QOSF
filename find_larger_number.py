from math import ceil, log2 
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
import sys
from qiskit.visualization import *
from matplotlib import style
from sys import argv

int1 = 100
int2 = 102123

def compare_integers(A, B):

    # Determine the number of qubits required to represent A and B
    num_qubits = ceil(log2(max(A, B))) + 1
    print(f"number of Qbits required:", num_qubits) 
            
    # Create a quantum circuit with qubits required and one classical bit
    qc = QuantumCircuit(num_qubits, 1)
    
    # Create a superposition of all possible values of A and B using a Hadamard gate on each qubit
    for i in range(num_qubits):
        qc.h(i)
    
    # Define the oracle that marks the state where A equal to B
    for i in range(num_qubits):
        qc.x(i)
        qc.cz(num_qubits - 1, 0)
    for i in range(num_qubits):
        qc.x(i)


    # Apply Grover's algorithm amplitude amplification procedure to the superposition to amplify the marked state
    num_iterations = int(round((2 ** num_qubits) ** 0.5)) - 1
    for i in range(num_iterations):
        qc.h(range(num_qubits))
        for j in range(num_qubits):
            qc.x(j)
        qc.h(num_qubits-1)
        qc.mct(list(range(num_qubits-1)), num_qubits-1)
        qc.h(num_qubits-1)
        for j in range(num_qubits):
            qc.x(j)
        qc.h(range(num_qubits)) 

    # Measure the output qubit
    qc.measure(num_qubits-1, 0)
    # Run the circuit on a simulator
    backend = Aer.get_backend('qasm_simulator')
    shots = 1024
    result = execute(qc, backend, shots=shots).result()
    counts = result.get_counts()
    circuit_diagram = qc.draw(output='mpl')
    return counts, circuit_diagram


count, img = compare_integers(int1, int2)
if '0' in count:
    print(f"The larger integer is {int1}.")
else:
    print(f"The larger integer is {int2}.")
