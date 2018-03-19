todo_list = []

while 1:
    choice = int(input("Cosa vuoi fare?\n"
                   "1)Aggiungi una cosa da fare\n"
                   "2)Rimuovi una cosa da fare\n"
                   "3)Vedi le cose da fare\n"
                   "4)Chiudi il programma\n"))

    if(choice < 0 or choice > 4):
        print("Errore.")
        pass;

    if (choice == 1):
        new = input("Cosa vuoi aggiungere: ");
        todo_list.append(new)
    elif (choice == 2):
        to_delete = input("Inserisci la cosa da cancellare: ")
        if(to_delete in todo_list):
            todo_list.remove(to_delete)
        else:
            print("Non esiste questa cosa che vuoi fare!")
    elif (choice == 3):
        for cosa in todo_list:
            print(cosa)
    elif (choice == 4):
        exit(1)