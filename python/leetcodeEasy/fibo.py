# resultStore = dict()
# def fibo(n):
#     if (n == 0):
#         return 0
    
#     elif (n==1 or n==2):
#         return 1

#     if n in resultStore:
#         print("returning stored value")
#         return resultStore[n]

#     else:
#         print("recursive value")
#         res = fibo(n-1) + fibo(n-2)
#         return res
    
# if __name__ == "__main__":
#     for i in range(5):
#         print(fibo(i))
class Solution(object):
    def __init__(self):
        self.resultStore={}
    def fibo(self,n):
        if n in self.resultStore:
            print("returning stored value")
            return self.resultStore[n]

        if (n == 0):
            self.resultStore[0]=0
            return 0
        
        elif (n==1 or n==2):
            self.resultStore[n]=1
            return 1

        print("recursive value")
        print("calculating fib of:",n)
        res = self.fibo(n-1) + self.fibo(n-2)
        self.resultStore[n] = res
        return res

sol=Solution()
sol.fibo(4)

