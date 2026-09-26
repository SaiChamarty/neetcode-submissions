class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make a list of tuples position, speed
        list_cars = []
        stack = []
        num_fleets = 0
        for i in range(len(position)):
            list_cars.append((position[i], speed[i]))
        list_cars.sort(key=lambda x: x[0])
        for i in range(len(position) - 1, -1, -1):
            # calculate the time to end...
            pos, sp = list_cars[i]
            time_to_target = (target - pos) / sp
            if stack and stack[-1] >= time_to_target:
                    # the previous is slower than current.. no change
                    continue
            else:
                stack.append(time_to_target)
        return len(stack)


