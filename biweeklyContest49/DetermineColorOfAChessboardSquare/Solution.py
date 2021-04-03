class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return not (ord(coordinates[0])-ord('a') + int(coordinates[1])) % 2
    