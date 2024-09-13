#Python Code to see what is the highest common factor for any given two numbers
#HCF is the highest number that can divide both of the given numbers
#Example: For 30 and 20 the highest common factor would be 10 (which divides both 20 and 30 i.e its a common factor)

number1 = int(input("Enter the number: "))
number2 = int(input("Enter another number: "))

if number1 > number2:
  smaller = number2
else:
  smaller = number1

i=0
while(i <= smaller):
  if (number1 % i == 0 and number2 % i == 0):
    hcf= i
  i+=1 

print("HCF of %d and %d is: %d" %(number1, number2, hcf))

#Exercise: You can try this with three given numbers