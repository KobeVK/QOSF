# Importing necessary libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.visualization import *

# Implementing the Bernstein-Vazirani Oracle
def bv_circuit(a, b):
    """
    This function creates a quantum circuit that can determine the larger of two numbers using the Bernstein-Vazirani algorithm.
    It takes two integer inputs a and b, and returns the corresponding Bernstein-Vazirani Oracle quantum circuit.
    """
    # Marking the solution
    A = int(a/max(a, b))
    B = int(b/max(a, b))

    # Creating the base circuit
    q = QuantumRegister(3, "q") 
    c = ClassicalRegister(2, "c")
    bvqc = QuantumCircuit(q, c)
    
    # Applying the Hadamard's sandwich
    bvqc.x(2)
    bvqc.barrier()
    bvqc.h(0)
    bvqc.h(1)
    bvqc.h(2)
    
    # Applying the Oracle
    if(A == 1):
        bvqc.cx(0, 2)
    elif(B == 1):
        bvqc.cx(1, 2)

    # Closing the Hadamard's sandwich
    bvqc.h(0)
    bvqc.h(1)
    bvqc.h(2)
    bvqc.barrier()

    # Measuring the first two qubits and storing the result in the classical register
    bvqc.measure([0, 1],[0, 1])

    return bvqc

def find_the_largest_number(a, b):
    """
    This function finds the larger of two numbers using the Bernstein-Vazirani algorithm.
    It takes two integer inputs a and b, and returns the larger of the two numbers along with the circuit visualization and a histogram of the measurement results.
    """
    # Building the Bernstein-Vazirani circuit for the given input
    qc = bv_circuit(a, b)
    
    # backend for simulation
    aer = Aer.get_backend('aer_simulator')
    
    # Executing the circuit and obtaining the counts
    counts = execute(qc, backend = aer, shots = 1024).result().get_counts()
    
    # Determining the most frequently occurring result
    most_frequent_result = counts.most_frequent()
    
    # Creating a list with the input numbers and returning the larger number based on the measured output
    num_list = [a, b]
    result = num_list[int(most_frequent_result, 2)-1]
    
    # Drawing the circuit and plotting a histogram of the counts
    circuit_visualization = qc.draw(output='mpl')
    histogram = plot_histogram(counts)
    
    return result, circuit_visualization, histogram

# Finding the larger of two numbers (7 and -4) using the Bernstein-Vazirani algorithm
result, circuit_visualization, histogram = find_the_largest_number(7, -4)

# Printing the result
print("The larger of the two numbers is: ", result)

# Displaying the circuit visualization
circuit_visualization

# Displaying the histogram
# histogram
