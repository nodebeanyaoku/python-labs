# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

radius = 3.14
height = 5
pi = 3.14159

# pir2
vol_cylinder = pi * radius**2 * height
print(vol_cylinder) 

# 2pirh + 2pir2
sa_cylinder = (2 * pi * radius * height) + (2 * pi * radius**2) 
print(sa_cylinder)


