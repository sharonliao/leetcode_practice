class Solution(object):
    # case 1: s and t consist of lowercase English letters
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1.using a list which size is 26 to store the number of each lowercase English letters
        # 2.using ascii-97 as index of list
        count_list = [0]*26
        for c in s :
            index = ord(c)-97
            count_list[index] += 1;
        for c in t:
            index = ord(c)-97
            count_list[index] += -1;
        for cnt in count_list:
            if cnt != 0:
                return False
        return True;

    def isAnagram_hashmap(self, s, t):
        # 1.using a hashmap if the inputs contain Unicode characters
        if len(s) != len(t) :
            return False
        count_dic = dict();
        for c in s:
            count = count_dic.get(c, 0)
            count_dic[c] = count + 1
        for c in t:
            count = count_dic.get(c, 0)
            if count == 0 :
                return  False
            count_dic[c] = count - 1
        for c in count_dic.values():
            if c != 0 :
                return False
        return True;

s = "sbag"
t = "ssss"
result = Solution().isAnagram_hashmap(s,t)
print(f"{s} , {t} :  {result}")



