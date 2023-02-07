impl Solution {
    pub fn get_concatenation(mut nums: Vec<i32>) -> Vec<i32> {
        let mut v = nums.clone();
        v.append(&mut nums);
        v
    }
}
// impl Solution {
//     pub fn get_concatenation(mut nums: Vec<i32>) -> Vec<i32> {
//         let mut result = nums.clone();
//         result.append(&mut nums);
//         result
//     }
// }