#Define a procedure, lookup,
#that takes two inputs:

#   - an index
#   - keyword

#The output should be a list
#of the urls associated
#with the keyword. If the keyword
#is not in the index, the output
#should be an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

#lookup(index,keyword) => ['http://udacity.com','http://npr.org']


def lookup(index,keyword):
    filtered_index = filter(lambda x: x[0] == keyword,index)
    if len(filtered_index) > 0:
        keyword_url = index[index.index(filtered_index[0])]
        return keyword_url[1]
    else:
        return []

keyword = 'udacity'     
print lookup(index,keyword)