import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1
    

def recbinsearch(mylist, lower, upper, target) :
    mid = int((lower + upper) / 2)

    if lower > upper :
        return -1
    elif mylist[mid] == target :
        return mid
    elif mylist[mid] < target :
        return (recbinsearch(mylist, mid+1, upper, target))
    else : # mylist[mid] > target
        return (recbinsearch(mylist, lower, mid-1, target))


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers)-1, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d : not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d : not found %d time %.6f" % (numoftargets, cnt, ts))