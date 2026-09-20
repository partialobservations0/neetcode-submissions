class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        nrows = len(matrix)
        ncols = len(matrix[0])

        def binary(nums):
            left = 0
            right = len(nums)
            
            while right > left:
                mid = (left+right)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid 
            return False

        def mat_binary():
            lefti = find_row()
            print(lefti)
            if matrix[lefti][ncols-1] == target:
                return True
            else:
                return binary(matrix[lefti])

        def find_row():
            # lets first reduce columns
            lefti = 0
            leftj = 0 
            righti = nrows - 1 
            rightj = ncols - 1
            if lefti == righti:
                return lefti
            # first find if in upper or lower half
            # meaning search at [(lefti + righti)//2 ][ncols]
            while lefti < righti:
                print(lefti)
                print(righti)
                print(matrix[lefti][rightj])

                if lefti == righti:
                    return lefti
                midi = (lefti + righti)//2
                if matrix[midi][rightj] == target:
                    return midi
                elif matrix[midi][rightj] < target:
                    lefti = midi + 1
                elif matrix[midi][rightj] > target:
                    righti = midi
            return lefti

        return mat_binary()

            

        