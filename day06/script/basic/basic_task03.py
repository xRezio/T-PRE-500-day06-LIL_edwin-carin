def bread (x) :
    if x ==1 :
     print (" <////////// > ")
    return x
def lettuce (y) :
    if y ==2:
        print (" ~~~~~~~~~~~~ ")
    return y
def tomato (z) :
    if z == 3:
       print (" O O O O O O ")
    return z
def ham (a) :
    if a ==4:
        print (" ============ ")
    return a

n = int(input("Combien de burger ?"))
if n <= 0:
        print(" I can't do this !")

else :
        for i in range (n):
            bread(1)
            tomato(3)
            ham(4)
            ham(4)
            lettuce(2)
            bread(1)
            print(i)