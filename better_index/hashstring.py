#Define a function, hash_string,
#that takes as inputs a keyword
#(string) and a number of buckets,
#and outputs a number representing
#the bucket for that keyword.

#print hash_string('a',12) => 1
#print hash_string('b',12) => 2
#print hash_string('a',13) => 6

#print hash_string('au',12) => 10
#print hash_string('udacity',12) => 11

def hash_string(keyword,buckets):
    sum = 0
    for l in keyword:
        sum += ord(l)
    return sum%(buckets)

print hash_string('a',12)
print hash_string('b',12)
print hash_string('a',13)
print hash_string('au',12)
print hash_string('udacity',12)
