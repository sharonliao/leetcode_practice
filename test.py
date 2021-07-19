def solution(N):
    # write your code in Python 3.6
    result = []
    if N % 2 == 1:
        result.append(0)
    for i in range(1,N//2+1):
        result.append(i)
        result.append(-i)
    return result

import re
text = 'We test coders. Give us a try? Forget CVs..Save time !  X X'
def solution2(S):
    # . ? !
    # We test coders, Give us a try?
    # Forget CVs..Save time .  X X
    #1, slpit into sentenses
    #2. tokenizes
    #3. count words

    sents = re.split('[?.!]', S)
    max_cnt = 0
    for sent in sents:
        # words = re.split('\s', sent)
        words = [x for x in re.split('\s', sent) if len(x)>0]
        max_cnt = max(max_cnt,len(words))
    return max_cnt




solution2(text)

