#1
flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my sheep sizes", flock)
# #2
big = max(flock)
print('Now my biggest sheep has size', big, "let's shear it")
#3
b = flock.index(big)
flock.pop(b)
flock.insert(b, 8)
print(flock)
# #4 + #5
list_grow = []
for grow in flock:
    grow = grow + 50 
    list_grow.append(grow)
print('One month has passed, now here is my flock', list_grow)
bigg = max(list_grow)
print('Now my biggest sheep has size', bigg, "let's shear it " )
bb = list_grow.index(bigg)
list_grow.pop(bb)
list_grow.insert(bb, 8)
print('After shearing, here is my flock', list_grow)
    
    