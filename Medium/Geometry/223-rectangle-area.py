class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def rectArea(ax1: int, ay1: int, ax2: int, ay2: int):
            return (ay2-ay1)*(ax2-ax1)#vert*hor
        
        #find intersection area
        intersection = 0
        if (ay1>=by2 or by1>=ay2) or  ( bx1>=ax2 or ax1>=bx2 ): #one is above the other or to the side and no intersection
            intersection = 0
        else:
            mini_topy = min(ay2,by2)
            maxi_buty = max(ay1,by1)
            height = mini_topy-maxi_buty
            mini_rightx = min(ax2,bx2)
            maxi_leftx = max(ax1,bx1)
            width = mini_rightx-maxi_leftx
            intersection  = height*width
        
        return rectArea(ax1, ay1, ax2, ay2) + rectArea(bx1, by1, bx2, by2) - intersection

#cleaner
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, 
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        # Calculate individual areas
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Calculate intersection dimensions
        # The overlap starts at the maximum of the left/bottom edges
        # and ends at the minimum of the right/top edges.
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        
        # If there is no overlap, width or height will be negative.
        # max(0, ...) handles the "no intersection" case automatically.
        intersection = max(0, overlap_width) * max(0, overlap_height)
        
        return area_a + area_b - intersection