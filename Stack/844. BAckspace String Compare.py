    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(S):
            stack = []
            for c in S:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(s) == build(t)
