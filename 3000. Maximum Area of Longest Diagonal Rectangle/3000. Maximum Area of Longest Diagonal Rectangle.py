from cmath import sqrt


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal = 0
        area = 0
        for l, w in dimensions:
            temp_diag = sqrt(l ** 2 + w ** 2)
            temp_area = l * w

            if temp_diag > diagonal:
                area = temp_area
                diagonal = temp_diag
            if temp_diag == diagonal:
                area = max(area, temp_area)

        return area



        