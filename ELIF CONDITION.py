name=input('enter name')
per=int (input('enter percentage'))
if per<35:
    print (name,'fail')
elif per>= 35 and per<50:
    print (name,'C grade')
elif per>= 50 and per<90:
    print (name,' B grade')
elif per>= 90 and per<=100:
    print(name,'A grade')
else:
    print('invalid marks')