class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        d = list()
        if x < 0:
            return False
        elif x==0:
            return True
        elif x/10 == 0:
            return True
        else:
            while(x > 0):
                d.append(x%10)
                x/=10
            for i in range(0, len(d)/2):
                if(d[i]!=d[len(d)-i - 1]):
                    return False
            return True

        #return False if x < 0 else x == int(str(x)[::-1])
