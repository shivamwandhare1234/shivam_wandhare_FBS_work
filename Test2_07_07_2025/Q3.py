radius = 20
rect_length = 50
rect_breadth = 40
cost_per_meter = 35
num_wires = 5

pi = 3.1416

rect_perimeter = rect_length + 2 * rect_breadth
semicircle_perimeter = pi * radius
total_perimeter = rect_perimeter + semicircle_perimeter
total_wire_length = total_perimeter * num_wires
total_cost = total_wire_length * cost_per_meter

print(f"Total cost of fencing the field is Rs.{total_cost:.2f}")
