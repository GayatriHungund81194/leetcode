nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
nums3 = list()
nums4 = list()
nums3 = nums1
nums4  =nums2
# print(nums3)
# print(nums4)
nums5 = list()

for i in range(4):
    if nums3 and nums4:
        n1 = max(nums3)
        n2 = max(nums4)
        if n1> n2:
            nums5.append(n1)
            ind1 = nums3.index(n1)
            nums3 = nums3[ind1+1:]
            print(nums3)
        else:
            nums5.append(n2)
            ind2 = nums4.index(n2)
            nums4 = nums4[ind2+1:]
            print(nums4)
    else:
        if nums3:
            nums5 = nums5 + nums3
        else:
            nums5 = nums5 + nums4
# print(nums3)
# print(nums4)
print(nums5)
