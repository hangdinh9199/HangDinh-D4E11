n = int(input())
factrofn = 1
if n == 0 or n ==1:
    print(factrofn) 
else:
    for i in range(2, n+1):
        factrofn = factrofn * i
    print(int(factrofn)) 