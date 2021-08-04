#dictionary

age={"Tanbir":21,"Taohid":11,"Hiru":58,"Shmu":42}
print(age["Taohid"])

def gap(x):
    print("")
    print(x,"==========GAP========",x)
    print("")
#if age["Taohid"]---> Taohid does not exist this will give an error

# print(age["Tayeb"])--> this will be an error

#so for this problem we have get() function

print(age.get("Shmu"))
#this is Case sensitive So be careful

print(age.get("Tayeb"))
# this will say None . No error for Not Founding "tayeb"
# so w use get()
gap("contact dictionary")
contacts={
    "Tanbir": {"number": "01843966266","address":"Bakergonj"},
    "Shmu": {"number": "01820533379", "address": "Vorpasa"}
}
print(contacts.get("Tanbir").get("number"))

#dict.items()
gap("dict.items()")
print(contacts.items())
gap("dict.items()")


#dict.keys()
gap("dict.keys()")
print(contacts.keys())

gap("dict.keys()")


#dict.values
gap("values")
print(contacts.values())
gap("values")

#pop("what to remove")
gap("pop()")


print(contacts.pop("Shmu"))


gap("pop()")


print(contacts)

#pop or remove items randomly
contacts2={
    "Tanbir": {"number": "01843966266","address":"Bakergonj"},
    "Shmu": {"number": "01820533379", "address": "Vorpasa"},
    "Hiru": {"number": "01820533379", "address": "Vorpasa"},
    "Taohid": {"number": "01820533379", "address": "Vorpasa"},
    "Tayeb": {"number": "01820533379", "address": "Vorpasa"},
}
gap("popItems()")
print(contacts2)
contacts2.popitem()
contacts2.popitem()
contacts2.popitem()
gap("popItems()")
print(contacts2)
gap("popItems()")


#add to dict

contacts3 = {
    "Tanbir": {"number": "01843966266", "address": "Bakergonj"},
    "Shmu": {"number": "01820533379", "address": "Vorpasa"},
    "Hiru": {"number": "01820533379", "address": "Vorpasa"},
    "Taohid": {"number": "01820533379", "address": "Vorpasa"},
    "Tayeb": {"number": "01820533379", "address": "Vorpasa"},
}
gap("Contact 3")
#add to dict
contacts3["hello"]="How Are you?"
#add to dict
print(contacts3)
 
A_Sentence="hello, I am Tanbir and you ?"
listSentence=A_Sentence.split(" ")

print(listSentence)

for l in listSentence:
    print(l,"=",len(l))
    contacts3[l]=len(l)

print(contacts3)


#Dictionary is not a orderAble data

#so for do that we are going to import somthing




from collections import OrderedDict


