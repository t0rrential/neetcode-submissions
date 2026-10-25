class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd
            
            if stack and time <= stack[-1]:
                continue          # catches the fleet ahead, merges
            stack.append(time)    # new fleet
        return len(stack)