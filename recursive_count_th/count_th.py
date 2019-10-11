'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, word_lst=None, ticker=None, count=None, cache=None):
    
    if word == '':
        return 0
    
    elif ticker == 0:
        return count
    
    elif ticker and ticker > 0:
        if cache == 't' and word_lst[0] == 'h':
            count += 1
        ticker -= 1 
        
        if len(word_lst) > 1:
            cache = word_lst[0]
        word_lst = word_lst[1:]
        
        return count_th(word, word_lst, ticker, count, cache)
    
    else:
        if not word_lst:
            word_lst = list(word)
            ticker = len(word_lst) - 1
            count = 0
            cache = word_lst[0]
            word_lst = word_lst[1:]
        
        return count_th(word, word_lst, ticker, count, cache)