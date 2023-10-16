class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams_map = defaultdict(list)

        for string in strs:
            alphabet_count = [0] * 26

            for letter in string:
                alphabet_count[ord(letter) - ord("a")] += 1

            groupAnagrams_map[tuple(alphabet_count)].append(string)

        return groupAnagrams_map.values() 