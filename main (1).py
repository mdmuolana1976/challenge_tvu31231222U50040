# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
     return True
  else:
     return False

year= 2014

if isLeapYear(year):
  print ('{} is a Leap year.'.format(year))
else:
  print ('{} is a not Leap year.'.format(year))