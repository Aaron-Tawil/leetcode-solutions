class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        bot,top = 0,len(numbers)-1
        while(bot<top):
            if numbers[bot]+numbers[top]==target:
                return [bot+1,top+1]
            if numbers[bot]+numbers[top]<target:
                bot+=1
            else:
                top-=1
        return [-1]