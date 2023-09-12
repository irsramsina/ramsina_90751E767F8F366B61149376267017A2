def CheckLeapYear(year):
    import calendar 
    return(calendar.isleap(year))
year=int(input("Enter the year:"))
if(CheckLeapYear(year)):
  print("Leap Year")
else:
   print("Not a Leap Year")