from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.old_color = self.image[sr][sc]

        self.helper(sr, sc, color)

        return self.image

    def helper(self, sr, sc, color):
        self.image[sr][sc] = color

        for sr_delta, sc_delta in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            sr_new = sr + sr_delta
            sc_new = sc + sc_delta

            if 0 <= sr_new < len(self.image):
                if 0 <= sc_new < len(self.image[0]):
                    if self.image[sr_new][sc_new] == self.old_color:
                        if self.image[sr_new][sc_new] != color:
                            self.helper(sr_new, sc_new, color)

        