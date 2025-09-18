class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        max_len=0
        st=set()
        for ch in s:
            while ch in st:
                st.remove(s[l])
                l+=1
            
            st.add(s[r])
            r+=1
            max_len=max(max_len,r-l)
        return max_len    
            