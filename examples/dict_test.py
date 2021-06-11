count_dic = dict();


#  ===== 如果字典中不存在key，直接给默认值 ====
s = "test"
for c in s:
    count = count_dic.get(c, 0)
    count_dic[c] = count + 1

