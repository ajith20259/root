himalayan_Road= int(input('himalayan road:'))
local_Road=int (input('local road:'))
national_Road=int (input('national road:'))
avg= (himalayan_Road+local_Road+national_Road)/3
print(avg)
if avg>=60:
    print('eligible')
else:
    print('not eligible')