
from itertools import combinations


def substring(word: str):
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            print(word[i: j])
# substring("word")

# Another approach
def substring2(word:str)-> list:
    res = [word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1)]
    return res
# substring2("word")



# using combination since the position doesn't really matter
def substring3(word: str) -> list:
    res = [word[i:j] for i, j in combinations(range(len(word)+1), r= 2)]
    return res


substring3("word")
