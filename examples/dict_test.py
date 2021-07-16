import heapq

count_dict = dict();


#  ===== 如果字典中不存在key，直接给默认值 ====
# key:t,vaule:2
# key:e,vaule:1
# key:s,vaule:1
def dict_return_default_demo():
    s = "test"
    for c in s:
        count = count_dict.get(c, 0)
        count_dict[c] = count + 1

    count_dict["A"] = 23
    count_dict["B"] = 24

    for key, value in count_dict.items():
        print(f"key:{key},vaule:{value}")


# comprehension
def comprehension_test():
    a = [1, 2, 3, 4, 5]
    # list
    squares = [x ** 2 for x in a]
    even_squares = [x ** 2 for x in a if x % 2 == 0]

    # dictionary
    even_squares_dict = {x: x ** 2 for x in a if x % 2 == 0}

    # two control
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]

    # Combining multiple lists into one
    b = [6, 7, 8, 9, 10]
    [(x + y) for (x, y) in zip(a, b)]


# generator
def generator_test():
    a = [1, 2, 3, 4, 5]
    it = (x ** 2 for x in a)
    for x in it:
        print(x)


# generator_test()


# segregate
# 整理数组，把正负数分隔开
# [1,-1,4,-2,-5,-6]  => [-1,-5,-6,1,4]
def segregate(arr, size):
    j = 0
    for i in range(size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1  # increment count of non-positive integers
    return j


# 检查key是否在dict中
def dict_check():
    test_list = ["A", "C", 1]
    count_dict[1] = 100
    for char in test_list:
        if char in count_dict:
            print(f"chat {char}: Yes")
        else:
            print(f"chat {char}: No")


# stack
def stack_demo():
    stack = []
    stack.append("(")
    stack.append("[")
    # Pop the topmost element from the stack, if it is non empty
    # Otherwise assign a dummy value of '#' to the top_element variable
    top_element = stack.pop() if stack else '#'


#
def Str_demo():
    # "".join(path)   list ——> Str
    combinations = []
    path = ["ab", "v", "c"]
    combinations.append("".join(path))
    possible_letters = "abshdnc"
    for letter in possible_letters:
        print(letter)

    # 根据不同条件求list中的min 和max
    shortest = min(path, key=len)
    for index, char in enumerate(shortest):
        print(f"index:{index},{char}")


Str_demo()


def backtrack(index, path):
    digits = []
    combinations = []
    letters = {}
    # If the path is the same length as digits, we have a complete combination
    if len(path) == len(digits):
        combinations.append("".join(path))
        return  # Backtrack

    # Get the letters that the current digit maps to, and loop through them
    possible_letters = letters[digits[index]]
    for letter in possible_letters:
        # Add the letter to our current path
        path.append(letter)
        # Move on to the next digit
        backtrack(index + 1, path)
        # Backtrack by removing the letter before moving onto the next
        # !!!!! backTracking 非常关键的一步，每个数字有3个字母，一个一个轮流上
        path.pop()


# What is the correct way to write a doctest?
# def sum(a, b):
#     """
#     >>> sum(4, 3)
#     7
#
#     >>> sum(-4, 5)
#     1
#     """
#     return a + b


#  string reverse
def str_reverse():
    x = 12345
    str_x = str(x)
    rev_x = str_x[::-1]
    print(rev_x)


# str_reverse()

# shortest string
def shortest_string():
    strs = ["aa", "yt", "ss", "uh"]
    shortest = min(strs, key=len)


# 一个非常巧妙的判断
# and 具有断电功能，只有全部都true才返回true，只要其中一个false立即返回false
# p is q 可以判断 p==None and q==None
def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q


# python priority queue
# heapq Heap queue algorithm
# To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().
class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:  # 只保留k个最大值，如果超过k个，那么把最小的出队（所以最小优先队列）
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        # 如果要加入的新值大于队列最小值，那么队列pop，再把新值加入队列
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        # return pop
        return self.pool[0]
