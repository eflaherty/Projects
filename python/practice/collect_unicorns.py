from collections import deque
unicorns=deque('1')
for x in range(1,1000):
    unicorns.append(x+1)

print ('append unicorns')
print (unicorns)

unicorns.clear()

print ('clear unicorns')
print(unicorns)
