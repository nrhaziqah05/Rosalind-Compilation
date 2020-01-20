import itertools

n = 6

perms = list(itertools.permutations([i for i in range(1,n+1)]))

print(len(perms))
 
for perm in perms:
    print(str(perm)[1:].replace(')','').replace(',',''))