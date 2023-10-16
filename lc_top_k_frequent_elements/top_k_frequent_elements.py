class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for key, value in freq_map.items():
            freq_arr[value].append(key)

        ans_arr = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for key in freq_arr[i]:
                ans_arr.append(key)
                if len(ans_arr) >= k:
                    return ans_arr