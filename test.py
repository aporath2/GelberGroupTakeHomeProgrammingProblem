from sim import simulation

#General example one
assert(simulation("TestInputs/example1.txt") == 7)

#General example two
assert(simulation("TestInputs/example2.txt") == 13)

#Illustrates the requirement that departing customers aren’t counted in line
assert(simulation("TestInputs/example3.txt") == 6)

#Illustrates the requirement that customers with fewer items choose lines sooner
assert(simulation("TestInputs/example4.txt") == 9)

# Illustrates the requirement that customers of type A choose before customers of type B
assert(simulation("TestInputs/example5.txt") == 11)

print("Passed all test cases")
