#print function
def p(element):
    print(element)


#gap function
def gap(x):
    print(x, "==============||||||||GAP||||||||||=============", x)





our_numbers={'01843966266','01792396668','01715211930','01812860648','01712765906','01820533379',"01972860648"}
my_number={"01843966266","01792396668","5454545456"}
father_number={"01812860648","01715211930","23132153413"}
mother_number={"01712765906","01820533379","5464546851231"}
Friend_numbers={"01721351560","01790826762"}

our_use_number =my_number.intersection(our_numbers) , father_number.intersection(our_numbers)

my_family_members = [my_number, father_number, mother_number, Friend_numbers]

for our_num in my_family_members:
    items = our_numbers.intersection(our_num)
    if len(items)>0:
        print((len(items)), " item Found for", our_num, "set :")
        print(items)
    else:
        print("Data Did not match")
   
gap('loop Gap')
p(list(our_use_number))


