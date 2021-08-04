e=10
def res():
    global e
    
    while e<=100:
             e += 1
             print(res(), "by")
            
    return "hello"


print(res())
res()
