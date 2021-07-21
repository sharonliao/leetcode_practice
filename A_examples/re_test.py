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
    print(max_cnt)
    return max_cnt


def str_check_start_with_0():
    s = "01x110"
    # 1. check if this s is digit
    # 2. if yes, then check if this s start with 0
    if s.isdigit():
        return str(int(s)) == s
    else:
        return False

solution2(text)