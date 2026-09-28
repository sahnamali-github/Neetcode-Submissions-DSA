class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1, counts2 = [0]*26, [0]*26
        for c in s1:
            counts1[ord(c) - ord("a")] += 1
        l = 0
        for r in range(len(s2)):
            index = ord(s2[r]) - ord("a")
            if counts1[index] == 0:
                counts2 = [0] * 26
                l = r + 1
                continue
            counts2[index] += 1
            while counts2[index] > counts1[index]:
                counts2[ord(s2[l])- ord("a")] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False
