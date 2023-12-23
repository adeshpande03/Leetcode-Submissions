impl Solution {
    pub fn number_of_employees_who_met_target(hours: Vec<i32>, target: i32) -> i32 {
        let mut c = 0;
        for x in hours.iter(){
            if (x >= &target){c = c+ 1;}
        }
        c
    }
}