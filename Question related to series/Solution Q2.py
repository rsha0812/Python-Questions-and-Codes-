#Q2  : Given a number "N" print the sum of each digit to the power of number of digits in given input.
# Example :
# Input => 1234
# => (1**4)+(2**4)+(3**4)+(4**4)
# => 1+16+81+256
# Output => 354

# Solution2:

n = int(input("Enter the number: "))
sum = 0 
i = len(str(n))
while(n):
	a = n%10
	sum = sum+(a**i)
	n = n//10
print(sum)


a -32
a+ 32