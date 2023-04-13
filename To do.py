userList = []

# Function for deleting an Item
def delOptions():
                print("Enter the index of the item you would like to remove (Condider the first index to be 1)")
                try:
                    index = int(input())
                    
                except:
                    print("Invalid input: Please enter a valid integer index")
                    delOptions()
                    return
                if index == 0:
                     print("Invalid index")
                     delOptions()
                     return
                if index:
                    index = index-1
                if index >= 1 and index <= len(userList):
                    print(f'Are you sure you want to remove "{userList[index]}" from your list? ')
                    print(' "Y"            "N" ')
                    delChoice = input()
                    if delChoice.upper() == "Y":
                        print(f"Removing {userList[index]} from list")
                        del (userList[index])
                    elif delChoice.upper() == "N":
                        userPrompt()
                    else:
                        print("Invalid input")
                        delOptions()
                else:
                    print("No such index found!")
                    print("Please select a valid index and try again")
                    print("*** Remeber to start from 0 ***")


# Termination function
def termination():
                print("Are you sure you want to exit?")
                print(' "Y"         "N" ')
                terminateRes = input()
                while terminateRes.upper() == "Y":
                    print("Exiting program...")
                    quit()
                while terminateRes.upper() == "N":
                     userPrompt()
                while terminateRes.upper() != "N" or terminateRes.upper() != "Y":
                     print("Invalid input")
                     termination()

def clearList():
    print ("ATTENTION: You are about to clear your entire to do list!")
    print(' Confirm your decision:  "Y"           "N" ')
    confirm_clear = input()
    if confirm_clear.upper() == "Y":
        print("List cleared...")
        userList.clear()
    elif confirm_clear.upper() == "N":
        userPrompt()
    else:
         print("Invalid input...")
         clearList()
    
         

# This function is basically the entire program lol
# You can add items to the list and exit the program
# When the program is terminated the list will be printed to the console.
def userPrompt():
    print("Welcome to my first To-do list:")
    # this will put the program in an infinte loop 
    # I made it this way so that once the user enters something the prompt will keep coming back until the program is terminated.
    # btw this works because While loops are always TRUE unless explicity assigned a FALSE value, so by using "While True" the program is placed into a somewhat infinite loop.
    # This is the same for most other loops and in built functions i guess... i'm not sure, but it definitely works for while loop so yay!
    while True:
        print('Type "A" to add a new item to your list')
        print('Type "E" to terminate program')
        print('Type "L" to display the current list items')
        print('Type "D" to remove list items')
        print('Type "D -A" to remove all items from list')
        userResponse = input()
        # This IF Statement is where the program decides whether to accept input or terminate.
        if userResponse.upper() == "A":
            print("Enter an item to the list")
            item = str(input())
            # if the item variable is not empty (ie, the user entered a response) the following IF Statement will be executed.
            if item:
                userList.append(item)
                
        elif userResponse.upper() == "L":
            if userList:
                print("Current list itmes: ")
                print (userList)

                print("\nl")
                print("\nl")

            else:
                print("Nothing to show here...")
                print("Add an item to your list and try again😊")

                print("\nl")
                print("\nl")  

        elif userResponse.upper() == "D":
            print ("Which item would you like to remove? ")
            print (userList) 
            if userList:
                delOptions()
        elif userResponse.upper() == "D -A":
             clearList()
        # the program will terminate if "E" is entered as the response...
        elif userResponse.upper() == "E":
            termination()
            
userPrompt()