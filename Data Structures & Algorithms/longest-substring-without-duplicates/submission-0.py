class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        outs = []
        for i in s:
            if i not in substring:
                substring += i
            else:
                outs.append(len(substring))
                substring = substring[substring.index(i)+1:] + i
        outs.append(len(substring))
        return max(outs)