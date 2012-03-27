#Define a procedure, hashtable_get_bucket,
#that takes two inputs - a hashtable, and
#a keyword, and outputs the bucket where the
#keyword could occur.

#hash_string(keyword,nbuckets) => index of bucket

def hashtable_get_bucket(htable,keyword):
    nbuckets = len(htable)
    return htable[hash_string(keyword,nbuckets)]


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
    

