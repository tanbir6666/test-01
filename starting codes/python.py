a=25;
c=11.25;
f=False;
st="hello "
print(type(st))


def p(content):
	 print(content)

def mypythonOne():
			age= input("How old are you ?");

			ageNumber=int(age);
			born_year= 2021-ageNumber;

			print(born_year);


			if born_year>1999:
				print("welcome to the new age");
			else:
				print("You are form 90s.. !")	

			name="tanbir how are you ?"

			p(name[0:3]);
			p(name[-1:-2]);
			word = 'abcdefghijklmnopqrstuvwxyz';
			length=len(word);
			p(length);
			neWword= word[0:length:3] 
			p(neWword)

			p(name.endswith("bir"));

			capitalizeName=name.capitalize();
			p(capitalizeName);


			index_of_how=name.find("how");
			p(index_of_how);
			p(name[index_of_how:]);

			p(name.count("o"));
			#input("What is your Name ?");


			#p("Dear "+ input("What is your Name ?"));
			#p("your are selected");




			import turtle
			tanbir_turtle=turtle.Turtle();

			def Square(position):
				

				tanbir_turtle.forward(100+position);
				tanbir_turtle.right(90);
				tanbir_turtle.forward(100+position);
				tanbir_turtle.right(90);
				tanbir_turtle.forward(100+position);

				tanbir_turtle.right(90);
				tanbir_turtle.forward(100+position);





			def newsquare():
				Square(0)
				tanbir_turtle.forward(40);
				tanbir_turtle.right(45);
				tanbir_turtle.forward(120);
				Square(0)




import calendar;

print(calendar.weekheader(3))
# 3 define the length of days like 'Mon' 3 is the length

print(calendar.firstweekday())


print(calendar.month(2021,2))


cl = calendar.monthcalendar(2021, 2);
print(cl)


print(calendar.calendar(2021))

#for clr in cl:
#	print(clr)
for allmonth in range(1,13):
	eachMonth= calendar.monthcalendar(2021, allmonth)
	print(calendar.month(2021, allmonth));
	for mont in eachMonth:
		
		print(mont)



def getWeekDay(year,month,date):

		week_day_on_date = calendar.weekday(year, month, date)

		if week_day_on_date==0:
			print("Monday")
		elif week_day_on_date==1:
			print("Tuesday")
		elif week_day_on_date == 2:
			print("wednesday")
		elif week_day_on_date == 3:
			print("Thursday")
		elif week_day_on_date == 4:
			print("Friday")
		elif week_day_on_date == 5:
			print("Saturday")
		elif week_day_on_date == 6:
			print("Sunday")
		else:
			print("sorry nothing found")	
			
		#print(week_day_on_date)
getWeekDay(1999,11,14);
getWeekDay(2010, 4, 12);

getWeekDay(2021, 2, 20);


#leapYearOrNot=calendar.isleap(2021);
#print(leapYearOrNot);
def leapYear_(year):
	leapYear = calendar.isleap(year)
	if leapYear==True:
		print(year, "is a Leap Year")
	else:
		print(year, "is Not a Leap Year, Sorry About that")	


leapYear_(2020)

def leapDays_(range0,range1):
	print(calendar.leapdays(range0, range1));



leapDays_(1999,2021);