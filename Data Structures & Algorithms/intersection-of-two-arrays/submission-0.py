class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        set1 = set(nums1)

        for i in nums2:
            if i in set1:
                result.add(i)

        return list(result)