import numpy as np
import matplotlib.pyplot as plt

class Mandlebrot:


def main():

    """
    when creating an object, pass through the domain and range of Re(C) 
    and Im(C)
    """

    real_lower = input("Set the lower domain for Re(C): ")
    real_upper = input("Set the upper domain for Re(C): ")

    imaginary_lower = input("Set the lower range for Im(C): ")
    imaginary_upper = input("Set the upper range for Im(C): ")

    plt.show()

if __name__ == "__main__":
    main()