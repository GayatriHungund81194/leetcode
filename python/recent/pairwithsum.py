def findPair(nums, target):
    if not nums:
        return []
    
    target -= 30
    dic, cand = {}, {}
    for i in range(len(nums)):
        if nums[i] in dic:
            cand[max(nums[i], target-nums[i])] = [dic[nums[i]], i]
            # cand = {40:[0,2], 50:[1,5]} for the example 2 given 
        else:
            dic[target-nums[i]] = i
            
    return cand[max(cand.keys())]