"""Abstract class representing the decision loop part of a game"""
class ConsoleDecisionLoop:

    """Creates object by initializing menu, calls the create menu function"""
    def __init__(self):
        #reads in menu and initializes it 
        self.menu={}
        self.create_menu()

    """Method to get user input for commands."""
    def loop_over_decision_menu(self):
        self.help_command()
        user_option_str : str = input("Enter a command. 0 For help.")
        while(user_option_str!="-1"):
            if user_option_str in self.menu:
                #call function 
                self.menu[user_option_str]()
            elif user_option_str!= "-1" and user_option_str not in self.menu:
                print(f"ERROR. Command not recognized:{user_option_str}")
            user_option_str : str = input("Enter a command. 0 For help.")

    """Help command to display options to the user."""
    def help_command(self):
        pass

    """This value is overriden in child classes such that each function can have its own"""
    def create_menu(self):
        pass 