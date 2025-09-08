class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up positions and speeds for each car
        cars = [(pos, spd) for pos, spd in zip(position, speed)]

        # Sort cars by starting position in descending order (closest to target first)
        cars.sort(reverse=True)

        fleets = []  # stack to keep track of fleet arrival times

        for position, speed in cars:
            # Time for this car to reach the target
            time_to_target = (target - position) / speed
            
            # If the car catches up to the fleet in front, they merge (skip push)
            if fleets and time_to_target <= fleets[-1]:
                continue
            
            # Otherwise, this car forms a new fleet
            fleets.append(time_to_target)

        return len(fleets)