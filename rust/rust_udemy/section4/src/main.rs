// ownership
//1. each value has an owner
//2. only one owner per value
//3. value gerts dropped after scope

// fn main(){
//     let s1 = String::from("abc");
//     let s2 = s1;
//     println!("{s1}"); // error
// }

// use .clone(): copies both stack and heap .copy(): copies only stack

// fn main() {
//     let s1 = String::from("abc");
//     do_stuff(s1);
//     println!("{s1}")
// }

// fn do_stuff(s: String) {}

// fn main() {
//     let mut s1 = String::from("abc");
//     s1 = do_stuff(s1);// do_stuff에 넘겨준 오너십을 다시 받기
//     println!("{s1}")
// }

// fn do_stuff(s: String) -> String {
//     s
// } 

//ref and borrowing
// fn main() {
//     let s1 = String::from("abc");
//     do_stuff(&s1);
//     println!("{s1}")
// }

// fn do_stuff(s: &String) {
//     //
// } 

//mutable ref
fn main() {
    let mut s1 = String::from("abc");
    do_stuff(&mut s1);
    println!("{s1}")
}

fn do_stuff(s: &mut String) {
    s.insert_str(0, "Hi, ");
    *s = String::from("Replacement"); // 레퍼런스 해제, s == mut s1
} 