Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> n, m = input("Enter months to run, and how many months rabbits live, separated by a space ").split()
Enter months to run, and how many months rabbits live, separated by a space 88 20
>>> n, m = int(n), int(m)
>>> generations = [1, 1]
>>> def fib(i, j):
    count = 2
    while (count < i):
        if (count < j):
            generations.append(generations[-2] + generations[-1]) 
        elif (count == j or count == j+1):
            print ("in base cases for newborns (1st+2nd gen. deaths)") 
            generations.append((generations[-2] + generations[-1]) - 1)        else:
            generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)])) 
        count += 1
    return (generations[-1])
SyntaxError: invalid syntax
>>> def fib(i, j):
    count = 2
    while (count < i):
        if (count < j):
            generations.append(generations[-2] + generations[-1]) 
        elif (count == j or count == j+1):
            print ("in base cases for newborns (1st+2nd gen. deaths)") 
            generations.append((generations[-2] + generations[-1]) - 1)
        else:
            generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)])) 
        count += 1
    return (generations[-1])

>>> print(fib(n,m))
in base cases for newborns (1st+2nd gen. deaths)
in base cases for newborns (1st+2nd gen. deaths)
1097819219651235817
>>>