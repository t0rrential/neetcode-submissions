class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        sol = []
        l, r = 0, length-1

        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]

        if numbers[l] + numbers[r] < target:
            print("not enough")

            # forwards from l as smallest num is not enough to eclipse target
            for i in range(l, r):
                print(f"checking {numbers[i]} + {numbers[r]}")
                # if i + r suddenly is larger than target
                while numbers[i] + numbers[r] > target:
                    print(f"{numbers[i]} + {numbers[r]} > target")
                    r -= 1
                
                print(f"now checking {numbers[i]} + {numbers[r]}")

                if numbers[i] + numbers[r] == target:
                    sol = [i+1, r+1]
                    break

        elif numbers[l] + numbers[r] > target:
            print("too much")

            # backwards from r as largest num eclipses target
            for i in range(r, l, -1):
                print(f"checking {numbers[l]} + {numbers[i]}")
                    # if l + i suddenly is smaller than target
                while numbers[l] + numbers[i] < target:
                    print(f"{numbers[l]} + {numbers[i]} < target")
                    l += 1
                
                print(f"now checking {numbers[l]} + {numbers[i]}")

                print(f"{numbers[l] + numbers[i] == target}")
                if numbers[l] + numbers[i] == target:
                    sol = [l+1, i+1]
                    break

        return sol
