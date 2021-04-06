def  fetchInputFile(file):
    #Opens the input file
    f = open(file, "r")

    #Reads the first line to learn the number of registers
    numRegisters = int(f.readline())

    #Reads the second line to learn of the first customer
    customer = f.readline()

    #Creates a list of customers
    customers = []

    #Continually reads for new customers until it reachs the end of the input file
    while customer:
        customers.append(customer.split())
        customer = f.readline()

    #Returns a tuple that contains the number of registers and the list of customers
    return(numRegisters,customers)


def newCustomerEnters(customer, registers):

    #Logic for a type A customer
    if customer[0] == 'A':

        #Finds the register with the fewest people in line
        numRegister = registers.index(min(registers, key = len))

        #Gets the number of items the new customer has
        numItems = int(customer[2])

        #Returns the register the customer picks and the number of items they have
        return (numRegister, numItems)

    #Logic for a type B customer
    if customer[0] == 'B':

        #Creates a list of the number of items held by the last person in each line
        lastPersonItems = [x[-1] if x else 0 for x in registers]

        #Finds the register with the fewest items held by the last person in each line
        numRegister = lastPersonItems.index(min(lastPersonItems))

        #Gets the number of items the new customer has
        numItems = int(customer[2])

        #Returns the register the customer picks and the number of items they have
        return (numRegister, numItems)

def sortCustomers():
    pass
