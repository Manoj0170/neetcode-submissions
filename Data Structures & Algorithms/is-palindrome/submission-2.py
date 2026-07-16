class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''

        for st in s:
            if st.isalpha() or st in [str(x) for x in range(0,10)]:
                s1=s1+st.lower()
        # print(st,st[::-1])
        if s1==s1[::-1]:
            return True
        else:
            return False
        