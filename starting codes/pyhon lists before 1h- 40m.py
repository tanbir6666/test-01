# loop for array or list
def loop(listItem):
    print("Primary stage :",listItem)
    print("loop through every pice :")
    itemNumnber=0;
    for items in listItem:
        itemNumnber+=1
        print(itemNumnber," : ",items)
def rangeLoop(first,last):
    
    for x in range(first, last):
        print(x)

def p(prints):
    print(prints)

def gap():
    p("--------------")
    p("|||||||||||||||")
    p("GAP")
    p("--------------")


listOne = [1, 2, 3, 4, 5, 6, 8]
p(listOne)
listTwo=["hello","213",True,False,["he","is"],listOne]
#p(listTwo)
loop(listTwo)

p(listTwo[-1])


#append in lists
listTwo.append("I am an append Line");
# this will work like push in javascript
listTwo.insert(0,"I am an Insert at 0 line")
p(listTwo)


#insert(position,insert_able_Element)
listTwo.insert(0,"I am an Prepend Line and Now I am at position 0");

p(listTwo)


# where_toRemove.remove(what_to_remove)
nameLists=["Tanbir","Taohid","Tayeb","Robin","Amir"];
nameLists.remove("Amir");
p(nameLists)

#test
nameLists.append("New Amir");
p(nameLists)

nameLists.insert(4,"Moshiur")
p(nameLists)

newAmirSplit= nameLists[5].split(" ");
p(newAmirSplit)

#reverse a list
listOne.reverse()
p(listOne)

#sort()
listOf_random_number=[10,25,2,42,15,55,5,5,24,5,51,54,5,1,1242,145,7,5,]
listOf_random_number.sort()
p(listOf_random_number)


#reverse_sort
listOf_random_number.reverse();
p(listOf_random_number)


p(listOf_random_number[-len(listOf_random_number):5])



#list slice

number_list=[]

for x in range(301):
    number_list.append(x)
gap();
p(number_list)
gap()



#first:second:third 
#first = where to start (default is 0)
#second=where to end (no default)
#third=how much gap between each part (default is 1) 

p(number_list[:50:5])

# a negative index in third will reverse the process
# that time, after crossing 0:50 count will start for -5
# 55-300 in reverse so [300,299,.......55]
gap()

view=12;
for l in range(len(number_list)-(view-1)):
    p(number_list[l:l+view])




arraycode=['my' , 'name' , 'taohid']
print(arraycode[0:2])

def minute(hour):
    print(hour,"hour : ", hour*60," minutes")


minute(24)  

