#zip function will marge 2 list items

Names=["Tanbir","Taohid","Shmu","Hiru","Tayeb"]
Ages=[21,11,42,58]
height=["5f9inc","4f5inc","5ft3inc","5ft5inc","5ft10inc"]

#here height has the shortest amount . here 2 & and zip index will reach max 2 Rows
# that means in all zip inside items , whoever has the sortest amount of data will be equal to the zip row value 

zip_function=list(zip(Names,Ages,height))
print(zip_function)
for zi in zip_function:
   
    print("name : ",zi[0]," & ","Age : ",zi[1]," & Height :",zi[2])


unzipped_function=list(zip(*zip_function))

print(unzipped_function)

for unzipped_tuple in unzipped_function:
        print(list(unzipped_tuple))




list_one=[1,2,3,4,5,6,7,8,9,10,11]
list_two=["one","Two","Three","Four","Five","six","Seven","Eight"]

for l1, l2 in zip(list_one, list_two):
    print(l1)
    print(l2)

# zip is used to marge 2 or more datas and loop threw Together
on_line_loop = [[l1,l2] for l1, l2 in zip(list_one, list_two)]

print(on_line_loop)


items=["Mothboard","RAM","Hard Drive","Power Supply"]
prices=[4000,2000,4000,2600]
amounts=[10,12,13,25]

Sentences=[]
for (item,price,amount) in zip(items,prices,amounts):
    Sentences.append((item+"\'s Price are "+str(price*amount)+" taka & "+str(price)+" taka per pice"))


for sen in Sentences:
    print(sen)


import pandas

datas=pandas.DataFrame({
    "Product Name": items,
    "Product Price": prices,
    "Product Amount": amounts,
})
print(datas.loc[0:])
datas.to_csv("Product info.csv")


my_Serise=pandas.Series(data=items,index=["one","Two","three","four"])
print(my_Serise)


print(pandas.read_csv("product info.csv"))








