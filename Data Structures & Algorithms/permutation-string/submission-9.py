class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        for c in s1:
            counts1[ord(c) - ord("a")] += 1

        L = 0
        for R in range(len(s2)):
            idx = ord(s2[R]) - ord("a")

            # character not in s1 → reset window
            if counts1[idx] == 0:
                counts2 = [0] * 26
                L = R + 1
                continue

            counts2[idx] += 1

            while counts2[idx] > counts1[idx]:
                counts2[ord(s2[L]) - ord("a")] -= 1
                L += 1

            if R - L + 1 == len(s1):
                return True

        return False
