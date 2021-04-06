import sys
from helper import *

def simulation(file):
    #Reads through the input file and sets the number of registers and a list of customers
    numRegisters, customers = fetchInputFile(file)

    #Sorts the customers first by the time the enter, then the number of items, and lastly by customer type
    customers = sorted(customers, key=lambda x: (x[1], x[2], x[0]))

    #Creates a list of lists representing the different registers at checkout
    registers = [[] for _ in range(numRegisters)]

    #Sets the starting time to zero
    time = 0

    #Creates a training flag to allow the new hire double time
    trainingFlag = False

    #Simulation runs while there are any potential customers or anyone checking out
    while customers or any(registers):

        #Checks if there is a new customer approaching checkout at the current time
        if customers and int(customers[0][1]) == time:

            #Gets the register the customer will pick and they number of items they have
            numRegister, numItems = newCustomerEnters(customers.pop(0), registers)

            #Adds that customer and there item to the register that they picked
            registers[numRegister].extend([numItems])

            #Starts a new iteration in case there are more new customers at the same time
            continue

        #Iterates through every register but the training one
        for i in range(0, numRegisters-1):

            #Checks if there is at least one person in line
            if registers[i]:

                #Checks out one item
                registers[i][0] -= 1

                #Checks if the customer is out of items
                if registers[i][0] == 0:

                    #Removes the customer from the line
                    registers[i].pop(0)

        #Checks there is at least one person in line at the training register
        if registers[-1]:

            #Checks if the cashier in training checked out some item last time interval
            if trainingFlag == True:

                #Checks out one item
                registers[-1][0] -= 1

                #Checks if the customer is out of items
                if registers[-1][0] == 0:

                    #Removes the customer from the line
                    registers[-1].pop(0)

                #inverts the trainingFlag so they do not checkout an item next time interval
                trainingFlag = False

            #Otherwise inverts the trainingFlag so they checkout an item next time interval
            else:
                trainingFlag = True
        #Updates the time interval
        time += 1

    #Prints out the final time
    print("Finished at: t=" + str(time))

    #Returns the ending time for testing
    return time

if __name__ == "__main__":
    simulation(sys.argv[1])
