# string manupulation
def loop(listItem):
    print("Primary stage :", listItem)
    print("loop through every pice :")
    itemNumnber = 0
    for items in listItem:
        itemNumnber += 1
        print(itemNumnber, " : ", items.strip())


def rangeLoop(first, last):

    for x in range(first, last):
        print(x)


def p(prints):
    print(prints)


def gap():
    p("--------------")
    p("|||||||||||||||")
    p("GAP")
    p("--------------")




#join strings arrays

marval_Movies="Iron Man, Thor, Captain America, Hulk, Avengers"
marval_Movies_array= marval_Movies.split(",")

p(marval_Movies_array)
loop(marval_Movies_array)
Marval_Movies_all_together = "\n and \n".join(marval_Movies_array)
p(Marval_Movies_all_together)


