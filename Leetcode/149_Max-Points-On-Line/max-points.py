from collections import deque   
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #pomysł jest taki, biorę po kolei punkt, kolejny, robię równanie prostej i czy jakiś jeszcze należy
        max_found = 0
        # for i in range(len(points)):
        if len(points) <= 2:
            return len(points)

        points_deq = deque(points)
        while points_deq:
            a = points_deq.popleft()
            for i, b in enumerate(points_deq):
                checking_points = list(points_deq)[i+1:]
                found = 2

                if a[0] != b[0]:
                    wspA = (b[1]-a[1])/(b[0]-a[0])
                    wspB = a[1]-wspA*a[0]

                    for check in checking_points:
                        if check[1] == wspA*check[0]+wspB:
                            found += 1

                else:
                    for check in checking_points:        
                        if check[0] == a[0]:
                            found +=1    

                max_found = max(found, max_found)
       
        return max_found




if __name__ == "__main__":
    task = Solution()
    points = [[1,1],[2,2],[3,3]]
    print(task.maxPoints(points))

    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(task.maxPoints(points))

    points = [[-6,-1],[3,1],[12,3]] #result = 3
    print(task.maxPoints(points))
