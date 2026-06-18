class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        i, j = 0, -1
        directions_map = {
            "right":{
                "steps": n,
                "next": "down"
            },
            "down":{
                "steps": m-1,
                "next": "left"
            },
            "left":{
                "steps": n-1,
                "next": "up"
            },
            "up":{
                "steps": m-2,
                "next": "right"
            }
        }
        direction = "right"
        while True:
            steps = directions_map[direction]["steps"]
            while steps > 0:

                if direction == "right":
                    j += 1
                elif direction == "down":
                    i += 1
                elif direction == "left":
                    j -= 1
                elif direction == "up":
                    i -= 1

                res.append(matrix[i][j])
                steps -= 1
                # print(f"direction: {direction}")
                # print(f"(i, j): {(i, j)}")
                # print(f"steps: {steps}")

            if len(res) == m * n:
                return res

            directions_map[direction]["steps"] -= 2
            direction = directions_map[direction]["next"]




