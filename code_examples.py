import numpy as np
import matplotlib.pyplot as plt

# Define 1D arrays for x and y
x = np.linspace(-5, 5, 10)  # 10 points from -5 to 5
y = np.linspace(-5, 5, 10)  # 10 points from -5 to 5

# Create a grid using meshgrid
X, Y = np.meshgrid(x, y)

# Print the grids
print("X grid:")
print(X)
print("\nY grid:")
print(Y)

# Compute a function over the grid (e.g., z = x^2 + y^2)
Z = X**2 + Y**2

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Surface Plot")
plt.show()