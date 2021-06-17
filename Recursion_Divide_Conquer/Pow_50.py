import math


class Solution(object):
    def myPow_iterative(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # iterator
        # Time Limit Exceeded
        if n == 0:
            return 1
        abs_n = abs(n)
        result = x
        while abs_n > 1:
            result = result * x
            --abs_n
        if n < 0:
            return 1/result
        else:
            return result

        def myPow_divide(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            # recursive
            def pow(x,n):
                if n == 0:
                    return 1
                if n == 1:
                    return x
                elif n%2 == 0:
                    temp = pow(x, n / 2)
                    return temp * temp
                else:
                    temp = pow(x, (n-1) / 2)
                    return temp * temp * x

            if n >= 0 :
                return pow(x,n)
            else:
                return 1/pow(x,-n)
















