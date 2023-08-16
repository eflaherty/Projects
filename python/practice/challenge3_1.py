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

if __name__ == '__main__':
    import timeit
    print 'range'
    print(timeit.timeit("geese()", setup="from __main__ import geese"))
    print 'xrange'
    print(timeit.timeit("light()", setup="from __main__ import light"))
