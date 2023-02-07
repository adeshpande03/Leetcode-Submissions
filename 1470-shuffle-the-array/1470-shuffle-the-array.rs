impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::new();
        let n = n as usize;
        for x in 0..n
        {
            res.push(nums[x]);
            res.push(nums[x + n]);
        }
        return res;
    }
}
