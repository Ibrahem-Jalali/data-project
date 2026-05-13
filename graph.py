import numpy as np
import matplotlib.pyplot as plt

print("Function Grapher")
print("Example: x**2, 2*x+3, np.sin(x)")

func = input("Enter a function in terms of x: ")

x = np.linspace(-10, 10, 100)

try:
    y = eval(func)
    plt.plot(x, y)
    plt.title("Graph of " + func)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()
except:
    print("Invalid function. Try again.")
