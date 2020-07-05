class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        maxlen=0
        minlen=0
        flag = False
        nums3 = list()
        if len(nums1) > len(nums2):
            maxlen = len(nums1)
            minlen = len(nums2)

        else:
            maxlen = len(nums2)
            minlen = len(nums1)
        
        for x in range(minlen):
            for y in range(maxlen):
                if minlen == len(nums2):
                    if nums1[y]==nums2[x] and nums1[y] not in nums3:
                        print("here")
                        nums3.append(nums1[y])
                        
                if minlen == len(nums1):
                    if nums2[y] == nums1[x] and nums2[y] not in nums3:
                        nums3.append(nums2[y])
                        
            flag=False
        return nums3
sol  = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
l = sol.intersection(nums1, nums2)
print("",l)