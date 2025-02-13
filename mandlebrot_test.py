import numpy as np
import matplotlib.pyplot as plt

def mandlebrot():
    x = np.linspace(-2.025, 0.6, 512)
    y = np.linspace(-1.125, 1.125, 512)

    XX, YY = np.meshgrid(x, y)

    grid = np.zeros((512, 512))

    # c = complex(XX, YY)
    complex_array = XX + YY*1j

    print(complex_array)

    # access each value in c and run for loop
    for i, row in enumerate(complex_array):
        for j, complex_number in enumerate(row):
            z = 0 + 0j
            for iteration_number in range(255):
                z = z**2 + complex_number
                if abs(z) > 2:
                    grid[i][j] = iteration_number
                    break

    print(grid)
    plt.imshow(grid)
    plt.colorbar()
    plt.show()
        


def main():

    mandlebrot()

main()