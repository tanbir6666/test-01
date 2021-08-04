names=["tanbir","taohid","tayeb","Robin","Amir"]

empty_list=[]
def loop(loopItem):
    for x in loopItem:
        print(x)
for person in names:
    empty_list.append(person)

print(empty_list)
empty_list.clear()
print(empty_list)
print([person for person in names])

empty_list.clear()

for person in names:
    print(person," The people That I know")
    empty_list.append(person + " The people That I know")

print(empty_list)

loop(empty_list)
empty_list.clear()
#let's to this in one line ||| always need the 3rd Brackets []

print([person+" Know people" for person in names])
loop([person+" Know people" for person in names])



#Fun time
#let's loop threw Dictionary

Movie_rateing={"Iron Man":7.5,"Hulk":5.8,"Thor":7.2,"Captain America":8.2}

Movie_rateing["The Avengers"]=8.7

popular_movie=[]
un_popular_movie=[]
for rate in Movie_rateing:
    if Movie_rateing[rate]>=7.5:
        popular_movie.append(rate)
    elif Movie_rateing[rate]<7.5: 
        un_popular_movie.append(rate)
    else:
        print("Somthing is wrong")


print("popular_movie : ", popular_movie)
print("un_popular_movie : ", un_popular_movie)

#lets do this in one line.
popular_movie.clear()

un_popular_movie.clear()


print([movie for movie in Movie_rateing if Movie_rateing[movie] >= 7.5])
