
def main():
    introduced = 0
    if introduced == 0:
        introduced = introduced + 1
        intro()
    elif introduced != 0:
        pass


def intro():
    print('Welcome to Movie Magic')
    print('\nMovie Magic is an interactive movie list')
    print('\nAfter a brief tutorial you will be able to add, manipulate and remove movies from this list')
    print("\nFirst, let's start by getting your name")
    while True:
        uservars.name = input()
        inputcheck = len(uservars.name)
        if inputcheck > 0:
            confirm = input('You wish to be called ' + uservars.name + '? Y/N')
            if confirm.lower() == 'y':
                    uservars.name = uservars.name
                    print('Alright, ' + uservars.name + ", Let's get started.")
                    break
            if confirm.lower() == 'n':
                print('Well then, what would you like to be called?')
            elif confirm.lower() != 'y' and confirm.lower() != 'n':
                confirm2 = input('Please confirm your input with [Y]es or [N]o')
                if confirm2.lower() == 'y':
                    uservars.name = uservars.name
                    print('Alright, ' + uservars.name + ", Let's get started.")
                    break
                else:
                    print('Well then, what would you like to be called?')
        elif inputcheck == 0:
            print('Please input your name.')
    print('Break Confirmation Placeholder')



def uservars():
    uservars.name = '-blank-'



main()