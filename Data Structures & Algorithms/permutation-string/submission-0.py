class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = len(s1)
        for i in range(len(s2)):
            if s2[i] in s1:
                if i + x <= len(s2):
                    if sorted(s2[i:i+x]) == sorted(s1):
                        return True

        return False