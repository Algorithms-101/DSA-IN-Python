class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        box = [a for a in nums1]+ [b for b in nums2]
        median = ''
        for x in range(len(box)):
            try:
                if box[x] > box[x + 1]:
                    box[x], box[x + 1] = box[x+1], box[x]
            except:pass
        box.sort()
        medianindex = int(((len(box)+1)/2)-1)
        return box[medianindex]
print(Solution().findMedianSortedArrays([1,3],[5,7,2]))