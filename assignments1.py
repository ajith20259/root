#1. Print User's Name
name = input('Enter User Name:')
print('Hello,',name,'!')


#2. Add Two Numbers
a = int(input('Enter first number for addition:'))
b = int(input('Enter second number for addition:'))
print('Addition of',a,'and',b,'is',a+b)


#3. Square of a Number
num = int(input('Enter a number:'))
print('Square of',num,'is',num*num)


#4. Check Even or Odd
num = int(input('Enter a number:'))
if (num%2)==0:
  print(num,'is an even number')
else:
   print(num,'is an odd number')



#5. Compare Two Numbers
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
if (a==b):
   print('First Number is equal to second number')
elif (a>b):
   print('First number is greater than second number')
else:
   print('First number is less than second number')


#6. Simple Calculator
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
operator = input('Enter operator:')
if operator=='+':
   print('Addition of',num1,'&',num2,'is',(num1+num2))
elif operator=='-':
   print('Substraction of',num1,'&',num2,'is',(num1-num2))
elif operator=='*':
   print('Multiplication of',num1,'&',num2,'is',(num1*num2))
elif operator=='/':
   print('Division of',num1,'&',num2,'is',(num1/num2))
else:
   print('Invalid operator, enter correct operator +,-,*,/')


#7. Find Remainder and Quotient
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
print('Quotient is:',(num1/num2))
print('Remainder is:',(num1%num2))


#8. Logical Operation Check
a = input('First Boolean Value:')
b = input('Second Boolean Value:')
if a and b == 'true':
    print('Both a & b are True')
if a or b =='true':
    print('Either a or b is True')
print(not b)



#9. Membership Check in a String
str = input('Enter the string:')
char = input('Enter the character to check:')
for x in range(len(str)):
    if str[x] == char:
        print('Char',char,'found at index',x)
    else:
        print('Char',char,'not found at index',x)

#10. Sum of Digits
num = int(input('Enter a multi digit number:'))
sum = 0
for x in str(num):
    sum = sum+int(x)
print('Sum of multi digit',num,'is',sum)

