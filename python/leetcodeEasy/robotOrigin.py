def judgeCircle(moves: str) -> bool:
            countl=0
            countu=0
            for i in range(len(moves)):
                if moves[i] == 'D':
                    countu = countu+1
                elif moves[i] == 'U':
                    countu = countu-1
                elif moves[i] == 'L':
                    countl = countl+1
                elif moves[i] == 'R':
                    countl = countl-1
            if countl==0 and countu==0:
                return True
            else:
                return False
st = "LL"
r=judgeCircle(st)
print(r)