import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def f(x, y):
    return 3*x**2 - 2*y**2

# Generate x and y values
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
x, y = np.meshgrid(x, y)

# Calculate z values
z = f(x, y)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
ax.plot_surface(x, y, z, cmap='coolwarm', edgecolor='none')

# Saddle point at (0,0)
ax.scatter(0, 0, 0, color='r', s=100)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Saddle Point at (0, 0) for f(x, y) = 3x^2 - 2y^2')

plt.show()
