from collections import OrderedDict
place={
    'bangladesh':{'dhaka':'Sodor Road','barishal':["Cunia","Rupatoli","Bakergonj","Jalokati"],"ptuakali":[]},
    'USA':{"wasington":"White house","New York":"Avengers Tower","calophonea":None}
}

def gap(x):
    print("                 ")
    print("====", x, "======>>>>>Gap<<<<<=====", x, "====")
    print("                 ")
place["My area"]=['my house','Amir\'s house','Dipty\'s house']
gap("before pop() usa ")
print(place)


place.pop("USA")
gap("after pop usa")
print(place)

gap("before popitem()")

place.popitem()
gap("after popitem()")
print(place)


gap("new line")
names={
    "tanbir":{"Name":"Tanbir", "age":21,'class':"Honer's 1st year","address":"Bakergonj, Barishal" },
    "taohid":{"Name":"Taohid", "age":11,"class":"5","address":"Bakergonj, Barishal"}
    
}
def gets(tar):
    return names.get(tar)

def getkey(tar):
    return gets(tar).keys()
def getVal(target):
    return gets(target).values()


persons_key = [list(getkey("tanbir")),list(getkey("taohid"))]
persons_key_value = [list(getVal("tanbir")),list(getVal("taohid"))]


def append_name(name):
    persons_key.append(list(getkey(name)))
    persons_key_value.append(list(getVal(name)))



gap("key")
print(persons_key)
def info(target):
    print("Name     :", target.get("Name"))
    print("Age      :",target.get("age"))
    print("Class    :",target.get("class"))
    print("Address  :",target.get("address"))

gap("loopinfo")
def loopInfo():
    persons_key_length = len(persons_key)
    for x in range(persons_key_length):
        print("     ")
        print("new student")
        print("     ")
        keylength=len(persons_key[x])
        for newX in range(keylength):
            print(persons_key[x][newX], " : ", persons_key_value[x][newX])
         
        

loopInfo()
gap("loopinfo")
gap("loopinfo")
gap("loopinfo")
gap("loopinfo")

print(names.get("Tayeb"))

print(names.get("tanbir"))

gap("adding tayeb in the dictionary")

names["tayeb"]={"Name":"Tayeb","age":20,"class":"Honer's 2nd year","address":"Padri-Shippur, Bakergonj,Barishal "}
append_name("tayeb")


print(names.get("tayeb"))
gap("")
info(gets("tayeb"))
gap("")
print(persons_key)
gap("val")
print(persons_key_value)

loopInfo()


names["Sam"]={"code_name":"Falcon","class":"An Avenger"}


append_name("Sam")
loopInfo()


names["Taohid"]={"Name":"Taohid","Class":"5","Roll":"1","Age":11,"Address":"Mashespur"}
append_name("Taohid")
loopInfo()
for taohid in range(1000):
    n = "Taohid", taohid
    names[n]={"Name":"Taohid","Class":"5","Roll":"1","Age":11,"Address":"Mashespur"}
    append_name(n)
#loopInfo()
#print(names)


tanbir_value= (50,20,10,11,222,32,12,12,2,2,111,2,1,12,1,2,2,21)
sort_tanbir_value = sorted(list(tanbir_value))
print(tuple(sort_tanbir_value))
