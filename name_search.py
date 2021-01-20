
def start():
    from names_list import people_database

    Name = input('Please enter a name: ').lower()
    print('You typed in the name ' + Name.capitalize())
    try:
        Persons_data = people_database[Name]
        print('Name: ' + Name.capitalize())
        print('Sex: ' + Persons_data[0])
        print('Weight: ' + Persons_data[1])
        more()
    except:
        print('That name was not found in the database.')
        more()
def more():
    More = input('Would you like to search for another name? ')
    if More == 'Yes':
        start()
    if More == 'No':
        print('Goodbye!')
        quit()
    else:
        print('Please enter Yes or No.')
        more()
start()

