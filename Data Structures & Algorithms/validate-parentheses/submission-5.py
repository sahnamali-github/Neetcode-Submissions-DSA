class Solution:
    def isValid(self, s: str) -> bool:
        # while "[]" in s or "{}" in s or "()" in s:
        #     s = s.replace("[]", "")
        #     s = s.replace("{}", "")
        #     s = s.replace("()", "")
        # return s == ""

        stack = []
        pairs = {"}" : "{", "]" : "[", ")" : "("}
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False



        

   