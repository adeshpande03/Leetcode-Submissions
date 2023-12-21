impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut v = vec![];
        for i in nums.iter()
        {
            v.push(nums[*i as usize]);
        }
        v
    }
}