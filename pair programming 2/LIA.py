Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

	
>>> k=5
>>> n=7
>>> m=2**k
>>> i=2**k
>>> p=0
>>> while i>=n:
	p=p+(factorial(m)/(factorial(i)*factorial((m-i))))*(0.25**i)*(0.75**(m-i))
	i -=1

	
>>> print(round(p,3))
0.722
>>>