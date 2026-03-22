class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = sorted(zip(position, speed), reverse=True)
        last_time = -1
        res = 0 
        for pos,speed in data:
            arrive = (target-pos)/speed
            if  arrive>last_time:
                last_time = arrive
                res+=1
        return res
        