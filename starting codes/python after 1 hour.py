newString="hello Tanbir";
print(type(newString));
newstring_value= newString[5:]
print(newstring_value);
print(newstring_value.upper());
print(newstring_value.lower());


print(newstring_value.replace("Tanbir", "Taohid"))

print(newstring_value);

#replace string

whatTosay=newString.replace("hello","how are you");
print(whatTosay)



# loop for array or list
def loop(listItem):
    print("Primary stage :",listItem)
    print("loop through every pice :")
    itemNumnber=0;
    for items in listItem:
        itemNumnber+=1
        print(itemNumnber," : ",items);



#splits

splitSay=whatTosay.split(" ")
print(splitSay);
loop(splitSay);

splitSentence="hi whats up ! how you are doing ? I am coming Buddy. Are you ready ?";
splitWord2 = splitSentence.split("?")

print(splitWord2[1])
loop(splitWord2)

