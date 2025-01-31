'''
To find the eigenvalue and eigenvector of an arbitrary 4x4 matrix using power method
'''

# Matrix under consideration
a = [[2, 1, 1, 0], 
     [1, 1 ,0, 1], 
     [1, 0,1 , 1], 
     [0, 1 , 1 , 2]]

# Initial vector guess
v = [1, 1, 1, 1]

def multiplication_of_matrix(a, v):
    j = [0, 0, 0, 0]  # Initialize the result vector
    for i in range(4):
        j[i] = sum(a[i][k] * v[k] for k in range(4))  # Matrix-vector multiplication
    return j

def max_term(j):
    m = abs(j[0])  # Start with the absolute value of the first element
    for i in range(4):
        m = max(m, abs(j[i]))  # Find the maximum absolute value
    return m

def eigenvector(j, m):
    for i in range(4):
        j[i] = j[i] / m  # Normalize the vector
    return j

def power_method(a, v):
    val0 = max_term(v)
    val1 = 0
    while abs(val1 - val0) >= 10**-6:  # Continue until convergence
        vect0 = multiplication_of_matrix(a, v)  # Multiply matrix by current vector
        val0, val1 = val1, max_term(vect0)  # Update eigenvalue
        # print(f'Working with eigenvalue: {val1}')
        v = eigenvector(vect0, val1)  # Normalize the vector
    return val1, v

# Running the power method
eigenvalue, eigenvector = power_method(a, v) #as the output is a tuple

# Output the result
print(f'The eigenvalue is {eigenvalue:6f}')
print(f'The eigenvector is {[f"{eigenvector[i]:.6f}" for i in range(4)]}')

