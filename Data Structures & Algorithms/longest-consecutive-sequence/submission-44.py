class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: return 0
        
        # Vẫn dùng cách của bạn: lọc trùng và sắp xếp -> O(N log N)
        num_sorted = sorted(set(nums)) 
        
        if len(num_sorted) == 1: return 1
        
        longest_streak = 1 # Khởi tạo kỷ lục là 1 (vì mảng có ít nhất 1 phần tử)
        current_streak = 1 # Chuỗi hiện tại cũng bắt đầu là 1
        
        for i in range(len(num_sorted) - 1):
            if num_sorted[i + 1] - num_sorted[i] == 1:
                # Nếu liên tiếp, chỉ cần CỘNG SỐ, không dùng list/set nữa
                current_streak += 1
            else:
                # Nếu đứt đoạn, reset lại bộ đếm về 1
                current_streak = 1
                
            # Cập nhật kỷ lục liên tục
            if current_streak > longest_streak:
                longest_streak = current_streak
                
        return longest_streak