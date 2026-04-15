class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        s_map = {}
        t_map = {}

        for index in range(len(s)):
            s_map[s[index]] = s_map.get(s[index], 0) + 1
            t_map[t[index]] = t_map.get(t[index], 0) + 1

        return s_map == t_map

        