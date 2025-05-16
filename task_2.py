import numpy as np
import matplotlib.pyplot as plt

R = 5  
latitude = 10  
declination = 20  
hour_angle = 15 

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

circ_phi = np.linspace(0, 2 * np.pi, 100)
circ_x = R * np.cos(circ_phi) * np.cos(np.radians(latitude))
circ_y = R * np.sin(circ_phi) * np.cos(np.radians(latitude))
circ_z = R * np.sin(np.radians(latitude))
ax.plot(circ_x, circ_y, circ_z, color='orangered')

circ_theta = np.linspace(-np.pi / 2 + np.radians(declination), np.pi / 2 + np.radians(declination), 100)
circ_x2 = R * np.cos(hour_angle) * np.cos(circ_theta)
circ_y2 = R * np.sin(hour_angle) * np.cos(circ_theta)
circ_z2 = R * np.sin(circ_theta)
ax.plot(circ_x2, circ_y2, circ_z2, color='darkblue')

light_source_x = R * np.cos(np.radians(hour_angle)) * np.cos(np.radians(declination))
light_source_y = R * np.sin(np.radians(hour_angle)) * np.cos(np.radians(declination))
light_source_z = R * np.sin(np.radians(declination))
ax.scatter(light_source_x, light_source_y, light_source_z, color='r', s=100, label='Светило')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

ax.set_aspect("equal")

plt.savefig("task_2.png")