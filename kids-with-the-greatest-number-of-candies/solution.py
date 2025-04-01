class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest_number= 0
        for x in candies:
            if largest_number < x:
                largest_number = x
        result  = []
        for x in candies:
            if x+extraCandies >= largest_number:
                result.append(True)
            else:
                result.append(False)
        return result
