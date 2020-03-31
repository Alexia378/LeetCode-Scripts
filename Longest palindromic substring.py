#Given a string s, find the longest palindromic substring in
#s. You may assume that the maximum length of s is 1000.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
    
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
    
        res = s[0]
    
        for i in range(len(s)-1):
            if i > 0 and s[i] == s[i-1]:
                continue
            
            l , r = i - 1 , i + 1
            
            temp = [s[i]]
        
            while r <= len(s) - 1:
                if s[i] == s[r]:
                    temp.append(s[r])
                    r += 1
                else:
                    break
                
            
            while l >= 0 and r < len(s):
                if s[l] == s[r] and r > i:
                    temp.insert(0, s[l])
                    temp.append(s[r])
                    l -= 1
                    r += 1      
                else:
                    break
        
            if len(temp) > len(res):
                res = temp

        return ''.join(res)
