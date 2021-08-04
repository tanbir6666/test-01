mutability_full_form=["mutate Ability"]

mutable="Changeable"
immutability="Unchangeable"

# list Data's are Mutable & also dictionary,Order Dictionary,and so many........



# Tuple Data's are immutability & int, Floats, booleans, strings
# in dictionary Key's are immutable but Values are not
# immutability data's are Much secure than the mutable data types


#let's write a tuple and in there make a list

Unchangeable_data=(1,2,3,[4,5,6])
#Unchangeable_data[3] is an error . because it's an item of tuple . so we need to target inside that list. 
# in that case we need to add a new parameater like this Unchangeable_data[tuple_index][list_index] to change it
#So (1,2,3,[4,5,6]) hole thing is immutable but [4,5,6]-this small located area of it is muteable
#it means Location is unchangeable but the value inside of that location is changeable

Unchangeable_data[3][0]="hello"

print(Unchangeable_data)

#so it worked !!!!!!


