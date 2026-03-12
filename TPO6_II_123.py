"""#exercice 1
def calcul_de_moyenne(): 
    note_matiere_a = float(input(" Veuillez-rentrez votre note : "))
    note_matiere_b = float(input("Veuillez-rentrez  votre note : "))
    note_matiere_c = float(input("Veuillez-rentrez  votre note : "))
    note_matiere_d = float(input("Veuillez-rentrez  votre note : "))
    moyenne = round((note_matiere_a + note_matiere_b + note_matiere_c + note_matiere_d) / 4, 1)
    print(moyenne)

    if moyenne < 10 :
        print("Ajourné")
    elif moyenne <= 12 : 
        print ( "Passable" )
    elif moyenne <= 14 :
        print("Assez biens ")
    elif moyenne <=16 :
        print ("Biens ! ")
    else : 
        print("Très biens ! ")
calcul_de_moyenne()
"""
#exercice
