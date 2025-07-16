from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_map = defaultdict(int)
        # t_map = defaultdict(int)
        # for character in s:
        #     s_map[character]+= 1

        # for character in t:
        #     t_map[character]+= 1

        # return s_map == t_map

        return Counter(s) == Counter(t)