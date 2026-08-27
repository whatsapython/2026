# Projectile Calculator
# You are building this yourself. Cursor is only a coach.

# Challenge 1 instructions are in the chat.
# Write your code below this line.

import math
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

name = input("Enter your name: ").strip()
if name == "":
    print("You did not enter a name.")
    name = input("Enter your name: ").strip()

print("Hello, " + name + "!")

print ("Welcome to the Projectile Calculator, " + name + "!")
print ("This program will calculate the trajectory of a projectile given its initial velocity and angle of launch.")

G = 9.81

while True: # outer: whole calculation
    while True: # get velocity
        try:
            initial_velocity = float(input("Enter the initial velocity of the projectile (m/s): "))
            if initial_velocity > 0:
                break
            print("The initial velocity must be greater than 0.")
        except ValueError:
            print("Please enter a number.")
    while True: # get angle
        try:
            angle_of_launch = float(input("Enter the angle of launch of the projectile (degrees): "))
            if angle_of_launch > 0 and angle_of_launch < 90:
                break
            print("The angle of launch must be between 0 and 90 degrees.")
        except ValueError:
            print("Please enter a number.")

# calculate the horizontal and vertical components of the initial velocity
    horizontal_velocity = initial_velocity * math.cos(math.radians(angle_of_launch))
    vertical_velocity = initial_velocity * math.sin(math.radians(angle_of_launch))

    print ("The horizontal velocity of the projectile is",  round(horizontal_velocity, 2), "m/s")
    print ("The vertical velocity of the projectile is",  round(vertical_velocity, 2), "m/s")

    time_of_flight = 2 * vertical_velocity / G # 9.81 is the acceleration due to gravity in m/s^2
    
    if HAS_MATPLOTLIB:
        x_points = []
        y_points = []
        t= 0
        while t <= time_of_flight:
            x_points.append(horizontal_velocity * t)
            y_points.append(vertical_velocity * t - 0.5 * G * t ** 2)
            t += 0.01

        plt.plot(x_points, y_points)
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.title("Projectile Path")
        plt.grid(True)
        plt.show()
    else:
        print("Matplotlib is not installed. Please install it to see the plot.")

    print ("The time of flight of the projectile is",  round(time_of_flight, 2), "seconds")

    horizontal_distance = horizontal_velocity * time_of_flight
    print ("The horizontal distance traveled by the projectile is",round(horizontal_distance, 2), "meters")

    maximum_height = (vertical_velocity ** 2) / (2 * G)
    print ("The maximum height reached by the projectile is", round(maximum_height, 2), "meters")

    angle_of_impact = math.atan(vertical_velocity / horizontal_velocity)
    degrees_of_impact = math.degrees(angle_of_impact)
    print ("The angle of impact of the projectile is", round(degrees_of_impact, 2), "degrees")


    print ("Thank you for using the Projectile Calculator, " + name + "!")
    again = input("Calculate another? (y/n): ").strip().lower()
    if again == "n":
        print("Goodbye, " + name + "!")
        break

