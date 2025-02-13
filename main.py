import numpy as np
import matplotlib.pyplot as plt

class Mandlebrot:

    def __init__(
        self, real_lower, real_upper, imaginary_lower, imaginary_upper
    ):
        self.real_lower = real_lower
        self.real_upper = real_upper
        self.imaginary_lower = imaginary_lower
        self.imaginary_upper = imaginary_upper

        # instantiate 2d grid (512 x 512) bounded by given values
        self.real_axis = np.linspace(real_lower, real_upper, 512)
        self.imaginary_axis = np.linspace(
            imaginary_lower, imaginary_upper, 512
        )

        # for complex values
        self.XX, self.YY = np.meshgrid(self.real_axis, self.imaginary_axis)
        self.complex_array = self.XX + self.YY*1j

        # empty grid of zeros that will be updated with corresponding n value 
        self.mandlebrot_grid = np.zeros((512, 512))

    """
    calculates and displays mandlebrot grid
    """
    def generate_mandlebrot(self):

        """
        values of c (eg 3 + 2i or  2.4 - 9.7i) are determined by the bounds 
        of user input

        iterate through 2d grid with x and y coordinates representing complex 
        numbers c (512x512 means 262144 iterations)

            if |z_n| > 2 where z_(n+1) = z_n^2 + c, then set the empty
            grid coordinate -number of iterations- to n ie n = 30 
        """
        for i, row in enumerate(self.complex_array):
            for j, complex_number in enumerate(row):
                z = 0 + 0j
                for iteration_number in range(255):
                    z = z**2 + complex_number
                    if abs(z) > 2:
                        self.mandlebrot_grid[i][j] = iteration_number
                        break

        plt.imshow(
            self.mandlebrot_grid, 
            extent=(
                self.real_lower, self.real_upper, self.imaginary_lower,
                self.imaginary_upper
            ),
            interpolation='none', 
            cmap='hot'
        )
        plt.colorbar()
        plt.show()


        

def main():

    """
    when creating an object, pass through the domain and range of Re(C) 
    and Im(C)
    """
    print("Insert values for domain and range to view ")

    # real_lower = -2.025
    # real_upper = 0.6
    real_lower = float(input("Set the lower domain for Re(C): "))
    real_upper = float(input("Set the upper domain for Re(C): "))
    # imaginary_lower = -1.125
    # imaginary_upper = 1.125
    imaginary_lower = float(input("Set the lower range for Im(C): "))
    imaginary_upper = float(input("Set the upper range for Im(C): "))

    user_mandlebrot = Mandlebrot(
        real_lower, real_upper, imaginary_lower, imaginary_upper
    )

    user_mandlebrot.generate_mandlebrot()

if __name__ == "__main__":
    main()