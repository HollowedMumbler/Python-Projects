#Todo list?
import time
class Todolist:
    def __init__(self):
        self.tasks = []
    

            
    def add_task(self):
        add_ = input("What would you like to add? ")
        while True:    
            self.tasks.append(add_)
            print(f"{add_} has now been added.")
            ask_again = input("Enter another todo or Press [Q] to quit ")
            add_ = ask_again
            if ask_again.upper() == "Q":
                print("Ok, now ending")
                break
            else:
                print(f"Added {add_}")
    def delete(self):
        
        while True:
            try:
                remove_ = input("What would you like to remove? [Enter none if finished] ")
                
                self.tasks.remove(remove_)
                print(f"{remove_} has been removed.")
            except ValueError:
                if remove_.upper() == "NONE":
                    break
                else:
                    pass                
                print(f"{remove_} does not exist. Maybe you put in a typo?")

    def view_task(self):
        while True:
            print("The tasks that you have added are: \n")
            for i in self.tasks:
                print(i)
                
            time.sleep(2)
            confirm = input("All good now? [Press enter for yes]").upper()
            if confirm == "NO":
                print(f"Ok, one more time")
            else:
                break
   
            
    
todo1 = Todolist()
def main_func():
    while True:
        whatdo = input("What would you like to do? ADD/DEL/VIEW/QUIT: ").upper()
        if whatdo == "ADD": 
            todo1.add_task()
        elif whatdo == "DEL":
            todo1.delete()
        elif whatdo == "VIEW":
            todo1.view_task()
        elif whatdo == "QUIT":
            exit()

main_func()