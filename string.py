stringa = input("Inserisci una stringa: ")

if(len(stringa) < 2):
    print("")
    exit(1)

res = stringa[:2] + stringa[-2:]
print(res)
