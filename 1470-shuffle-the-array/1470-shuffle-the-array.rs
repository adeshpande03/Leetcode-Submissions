impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut f: Vec<i32> = vec![];
        
        let firstSlice = &nums[0..nums.len() / 2];
        let secondSlice = &nums[nums.len()/2..nums.len()];
        for (x) in 0..n
        { 
            f.push(firstSlice[x as usize]);
            f.push(secondSlice[x as usize]);
        }
        f
    }
}