year=int(input('year: '))
if year%400==0 and year%100==0:
    print("%d is a leap year"%(year))
elif year%4==0 and year%100!=0:
    print("%d is a leap year"%(year))
else:
    print("%d is not a leap year" % (year))