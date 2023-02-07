impl Solution {
    pub fn num_jewels_in_stones(jewels: String, mut stones: String) -> i32 {
        let mut x = 0;
        let mut len = stones.chars().count() as i32;
        for i in jewels.chars()
        {
            stones = stones.replace(i, "");
            x += len - (stones.chars().count() as i32);
            len = (stones.chars().count() as i32);
        }
        x
    }
}