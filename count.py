class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))
        
        def merge_sort(start, end):
            if start >= end:
                return
            
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid + 1, end)
            
            # Contagem antes do merge
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[indices[i]] > nums[indices[j]]:
                    j += 1
                else:
                    counts[indices[i]] += j - (mid + 1)
                    i += 1
            
            # Atualiza contagem para elementos restantes
            while i <= mid:
                counts[indices[i]] += end - mid
                i += 1
                
            # Merge das duas metades
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[indices[i]] <= nums[indices[j]]:
                    temp.append(indices[i])
                    i += 1
                else:
                    temp.append(indices[j])
                    j += 1
            while i <= mid:
                temp.append(indices[i])
                i += 1
            while j <= end:
                temp.append(indices[j])
                j += 1
                
            indices[start:end+1] = temp
        
        merge_sort(0, n - 1)
        return counts