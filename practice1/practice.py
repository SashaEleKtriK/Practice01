import math

d1 = float(input('Shortest way to water (yards): '))
d2 = float(input('Shortest way on the water to a drowning man (foots): '))
h = float(input('Lateral displacement from drowning man to savior (yards): '))
sand_speed = float(input('Moving speed on sand (miles/hour): '))
water_coefficient = float(input('Moving speed coefficient in water (n): '))
angle = float(input('On ground start angle (degrees): '))
foot_to_mile = 0.000189394
yard_to_mile = 0.000568182
to_miles_per_second = 1/3600
d1 = d1 * yard_to_mile
d2 = d2 * foot_to_mile
h = h * yard_to_mile
sand_speed = sand_speed * to_miles_per_second
radian_angle = angle * math.pi / 180
x = (math.tan(radian_angle) * d1) # displacement on ground
l_sand = ((x ** 2) + d1 ** 2) ** (1 / 2)
l_water = (((h-x) ** 2) + d2 ** 2) ** (1 / 2)
time_on_ground = l_sand / sand_speed
time_in_water = l_water * water_coefficient / sand_speed
result_time = time_on_ground + time_in_water
print("Result time, s ", "{:0.1f}".format(result_time))