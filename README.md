# QOSF Mentorship Program

## Task #1: Find the largest number

---
### Task Description
1. Compare integers using quantum algorithm and return the larger number.
2. Consider an appropriate number of qubits and explain why your proposal is valid for all kinds of numbers in case 
3. Print your quantum circuit

### Solution implementation
Grover's algorithm is a quantum algorithm designed to search for a specific element in an unsorted database, and in my solution, i adapted the algorithm to perfrom integer comparison.

I divided the task into 5 sub-tasks:
1. Input preparation: 
First, we need to calculate the number of qubits required to represent our inputs integers, which is given by the formula ceil(log2(max(A, B))) + 1

    * `MAX` - Gives us the maximum value between A and B
    For example, if A = 7 and B = 11, then the maximum value is 11
    
    * `log2` - Calculate the number of qubits required because each qubit can represent two possible states (0/1).Therefore, with n qubits, we can represent 2^n possible states. In the context of comparing two integers, if the maximum value of A and B is x, then we need to represent all integers from 0 to x. The minimum number of qubits required to represent x unique values is log2(x).
    For example, if the maximum value of A and B is 7, we need to represent all integers from 0 to 7. The minimum number of qubits required is log2(8) = 3, since 2^3 = 8. Therefore, we need 3 qubits to represent all possible values of A and B.
    
    * `Ceil` - Rounding up the resault of log2(x) to the nearest integer
    
    * `+1` - An extra qubit used as an ancilla qubit to determine whether the integers are equal or not. This extra qubit is needed to ensure that the comparison operation is reversible and can be undone later in the algorithm.

2. State Preparation: 
Grover’s algorithm uses Hadamard gates to create the uniform superposition of all the states at the beginning, before it amplifies the amplitude of the solution state and suppresses the amplitudes of the other states
The reason for creating a superposition of all possible values of A and B using a Hadamard gate on each qubit is to search the input space in parallel. When we apply the Hadamard gate on each qubit, it puts that qubit in a superposition of both 0 and 1 states. This means that every possible combination of the qubits is represented in the superposition state.
By creating a superposition state, we can search for the solution to the problem in parallel rather than sequentially. This is what gives Grover's algorithm its speedup compared to classical algorithms.

3. Oracle: 
The oracle marks the state where the two input integers are equal by applying a controlled-Z gate (CZ) between the qubits that represent the most significant bit (MSB) of each input integer.
Here's how the oracle works:
    1. The first loop for i in range(num_qubits): applies an X gate to each qubit in the quantum circuit, effectively flipping the phase of the state of each qubit.

    2. The CZ gate is applied between the MSB of each input integer (which are the num_qubits-1-th qubit for both integers) with the num_qubits-1-th qubit acting as the control and the 0-th qubit acting as the target. The CZ gate flips the phase of the target qubit if the control qubit is in the state |1>.
    
    3. The second loop for i in range(num_qubits): applies another X gate to each qubit in the quantum circuit, restoring the original phase of each qubit.

4. Amplitude amplification: 
Apply Grover's algorithm amplitude amplification procedure to the superposition to amplify the marked state. Repeat this step O(√(N)) times, where N is the total number of states (in this case, 2^qubits).

5. Measurement: 
Measure the qubits and observe the result. If the result is the state where A < B, then A is less than B. Otherwise, A is greater than or equal to B.

### QA / future work
    1. make sure solution applies for all negative/positive values
    2. make sure exception is raised when charecter is passed instead of number
    3. print how many qubits used
    4. draw the circuit
    5. make sure its' working on floating points
    6. write limits (min/max values that can be compared)
    7. consider talk/demo the advantages of doing this action in the QC world
    8. display how many qubits each integer was converted, and how many qubits were used in the circuits overall

<!-- There are several potential advantages of performing integer comparison on a quantum computer using qubits over a classical computer:

Parallelism: One of the most promising advantages of quantum computing is the potential for massive parallelism. Unlike classical computers, which perform operations sequentially, quantum computers can perform many calculations in parallel by applying a quantum gate to a superposition of states. This means that a quantum computer could potentially compare two integers in a single operation, which could significantly reduce the time required for the computation.

Algorithmic efficiency: There are certain algorithms, such as Grover's algorithm, that have been developed specifically for quantum computers and can provide exponential speedups over classical algorithms. While Grover's algorithm is not specifically designed for integer comparison, it can be adapted to perform this task efficiently on a quantum computer.

Privacy: Quantum computers offer the potential for secure communications through the use of quantum key distribution (QKD). In the context of integer comparison, QKD could be used to securely transmit the integers to be compared without the risk of interception or eavesdropping.

Complex number processing: Quantum computers are well-suited to processing complex numbers, which can be used to represent integers. This means that integer comparison could be performed more efficiently on a quantum computer than a classical computer, particularly for large integers.

However, it's worth noting that the practical advantages of using a quantum computer for integer comparison may be limited by the current state of quantum computing technology. While there have been significant advances in the development of quantum hardware and software, current quantum computers are still relatively small and error-prone, which can limit their ability to perform complex computations. Additionally, the overhead associated with converting integers to qubits and performing quantum gates can be significant, which can offset some of the potential speedup offered by quantum parallelism. -->


to fix:
    int1 = -1
    int2 = 12
    The larger integer is -1.

    int1 = -1
    int2 = -12
    math domain error

    int1 = 100
    int2 = 102123
    The larger integer is 100.
