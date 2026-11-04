def add_tasks(lista_zadan):
    zadanie = input("Podaj treść zadania").strip().lower()

    if zadanie:
        lista_zadan.append(zadanie)
        print("Zadanie dodano")
    else:
        print("zadanie nie moze byc puste")