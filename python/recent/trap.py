def trap(height):
        if len(height) < 3:
            return 0
        
        ret = 0
        left = [-1] * len(height)
        right = [-1] * len(height)
        left_max = -1
        right_max = -1
        
        for i in range(0, len(height)):
            left_max = max(left_max, height[i])
            left[i] = left_max
            print(left)
            
        for i in range(len(height)-1, -1, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max
            print(right)
            
        for i in range(1, len(height)-1):
            ret += min(left[i], right[i]) - height[i]
            print(ret)
            
        print(ret)
h =[0,1,0,2,1,0,1,3,2,1,2,1]
trap(h)