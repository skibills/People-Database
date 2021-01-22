
def start():
    from names_list import people_database
    loopRun = True

    
    while loopRun == True:
        Name = input('Please enter a name: ').lower()
        print('You typed in the name ' + Name.capitalize())
        try:
            Persons_data = people_database[Name]
            print('Name: ' + Name.capitalize())
            print('Sex: ' + Persons_data[0])
            print('Weight: ' + Persons_data[1])

        except:
            print('That name was not found in the database.')

        isNotValid = True       #primes loop - line 19
        while isNotValid == True:
            userInput = input('Would you like to search for another name? ').capitalize()
            
            if userInput == 'Yes':
                #loopRun = True
                isNotValid = False

            elif userInput == 'No':
                loopRun = False
                isNotValid = False

            else:
                print('Please enter Yes or No.')
                isNotValid = True

               
    print("No, Goodbye!")
start()
