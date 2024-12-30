# user-input.py

# Imports:
from math import sin, cos, radians

# Ask for the magnitude:
mag = input("Vector's magnitude (without units): ")
mag = float(mag)
assert mag >= 0, "The magnitude must be non-negative!"

# Ask for the direction:
angle = input("Vector's direction (in degrees CCW from +x axis): ")
angle = float(angle)

# Calculate components:
x = mag * cos(radians(angle))
y = mag * sin(radians(angle))

# Report out:
print(f"=> The vector's components are ({x:.3g}, {y:.3g}).")
