length = float(input("Enter the length of the wall (in meters): "))
width = float(input("Enter the width of the wall (in meters): "))
height = float(input("Enter the height of the wall (in meters): "))
cost_per_sq_meter = float(input("Enter the cost of painting per square meter: "))

wall_area = height * length

total_area = 4 * wall_area

total_cost = total_area * cost_per_sq_meter

print("Total cost of painting the interior walls: {:.2f}".format(total_cost))