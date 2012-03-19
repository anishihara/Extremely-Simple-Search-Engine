#Define a procedure, add_to_index,
#that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

#If the keyword is already
#in the index, add the url
#to the list of urls associated
#with that keyword.

#If the keyword is not in the index,
#add an entry to the index: [keyword,[url]]

index = []


#add_to_index(index,'udacity','http://udacity.com')
#add_to_index(index,'computing','http://acm.org')
#add_to_index(index,'udacity','http://npr.org')
#print index => [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def add_to_index(index,keyword,url): 
    index_keyword = filter(lambda x: x[0] == keyword,index)
    #found a keyword in index
    if len(index_keyword) > 0:
        i = index.index(index_keyword[0])
        keyword_urls = index[i]
        if url not in keyword_urls[1]:
            keyword_urls[1].append(url)
    else:
        index.append([keyword,[url]])
    
add_to_index(index,'udacity','http://udacity.com')
print index
add_to_index(index,'computing','http://acm.org')
print index
add_to_index(index,'udacity','http://npr.org')
print index