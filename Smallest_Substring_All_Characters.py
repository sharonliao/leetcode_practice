def solution(arr, str):
    cistr = dict()  # chars_in_substring
    num_unique_chars = 0
    len_arr = len(arr)

    min_suitable_str = None
    # get closest char and start from there

    for key, letter in enumerate(str):
        # store indice at which letter occurs
        # 记录char 第一次出现的index
        if letter not in cistr:
            num_unique_chars += 1
            cistr[letter] = key

        if num_unique_chars == len_arr:
            # we have a suitable substring
            min_ind_char = min(cistr.values())
            ukey = key + 1  # 1-indexed key
            suitable_substr = str[min_ind_char:ukey]

            if min_suitable_str == None or (len(suitable_substr) < len(min_suitable_str)):
                min_suitable_str = suitable_substr

            # pop off character with smallest indice
            # and continue reading
            del cistr[min(cistr, key=cistr.get)]
            num_unique_chars -= 1

    return min_suitable_str