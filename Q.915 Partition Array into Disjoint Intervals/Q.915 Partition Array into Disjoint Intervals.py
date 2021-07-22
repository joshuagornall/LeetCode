class Solution:
    def partitionDisjoint(self, nums):
        comparison = nums[0]
		# within numsMax we will keep track of the largest number we found so far
        numsMax = comparisonItem
		# result index
        partitionIdx = 0
        for i in range(1, len(nums)):
			# when we find lower item in an array we update partitionIdx to reflect it
			# and also set out comparison to the highest item we found prior to this item
            if (nums[i] < comparison):
                partitionIdx = i
                comparison = numsMax
			# keep track of the largest item we seen so far
            else:
                numsMax = max(numsMax, nums[i])
		# as we are storing an index of the last item that belongs to the partition
		# and arrays are indexed from 0 we need to increment the value
        return partitionIdx + 1
	
