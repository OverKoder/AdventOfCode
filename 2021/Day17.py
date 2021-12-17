# No matter the horizontal velocity, the maximum y position must be one such that
# from y = 0 can get to y = -76 in just 1 step. The vertical velocity increase by 1 in each step
# this means that the maximum y position must be 75 * 76 // 2
print("Part 1 sol:", (75*76) // 2)

# Brute force approximation, for every possible x speed try the y speed and see if it land on the target zone
sols = 0
for x_speed in range(24, 309 + 1):
    for y_speed in range(-76, 75 + 1):
        x, y = 0, 0
        drag, gravity = 0, 0

        # Condition that we do not miss the target zone
        while x <= 309 and y >= -76:

            # If inside the target zone
            if 287 <= x <= 309 and -48 >= y >= -76:
                sols += 1
                break
            x += x_speed - drag
            y += y_speed + gravity

            # Gravity always substracts 1
            gravity -= 1

            # Once the drag reaches the speed we stop substracting 1
            drag = drag if drag == x_speed else drag + 1

print("Part 2 solution: ",sols)



        

