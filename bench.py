from subprocess import call
import time
import sys

if len(sys.argv) != 3:
    print "script requires a mongorestore binary and output filename"
    quit()

binary = sys.argv[1]
outfile_name = sys.argv[2]

outfile = open(outfile_name, 'w') #todo make this argv
outfile.write('collections, inserters, seconds\n')
repeat = 3

def median(l):
    # assumes length is odd!
    l.sort()
    return l[repeat/2]

def run(path, collections, inserters):
    start = time.time()
    print "%d collections with %d inserters each..." % (collections, inserters)
    val = call(
            "%s -v -d bench --drop --numInsertionWorkersPerCollection %d --numParallelCollections %d dump/mci" %
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

test(binary, 1, 1)
test(binary, 1, 2)
test(binary, 1, 4)
test(binary, 1, 8)
test(binary, 1, 16)
test(binary, 1, 32)
test(binary, 2, 1)
test(binary, 2, 2)
test(binary, 2, 4)
test(binary, 2, 8)
test(binary, 2, 16)
test(binary, 2, 32)
test(binary, 4, 1)
test(binary, 4, 2)
test(binary, 4, 4)
test(binary, 4, 8)
test(binary, 4, 16)
test(binary, 4, 32)
test(binary, 8, 1)
test(binary, 8, 2)
test(binary, 8, 4)
test(binary, 8, 8)


    
