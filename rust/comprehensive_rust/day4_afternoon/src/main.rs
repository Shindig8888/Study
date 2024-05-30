//오류처리

//패닉
// fn main() {
//     let v = vec![10, 20, 30];
//     println!("v[100]: {}", v[100]);
// }

use std::{panic};

fn main() {
    let result = panic::catch_unwind(|| "rhoscksgtmqslek");
    println!("{result:?}");

    let result = panic::catch_unwind(|| {
        panic!("oops");
    });
    println!("{result:?}");
}
