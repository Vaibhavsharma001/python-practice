# 1
# 22
# 333
# 4444
# 55555


class solution:
    def pattern(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end = "")
            print()

obj = solution()
obj.pattern(5)


print()

class solution2:
    def pattern2(self,n):
        i =1
        while i<=n:
                j=1
                while j <= i:
                    print(i, end = "")
                    j+=1
                i+=1
                print()
obj1 = solution2()
obj1.pattern2(5)