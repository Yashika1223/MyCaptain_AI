# two sets
setE = {0, 2, 4, 6, 8}
setN = {1, 2, 3, 4, 5}

# Perform set operations
union_result = setE.union(setN)
intersection_result = setE.intersection(setN)
difference_result = setE.difference(setN)
symmetric_difference_result = setE.symmetric_difference(setN)

# Display the results
print(f"Union of E and N is {union_result}")
print(f"Intersection of E and N is {intersection_result}")
print(f"Difference of E and N is {difference_result}")
print(f"Symmetric difference of E and N is {symmetric_difference_result}")
