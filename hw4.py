def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found."
        except IndexError:
            return "Not found."
    return inner

@input_error
def parse_input(user_input):                     
    cmd, *args = user_input.split()              # Розділяє строку по пробілу на команду і аргументи
    cmd = cmd.strip().lower()                    # Видаляє зайві пробіли і приводить до нижнього реєстру
    return cmd, *args

@input_error
def add_contact(args, contacts):                 
    name, phone = args                           # Присвоєння значеннь
    contacts[name] = phone                       # Запис пари ключ:значення
    return "Contact added."

@input_error
def show_phone(args, contacts):                  
    name=args[0]                                 # Присвоєння значення за індексом
    if name in contacts:                         # Перевірка значень
        return contacts[name]
    return 'Not found'

@input_error
def show_all_contacts(contacts):                  
    if contacts:                                 
        for name, phone in contacts.items():     # Цикл виводу значень 
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def main():                                       
    contacts = {}                                # Створення порожнього словника
    print("Welcome to the assistant bot!")
    while True:                                  
        user_input = input("Enter a command: ")  # Ввід команди користувачем
        command, *args = parse_input(user_input) # Парсинг вводу і присвоєння значення

        if command in ["close", "exit"]:         # Перевірка вводу команди
            print("Good bye!")
            break
       
        elif command == "hello":                 # Перевірка вводу команди
            print("How can I help you?")
        
        elif command == "add":                   # Перевірка вводу команди
            print(add_contact(args, contacts))
        
        elif command == "phone":                 # Перевірка вводу команди
            print(show_phone(args, contacts))
        
        elif command == "all":                   # Перевірка вводу команди
            show_all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()