# range vs xrange for generating ranges from 1-1000
def geese():
    goose=[]
    for i in range(1000):
        goose.append(i+1)
    for i in range(1000):
        goose.remove(i+1)

def light():
    lights=[]
    for i in xrange(1000):
        lights.append(i+1)
    for i in xrange(1000):
        lights.remove(i+1)

# Using a List as a Queue vs using collections.deque (insert and remove 1000 items)
def rainbow():
    rainbows = []
    for x in range(1000):
        rainbows.append(x+1)
    for x in range(1000):
        rainbows.remove(x+1)

def unicorn():
    from collections import deque
    unicorns=deque('1')
    for x in range(1,1000):
        unicorns.append(x+1)
    unicorns.clear()

if __name__ == '__main__':
    import timeit
    print('range')
    print(timeit.timeit("geese()", setup="from __main__ import geese"))
    print ('xrange'')
    print(timeit.timeit("light()", setup="from __main__ import light"))
    print('list as a queue')
    print(timeit.timeit("rainbow()", setup="from __main__ import rainbow"))
    print('collections')
    print(timeit.timeit("unicorn()", setup="from __main__ import unicorn"))
