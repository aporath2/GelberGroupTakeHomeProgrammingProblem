import sys
from helper import *

# Simulation takes in one string input, the local address of the file,
# and returns the time it took in addition to printing it to console.
def simulation(file):

    # Reads through the input file, and returns the number of registers and a list of customers
    numRegisters, customers = fetchInputFile(file)

    # Sorts the customers first by the earliest time they enter,
    # then by the fewest number of items they have,
    # and lastly by the customer type of "A" first.
    customers = sorted(customers, key=lambda x: (int(x[1]), int(x[2]), x[0]))

    # Creates a list of lists representing the different registers at checkout
    registers = [[] for _ in range(numRegisters)]

    # Sets the starting time to zero
    time = 0

    # Creates a training flag to allow the new hire double time for checkout
    trainingFlag = False

    # Simulation runs as long as there are any potential customers
    # or anyone currently waiting checking out
    while any(customers) or any(registers):

        # Checks if there is a new customer approaching checkout at the current time
        if any(customers) and int(customers[0][1]) == time:

            # Gets the register that the customer will pick and also the number of items they have
            numRegister, numItems = newCustomerEnters(customers.pop(0), registers)

            # Appends the customer's items to the register that they picked
            registers[numRegister].extend([numItems])

            # Starts a new iteration in case there are more new customers at the same time
            continue

        # Iterates through every register except for the training one
        for i in range(numRegisters-1):

            # Checks if there is at least one person in line
            if registers[i]:

                # Checks out one item from the first customer at the register
                registers[i][0] -= 1

                # Checks if the customer is out of items
                if registers[i][0] == 0:

                    # Removes the customer from the line
                    registers[i].pop(0)

        # Checks there is at least one person in line at the training register
        if registers[-1]:

            # Checks if the cashier in training checked out some item during the last time interval
            if trainingFlag == True:

                # Checks out one item
                registers[-1][0] -= 1

                # Checks if the first customer at the last register is out of items
                if registers[-1][0] == 0:

                    # Removes the first customer from the last register
                    registers[-1].pop(0)

                # Inverts the trainingFlag so the casherir in training does not checkout an item next time interval
                trainingFlag = False

            # Otherwise inverts the trainingFlag so they checkout an item next time interval
            else:
                trainingFlag = True

        # Updates the time interval
        time += 1

    # Prints out the final time in the specifeid format
    print("Finished at: t=" + str(time))

    #Returns the ending time for testing
    return time

#Runs simulation with the inputted file from console
if __name__ == "__main__":
    simulation(sys.argv[1])
