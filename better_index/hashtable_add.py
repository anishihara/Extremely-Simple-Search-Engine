#Define a procedure,

#hashtable_add(htable,key,value)

#that adds the key to the hashtable
#(in the correct bucket), with the
#correct value.

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for bucket_unit in bucket:
        if bucket_unit[0] == key:
            bucket_unit[1].append(value)
            return
    bucket.append([key,[value]])
        


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

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

table = make_hashtable(10)
hashtable_add(table,'teste','http://www.udacity.com')
hashtable_add(table,'teste','http://www.udacity.com/2')
hashtable_add(table,'abc','http://www.google.com')
print table