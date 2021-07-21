def validateIP(ip):
    """
        @param ip: str
        @return: bool
        """
    nums = ip.split(".")
    print(len(nums))
    if len(nums) != 4:
        return False
    for num in nums:
        try:
            if int(num) < 0 or int(num) > 255:
                return False
        except:
            return False
    return True


def isValid(num):
    for c in num:
        if c.isdigit() is not True:
            return False

    return True


print(validateIP('1..23.0'))

x = [1,2,3]
print(x.index(1))
