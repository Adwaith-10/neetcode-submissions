class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        st = []
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                # ch should be a closer; stack must not be empty and must match
                if not st or st[-1] != pairs.get(ch, '#'):
                    return False
                st.pop()
        return not st
