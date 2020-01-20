Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 4586
>>> b = 9410
>>> c = 0
>>> for number in range (a,b+1):
	if (number % 2 != 0):
		c = c + number

		
>>> print ("{2}".format (a,b,c))
16879176
>>>