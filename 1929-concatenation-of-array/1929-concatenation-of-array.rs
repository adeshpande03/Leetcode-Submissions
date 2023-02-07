impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        let mut v: Vec<i32> = nums.clone();
        for i in v.iter()
        {
            nums.push(*i)
        }
        
        nums
    }
}