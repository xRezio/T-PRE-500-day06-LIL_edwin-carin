def recursion(mot):
    mot_reverse = mot[::-1]
    if mot_reverse == mot:
      print("palyndrome")
    else :
      print("pas palyndrome")

mot = input("entrez votre phrase : ")
recursion(mot)