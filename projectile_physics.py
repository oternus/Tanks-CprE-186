import math;

gravity = 9.8 # meters/sec

# initalAngle - user input would be in degrees 0-180
# power - user input 0-100
# idk how to do user input so I just set the angle and power to some values
# time - in seconds

initalAngle = 45
power = 50

# angle has to be in radians for math funtions to work right
inRads = math.radians(initalAngle)
time = (2 * power * math.sin(inRads)) / gravity

# displacment
disX = power * time * math.cos(inRads)
disY = (power * time * math.sin(inRads)) - (gravity * time)
# magnitude of displacement
magDis = math.sqrt(math.pow(disX, 2) + math.pow(disY, 2))

# velocity
velX = power * math.cos(inRads)
velY = (power * math.sin(inRads)) - gravity * time

# trajectory
# y=tanθ⋅x−(g/2⋅u2⋅cos2θ)⋅x2
arc = (math.tan(inRads) * disX) - (gravity/(2 * math.pow(power,2) * math.pow(math.cos(inRads),2) * math.pow(disX,2)))

# the time the max height is reached
maxHeightTime = (power * math.sin(inRads)) / gravity

# finds highest point in arc
maxHeight = (math.pow(power, 2) * math.pow(math.sin(inRads), 2)) / (2 * gravity)

# finds the total distance traveled on the x axis
totRange = (math.pow(power, 2) * math.sin(2 * inRads)) / gravity
