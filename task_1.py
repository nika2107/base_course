import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
R = 5

x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

lat = 70
lat_rad = np.radians(lat)
circle_x = R * np.cos(lat_rad) * np.cos(phi)
circle_y = R * np.cos(lat_rad) * np.sin(phi)
circle_z = R * np.sin(lat_rad) * np.ones_like(phi)
ax.plot(circle_x, circle_y, circle_z, color='b')

azimuth = 300
azimuth_rad = np.radians(azimuth)
vertical_circle_x = R * np.cos(phi) * np.cos(azimuth_rad)
vertical_circle_y = R * np.sin(phi) * np.cos(azimuth_rad)
vertical_circle_z = R * np.sin(phi) * np.sin(azimuth_rad)
ax.plot(vertical_circle_x, vertical_circle_y, vertical_circle_z, color='orangered')

height = -30 
height_rad = np.radians(height)

x_sun = R * (np.cos(lat_rad) * np.cos(azimuth_rad))
y_sun = R * (np.cos(lat_rad) * np.sin(azimuth_rad))
z_sun = R * (np.sin(lat_rad))

ax.scatter(x_sun, y_sun, z_sun, color="r", s=100, label='Светило')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_xlim([-R, R])
ax.set_ylim([-R, R])
ax.set_zlim([-R, R])

ax.set_aspect("equal")

plt.savefig("task_1.png")