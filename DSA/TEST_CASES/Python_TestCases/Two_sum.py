class Solution:
    def twoSum(self,List, target):
        check = set()
        for i in range(len(List)):
            if List[i] in check:
                return [List.index(target - List[i]), i]
            else:
                check.add(target - List[i])
                
List=[1,2,3,4,5,6]
TS = Solution()
print(TS.twoSum(List,9))
