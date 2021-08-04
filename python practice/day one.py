#turtle practice
import turtle;
turtleShapes=turtle.Turtle();

def activeShape():
   # turtleShape.speed(100);
    turtleShapes.forward(50)
    turtleShapes.write("First line")
    turtleShapes.width(5)
    turtleShapes.color("#0075ff")
    turtleShapes.circle(50)
    turtleShapes.write("second Line")
    turtleShapes.color("#ff6300")
    turtleShapes.left(45);
    turtleShapes.forward(75);
    turtleShapes.color("#00ffff")
    turtleShapes.write("third line")
    
    #turtleShapes.goto(25,120)

    

    turtleShapes.left(90)
    turtleShapes.forward(75)
    turtleShapes.color("#ffff00")
    turtleShapes.write("fifth line")
    
    turtleShapes.left(90)
    turtleShapes.forward(250)
    turtleShapes.color('#ff0080')
    turtleShapes.write("sixth line")

    
#activeShape();


#strings

MovieName="Iron Man, Captain America, Hulk, Thor, Avengers, AntMan, Doctor Strange";
#split
separateMovieName = MovieName.split(",")
print(separateMovieName)

#slice
sliceMovie= MovieName[0:20:2]
print(sliceMovie)

#format
myInformation="I am {0} and I am {2}years old. I was born in {1}"
withFormating= myInformation.format("Tanbir",1999,21)
print(withFormating)

#endswith()
print(MovieName.endswith("Strange"))


#geting Length
print(len(withFormating))

#count || count how many 'a' || in array or list how many things like [a,v,a,d,a,d,a] there are 4 a
print(myInformation.count("a"))

#INSERT
separateMovieName.insert(0, "0 this is the new 0 insert 0")
print(separateMovieName)

#append
separateMovieName.append("this a append value \"HULK 2003\"  ")
print(separateMovieName)

#sort()
numbers = [0, 56, 6, 4, 65, 56465, 465, 456, 465, 6545, 6545, 64, 654, 65, 46]

print("===========================")

print(numbers[2:4])

numbers.sort()
print(numbers)


#loop style
for xy in range(0,16,1):
    print(numbers[0:xy])


#for(let x=0;x<16;x=x+3){
 #   print(numbers[0:xy])
#}


#reverse
numbers.reverse()
print(numbers)








import calendar;

months = calendar.month(2020,4)
print(months)

monthIn_array=calendar.monthcalendar(2020,4)
print(monthIn_array)


def weekDay(year,month,day):

    weekDayOfTheDate = calendar.weekday(year, month, day)

    if weekDayOfTheDate==0:
        print("Monday")
    elif weekDayOfTheDate==1:
        print("Tuesday")
    elif weekDayOfTheDate==2:
        print("Wednesday")
    elif weekDayOfTheDate==3:
        print("Thursday")
    elif weekDayOfTheDate==4:
        print("Friday")
    elif weekDayOfTheDate==5:
        print("Saturday")
    elif weekDayOfTheDate==6:
        print("Sunday")
        

weekDay(2010,4,12)
weekDay(2021,2,21)
weekDay(2022,2,21)

print(calendar.isleap(2012))




