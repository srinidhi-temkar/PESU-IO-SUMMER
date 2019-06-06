n=int(input("Enter a number : "))
def digitsum(n):
	if(n==0):
		return 0
	else:
		return n%10+digitsum(n//10)    
print("sum of digits of",n,"is",digitsum(n))











