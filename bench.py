from subprocess import call
import time


outfile = open('outfile', 'w')
outfile.write('collections, inserters, seconds\n')
repeat = 5

def median(l):
    # assumes length is odd!
    print l
    l.sort()
    print l
    return l[repeat/2 + 1]

def run(path, collections, inserters):
    start = time.time()
    print "%d collections with %d inserters each..." % (collections, inserters)
    val = call(
            "%s -v -c users -d bench --drop --numInsertionWorkersPerCollection %d --numParallelCollections %d dump/mci/versions.bson" %
            (path, inserters, collections), shell=True)
    end = time.time()
    return end - start

def test(binary, collections, inserters):
    res = []
    for i in range(repeat):
        print "TEST %d for %d x %d" % (i, collections, inserters)
        res.append(run(binary, collections, inserters))
    med = median(res)
    print "Median time = %f secs" % med
    outfile.write('%d, %d, %f\n' % (collections, inserters, med))

binary = "mongorestore"
test(binary, 4, 1)
test(binary, 4, 2)
test(binary, 4, 4)
test(binary, 4, 8)
test(binary, 4, 16)
test(binary, 4, 32)

    
