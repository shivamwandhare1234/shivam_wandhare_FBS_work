cost_interior_wall=float(input("Enter the cost for interior wall painting: "))
cost_exterior_wall=float(input("Enter the cost for exterior wall painting: "))

side=float(input("Enter The side of Building: "))

total_area=4*side*side

total_cost=(total_area*cost_interior_wall) + (total_area*cost_exterior_wall)

print("The total cost of painting 2 rooms is: ",2*total_cost)