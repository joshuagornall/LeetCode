class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:    # test case: nums = [5, 0, 3, 8, 6]
        right = list(accumulate(nums, max))                 # prints right -> [5, 5, 5, 8, 8]
        left = list(accumulate(nums[::-1], min))[::-1]      # prints left -> [0, 0, 3, 6, 6]
        for i in range(1, len(nums)):                    
            if right[i-1] <= left[i]:                       # i=1 -> right 5 !<= 0 left
                print(i)                                    # i=2 -> right 5 !<= 3 left
                return i                                    # i=3 -> right 5  <= 6 left  | returns i=3
              
