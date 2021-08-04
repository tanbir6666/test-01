#sets---
#specialty: can not write same item more than 1 time . this will ignore duplicate


#print function
def p(element):
    print(element)


#gap function
def gap(x):
    print(x, "==============||||||||GAP||||||||||=============",x)
   

#tuple work


name = {"tanbir", "taohid", "tayeb", "tanbir", "tanbir", "taohid"}

p(name)

gap(1)
name.add("Hiru");
#there are no append() or insert() function in sets
#this arrange by alfabate order 



p(name)


#add() function  will ignored if the element is already exist in the sets

name.add("Tanbir")
# this is not case Sensitive


#if we have a list with duplicate types of list items

nameInLists = ["tanbir", "taohid", "tayeb", "tanbir", "tanbir", "taohid"]

gap(2)
p(nameInLists)

#after add sets
setOF_names = set(nameInLists);
#setOF_names is a set now with set() function
p(setOF_names)

#list again make it list
listOf_set = list(setOF_names);
p(listOf_set)

#tuple_of_list
tuple_of_list = tuple(listOf_set)
p(tuple_of_list)


gap(3)

#union-----------------


movie_list_one={"Avengers","iron Man","Captain America","Thor","Hulk","Avengers Age of ultron"}
movie_list_two_favorite={"Avengers","Iron man","Avengers Age of ultron","Avengers Endgame"}
#lets union these together

uni=movie_list_one.union(movie_list_two_favorite)

#now uni has "movie_list_one" & "movie_list_two_favorite" both but not add same thing more than one time

p(uni)

uni_set_list = list(movie_list_two_favorite)
p(uni_set_list)


gap(4)


#intersection--- opposite of union
intersetion_of_movie_lists = movie_list_one.intersection(movie_list_two_favorite)
#intersection will only sent those values which are in both sets. common calculation
p(intersetion_of_movie_lists)


gap(5)


#difference. this will get difference beetween two sets

difference=movie_list_one.difference(movie_list_two_favorite);
#this  represent this item which are not common in sets
p(difference)


gap(6)


#clean -- this will clean the sets

difference.clear()
p(difference)

