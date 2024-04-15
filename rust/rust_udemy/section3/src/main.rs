//타입은 suffix로도 사용가능
// fn main() {
//     let x = 5;
//     let y = 3.14;
//     let a = 5_u16;
//     let b = 3.14_f32;
// }

// //tuple
// fn main() {
//     let info = (1, 3.3, 999);
//     let jets = info.0;
//     let fuel = info.1
//     let ammo = info.2
    

//     let(jets, fuel, ammo) = info
// }

//array 스택에저장
// fn main() {
//     let buf = [0; 3];
//     println!("{:?}", buf);
// }

//lifetime with loop
// 'bob: loop {
//     loop{
//         continue 'bob
//     }
// }

//&str, String
// word.bytes();
// word.chars();
// graphemes(my_string, true)
// .nth(3)

fn main() {
    let s = String::from("hello");
    // let mut chars = s.chars(); // 문자열을 문자 이터레이터로 변환

    let mut chars = s.chars().nth(1);
    println!("{:?}", chars);

    // if let Some(second_char) = chars.nth(1) {
    //     println!("The second character is: {}", second_char);
    // } else {
    //     println!("The string has less than two characters");
    // }
}
