import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 1. get the code for each str
        # 2. put (code, group of strs) in dict
        # 4. time complexity O(NK), space(NK)
        code_dict = {}
        for str in strs:
            code = self.getCode(str);
            if code_dict.get(code) is not None:
                code_dict.get(code).append(str)
            else:
                code_dict[code] = [str]
        print(f"result:{code_dict.values()}")
        return code_dict.values()

    def  getCode(self, s):
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
        print(f"count_list:{count_list}")
        string_ints = [str(int) for int in count_list]
        str_of_ints = ".".join(string_ints)
        print(f"str :{s},code: {str_of_ints}")
        return str_of_ints


    def  getCode_tuple(self, s):
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
        return tuple(count_list)



    def groupAnagrams_advance(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # tuple(count) is hashable
            # directly store group result in the valus
            ans[tuple(count)].append(s)
        return ans.values()




strs = ["bdddddddddd","bbbbbbbbbbc"]

Solution().groupAnagrams(strs)

[["bat"],["nat","tan"],["ate","eat","tea"]]