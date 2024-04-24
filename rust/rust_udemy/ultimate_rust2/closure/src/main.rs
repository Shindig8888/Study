//closures
// fn main() {
//     let add = |x, y| x+y;
//     println!("{}", add(1,2));

//     let s = "아아아아";
//     let f = move || {
//         println!("{}", s)
//     };

// }

//iterator
// fn main() {
//     let v = vec![6,7,8,9];

//     v.into_iter().for_each(|num| println!("{}", num));
// }

//map
fn main() {
    let v = vec![6, 7, 8];
    let total: Vec<i32> = v
        .into_iter()
        .map(|x| x * 3)
        .filter(|y| *y % 2 == 0)
        .collect();
    println!("{:?}", total)
}
