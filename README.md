# GelberGroupTakeHomeProgrammingProblem

This is a console only python program that implements a cashier line simulation. It can be run by calling "sim.py" within the folders directory and reads input from the "input.txt" file . It prints the resulting ending time to the console while also returning the ending time for testing. In the simulation, customers arrive at a set of registers to check out. Each register is run by a cashier who serves customers on a first-come, first-served basis.

The input file is in the form of a single integer, the number of registers, followed by a list of zero or more pairs. Each pair specifies the type of customer, the time in minutes from start when a customer arrives to the set of registers, and the number of items that customer has. Each pair appears white-space separated on a line by itself in the input file. See any of the files in the "TestInputs" folder for examples.

The rules of the simulation are as follows:
1) The number of registers is specified by the problem inputs; registers are numbered 1, 2, 3...n for
n registers.
2) Time is measured in minutes.
3) The grocery store always has a single cashier in training. This cashier is always assigned to the
highest numbered register.
4) Regular registers take one minute to process each customer's item. The register staffed by the
cashier in training takes two minutes for each item. So a customer with n items at a regular
register takes n minutes to check out. However, if the customer ends up at the last register, it
will take 2n minutes to check out.
5) The simulation starts at t=0. At that time all registers are empty (no customers in line).
6) Two types of customers arrive at the registers:
a. Customer Type A always chooses the register with the shortest line (fewest number of
customers in line).
b. Customer Type B looks at the last customer in each line, and always chooses to be
behind the customer with the fewest number of items left to check out, regardless of 
how many other customers are in the line or how many items they have. Customer Type
B will always choose an empty line before a line with any customers in it.
7) Customers just finishing checking out do not count as being in line (for either kind of Customer).
8) If two or more customers arrive at the same time, those with fewer items choose registers
before those with more, and if they have the same number of items then type A's choose before
type B's.

Lastly, the time is printed out in console in the form "Finished at: t=*time* minutes", where time is the resulting ending time.

To run your code, type "sim.py" followed by the name of the input file
To test your code using the example test cases, simply type "test.py" in the command line.
