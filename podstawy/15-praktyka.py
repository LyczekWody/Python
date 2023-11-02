user_choice = -1

tasks = []


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1 

def add_tasks():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")

def delete_task():
    task_index = int(input("Zadania do usuniecia: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indeksie nie istnieje!")
        return
    tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_tasks_to_file():
    file = open("tasks.txt", "w", encoding="utf-8")

    for task in tasks:
        file.write(task +"\n")
    file.close()

def load_task_from_file():
    try:
        file = open ("tasks.txt")
        for line in file.readline():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return


load_task_from_file()

while user_choice !=5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_tasks()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file()

    print()   
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany w pliku")
    print("5. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()

    