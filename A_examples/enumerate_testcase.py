#当迭代list时，通常还想知道当前元素在列表中的index
flavor_list = ['vanilla','chocolate','pecan','strawberry']
for i, flavor in enumerate(flavor_list):
    print("%d: %s"%(i,flavor))