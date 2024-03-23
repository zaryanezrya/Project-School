import math

def solve_square_equation(a, b, c):
    if a == 0:
        return "error"
    
    d = b*b - 4*c*a

    print("asdasdasd")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = c/x1
        return sorted([x1, x2])

    if d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return  [x]