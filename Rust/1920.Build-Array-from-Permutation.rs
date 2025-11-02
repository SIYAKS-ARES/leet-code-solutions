impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![];
        
        for &id in nums.iter() {
            ans.push(nums[id as usize]);
        }
        
        ans
    }
}