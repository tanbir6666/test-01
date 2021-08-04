def p(prints):
    print(prints)



#slice test
#what_to_slice[slice[start (default is 0),end,gapBeetween (optional) (default is 1)]]
p(nameLists[slice(0, 6, 2)])


#strings======================90deg right

#ignore it
bx = '  he l  lo        world  '
p(bx[-5:-2])

p(bx)


# using strip . strip() remove whiteSpace form a line (begining or end)
p(bx.strip())

#format() .   this used to combine 2 types of data in one by making them all string or number
this_is_a_string = "I am A string and this is a Number {}"
# {} this is a Target for Format() Function
this_is_a_number = 531
#we can not add these together, So:
#All Number can Turn into string. But all string can not turn into Numbers So
newFormet = this_is_a_string.format(this_is_a_number)
print(newFormet)

#let's think bigger

age = 21
weight = 88
height = 69

all_in_one = "I am Tanbir and I am {0} years old. I am {2}inch tall and My weight is {1}kg"
#{2} the number 2 define the order inside the formet function.this case 2 means 3rd. 0 means 1. default {0},{1},{2} and so on.

After_add_values = all_in_one.format(age, weight, height)


p(After_add_values)

#escape values \' ,\\=add one Backslash, \n=new line, \r, \t=tab, \b=backspace(remove space before it), \f=form feed, \ooo=Octal value, \xhh=hex value
#lets add "" in side ""
Favorite_series = "My favorite \t series   is \n  \"Game Of Thrones\" "
p(Favorite_series)
encode = Favorite_series.encode()
p(encode)
p(Favorite_series.endswith("\"Game Of Thrones\" "))
p(Favorite_series.translate("My"))
p(Favorite_series.zfill(50))
