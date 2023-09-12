def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1

        while top<=bottom:
            mid=(top+bottom)//2
            if target<matrix[mid][0]:
                bottom = mid-1
            elif target>matrix[mid][-1]:
                top = mid+1
            else:
                break
        
        l,r = 0, columns-1
        row = (top+bottom)//2
        while l<=r:
            mid=(l+r)//2
            print("from line 18 l:,r:,mid:",l,r,mid)
            if target<matrix[row][mid]:
                print(f"r:{r} mid:{mid} value:{matrix[row][mid]}")
                r = mid-1
            elif target>matrix[row][mid]:
                print("line 22",l)
                l = mid+1
            else:
                return True
        return False




def runTest():
    m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    t1,t2 = 3, 13
    if searchMatrix(m1,t1): # type: ignore
        print("Test 1 passed", True)
    if not searchMatrix(m1,t2):
        print("Test 2 passed", True)
    return 0

runTest()