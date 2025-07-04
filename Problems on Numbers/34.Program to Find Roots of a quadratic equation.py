# Problem Statement: The standard form of a quadratic equation is:

# ax2 + bx + c = 0, where a, b and c are real numbers and a != 0

# You have given a, b, c of the equation, you have found the roots of the equation.

# Examples:

# Example 1:
# Input: a = 1, b = -3, c = -10
# Output: Roots are real and different, i.e(5 , -2).

# Example2:

# Input: a = 1, b = 1, c = 1
# Output: Roots are complex, i.e-(-0.5+i1.732 , -0.5-i1.732).


a, b, c = 1, 1, 1
d = (b**2) - 4 * a * c

if d > 0:
    r1 = ((-b) + (d**0.5)) / (2 * a)
    r2 = ((-b) - (d**0.5)) / (2 * a)
    print("Roots are real and different:", r1, ",", r2)

elif d == 0:
    r1 = -b / (2 * a)
    print("Roots are real and same:", r1, ",", r1)

else:
    real = -b / (2 * a)
    imag = ((-d)**0.5) / (2 * a)
    print("Roots are complex:", f"{real}+i{imag}", ",", f"{real}-i{imag}")
