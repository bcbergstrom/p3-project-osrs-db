import ORM as ORM
def UI():
    print("Welcome to the MMORPG Profit Calculator")
    print("Type 'help' for a list of commands")
    while True:
        command = input(">>> ")
        if command == "help":
            print("add_user: Add a user to the database")
            print("add_method: Add a method to the database")
            print("get_user: Get a random user from the database")
            print("get_method: Get a random method from the database")
            print("get_method_by_user: Get all methods associated with a user")
            print("get_random_method_by_user: Get a random method associated with a user")
            print("edit_user: Edit a user in the database")
            print("edit_method: Edit a method in the database")
            print("exit: Exit the program")
        if command == "add_user":
            name = input("Name: ")
            reqsid = input("Requirements ID: ")
            main_doc.add_user(name, reqsid)
        if command == "add_method":
            method = input("Method: ")
            profit = input("Profit: ")
            time = input("Time: ")
            reqsid = input("Requirements ID: ")
            main_doc.add_method(method, profit, time, reqsid)   
        if command == "get_user":
            name = input("Name: ")
            print(main_doc.get_user(name))
        if command == "get_method":
            id = input("ID: ")
            print(main_doc.get_method(id))
        if command == "get_method_by_user":
            name = input("Name: ")
            print(main_doc.get_method_by_user(name))
        if command == "get_random_method_by_user":
            name = input("Name: ")
            print(main_doc.get_method_by_user(name))
        if command == "edit_user":
            id = input("ID: ")
            name = input("Name: ")
            reqsid = input("Requirements ID: ")
            main_doc.edit_user(id, name, reqsid)
        if command == "edit_method":
            id = input("ID: ")
            method = input("Method: ")
            profit = input("Profit: ")
            time = input("Time: ")
            reqsid = input("Requirements ID: ")
            main_doc.edit_method(id, method, profit, time, reqsid)
        if command == "exit":
            break
    
if __name__ == "__main__":
    main_doc = ORM.ORM("test.db")
    UI()