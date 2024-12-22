# -------------------------------------------------------------------
# PHY 291 HW-2 Problem 3 -- Calculations
# -------------------------------------------------------------------

# Imports
from math import radians, degrees, sin, cos, sqrt, atan2

# Define constants
g = 9.806           # N/kg -- local gravitational constant

# define givens
h = 10             # m -- height for which we want velocity
v0 = 20            # m/s -- initial speed
q0 = radians(50)   # degrees (converted) -- initial direction

# Calculate initial velocity components
v0x = v0 * cos(q0)
v0y = v0 * sin(q0)

# Calculate velocity components at height `h`
vx = v0x
vy = sqrt(v0y**2 - 2 * g * h)

# Calculate magnitude and direction
v = sqrt(vx**2 + vy**2)
q = atan2(vy, vx)

# Report out the result
print(f"At a height of {h} m, the final velocity is {v:.2f} m/s")
print(f"at an angle of {degrees(q):.2f} degrees above horizontal.")

# -------------------------------------------------------------------
