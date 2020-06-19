'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    while len(word) > 1:
        count = 0
        for i in range(len(word)-1):
            if word[i] == 't' and word[i+1]=='h':
                count = count_th(word[i+2:])
                return count + 1
        return 0
    return 0
arr = 'abcthefthghith'
print(count_th(arr))