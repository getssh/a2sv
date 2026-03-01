class Solution: 
    def selectionSort(self, arr):
        #code here
        '''
        4, 1, 3
        1, 4, 3
        1, 3, 4
        '''
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if (arr[i] > arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
        
        return arr
