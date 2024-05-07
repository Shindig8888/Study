// fn takes_u32(x: u32) {
//     println!("u32: {x}");
// }

// fn takes_ui8(y: i8) {
//     println!("i8: {y}");
// }

// fn main() {
//     let x = 10;
//     let y = 20;

//     takes_u32(x);
//     takes_ui8(y);
// }

// fn fib(n: u32) -> u32 {
//     if n <= 2 {
//         return 1;
//     } else {
//         return fib(n - 1) + fib(n - 2);
//     }
// }

// fn main() {
//     let n = 20;
//     println!("fib({n}) = {}", fib(n))
// }

//#if 표현식
// fn main() {
//     let x = 10;
//     if x == 0 {
//         println!("zero");
//     } else if x < 100 {
//         println!("큰")
//     } else {
//         println!("거대한")
//     }
// }

// fn main() {
//     let x = 10;
//     let size = if x < 20 { "작은" } else { "대형" };
//     println!("{size}")
// }

// fn main() {
//     let mut x = 200;
//     while x >= 10 {
//         x = x / 2;
//     }
//     println!("{x}")
// }

// fn main() {
//     for x in 1..5 {
//         println!("x: {x}");
//     }

//     for elem in [1,2,3,4,5] {
//         println!("elem: {elem}")
//     }
// }

// fn main() {
//     let mut i = 0;
//     loop {
//         i += 1;
//         if i>5 {
//             break;
//         }

//         if i%2 == 0 {
//             continue;
//         }
//         println!("{}", i);
//     }
// }

//#label
// fn main() {
//     let s = [[5, 6, 7], [8, 9, 10], [21, 15, 32]];
//     let mut elements_searched = 0 ;
//     let target_value = 10;
//     'outer : for i in 0..=2 {
//         for j in 0..=2 {
//             elements_searched += 1;
//             if s[i][j] == target_value {
//                 break 'outer;
//             }
//         }
//     }
//     println!("elements searched: {elements_searched}")
// }

//#블록
// fn main() {
//     let z = 13;
//     let x = {
//         let y = 10;
//         println!("y = {y}");
//         z-y
//     };
//     println!("x: {x}")
// }

//#매크로
// fn factorial(n:u32)->u32 {
//     let mut product = 1;
//     for i in 1..=n {
//         product *= dbg!(i);
//     }
//     product
// }

// fn fizzbuzz(n:u32) -> u32 {
//     todo!()
// }

// fn main() {
//     let n = 4 ;
//     println!("{n}! = {}", factorial(n))
// }

//콜라츠수열
fn collatz_length(n: i32) -> u32 {
    let mut length = 0;
    let mut col = n;
    loop {
        length += 1;
        if col == 1 {
            return length;
        } else if col % 2 == 0 {
            col = col / 2
        } else {
            col *= 3
        }
    }
}

fn main() {
    let n = 64;
    println!("{}", collatz_length(n));
}
