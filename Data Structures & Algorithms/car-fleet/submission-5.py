import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        position = list(position)
        speed = list(speed)
        n = len(position)

        stack = []
        for i in range(0, n):
            stack.append([position[i], speed[i]])
        
        ahead_pos, ahead_spd = stack.pop()
        ahead_time = (target - ahead_pos) / ahead_spd
        fleets = 1
        while stack:
            behind_pos, behind_spd = stack.pop()
            behind_time = (target - behind_pos) / behind_spd
            
            if behind_time > ahead_time:
                # behind is slower and cannot catch up to the fleet ahead before/at target
                fleets += 1
                ahead_pos = behind_pos
                ahead_spd = behind_spd
                ahead_time = behind_time

        return fleets
