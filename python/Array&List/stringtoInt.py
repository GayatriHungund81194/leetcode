def myAtoi(str: str) -> int:
        a = [1,2,3,4,5,6,7,8,9]
        for i in range(len(str)):
            if (int(str[i]) in a):
                print(str[i])
            else:
                print("dfdfdfd")
myAtoi("  42")