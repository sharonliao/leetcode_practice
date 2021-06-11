class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 1. get the code for each str
        # 2. put (code, index of result) in dict
        # 3. the strs have same code put in same place of result list.
        result_list = []
        code_dict = {}
        for str in strs:
            code = self.getCode(str);
            if code_dict.get(code) is not None :
                index = code_dict.get(code)
                print(f"index: {index}")
                result_list[index].append(str)
            else:
                print(f"dict: {code_dict}")
                index = len(code_dict)
                code_dict[code]=index;
                result_list.append([str])
                print(f"new index: {index}")
            print(result_list)

        return result_list

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



strs = ["bdddddddddd","bbbbbbbbbbc"]

Solution().groupAnagrams(strs)

[["bat"],["nat","tan"],["ate","eat","tea"]]