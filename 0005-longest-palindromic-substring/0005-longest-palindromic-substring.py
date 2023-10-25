class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (0,0)
        i = 0
        while i<len(s):
            for a,b in [(i,i),(i,i+1)]:
                current = (0,0)
                while a>=0 and b<len(s) and s[a] == s[b]:
                    current = (a,b)
                    a-=1
                    b+=1
                if (current[1]-current[0])>(longest[1]-longest[0]):
                    longest = current
            i+=1
        return s[longest[0]:longest[1]+1]
                
             
            