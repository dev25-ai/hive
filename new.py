from sympy import symbols, Implies, And
from sympy.logic.boolalg import simplify_logic

# Define symbols
A, B, C = symbols('A B C')

# Define premises and conclusion
premise1 = Implies(A, B)
premise2 = Implies(B, C)
conclusion = Implies(A, C)

# Combine premises
premises = And(premise1, premise2)

# Check if the premises imply the conclusion
result = Implies(premises, conclusion)

# Simplify the result to see if it holds as a tautology
simplified_result = simplify_logic(result)

# Print the result
print("Do the premises imply the conclusion?", simplified_result)
