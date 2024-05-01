//패턴

//패턴이 사용될 수 있는 모든 곳
//#match
// fn main() {
//     match x {
//         None => None,
//         Some(i) => Some(i+1)
//     }
// }

//#if let
// fn main() {
//     let favorite_color: Option<&str> = None;
//     let is_tuesday = false;
//     let age: Result<u8, _> = "34".parse();

//     if let Some(color) = favorite_color {
//         println!("Using your faborite color, {color}, as the background.");
//     } else if is_tuesday {
//         println!("Tuesday is green day!");
//     } else if let Ok(age) = age {
//         if age > 30 {
//             println!("Using purple as the background color");
//         } else {
//             println!("Using orange as the background color");
//         }
//     } else {
//         println!("Using blue as the background color");
//     }
// }

//#while let
// fn main() {
//     let mut stack = Vec::new();

//     stack.push(1);
//     stack.push(2);
//     stack.push(3);

//     while let Some(top) = stack.pop() {
//         print!("{}", top)
//     }
// }

//#for loop
// fn main() {
//     let v = vec!['a', 'b', 'c'];

//     for (index, value) in v.iter().enumerate() {
//         println!("{} is at index {}", value, index)
//     }
// }

//#let
// fn main() {
//     let(x, y, z) = (1, 2, 3);
// }

//#함수의 매개변수
// fn print_coordinates(&(x, y): &(i32, i32)) {
//     println!("Current location:({}, {})", x, y);
// }
// fn main() {
//     let point = (3,5);
//     print_coordinates(&point);
// }

//반박가능성: 패턴이 매칭에 실패할지의 여부
//let: 반박 불가능할때만 사용가능 iflet: 반박가능해도 사용가능

//패턴 문법
//#리터럴 매칭
// fn main() {
//     let x = 1;
//     match x {
//         1 => println!("one"),
//         2 => println!("two"),
//         3 => println!("three"),
//         _ => println!("anything"),
//     }
// }

//#명명된 변수 매칭
// fn main() {
//     let x = Some(5);
//     let y = 10;

//     match x {
//         Some(50) => println!("Got 50"),
//         Some(y) => println!("matched, y = {y}"), // match scope 내 y의 값은 Some에 해당할 수 있는 모든 값으로 섀도잉됨
//         _ => println!("Default case, x = {:?}", x),
//     }
//     println!("at the end: x = {:?}, y = {:?}", x, y);
// }

//#다중패턴
// fn main() {
//     let x = 1;

//     match x {
//         1 | 2 =>println!("one or two"),
//         3 =>println!("three"),
//         _ =>println!("anything"),
//     }
// }

// ..=
// fn main() {
//     let x = 5;

//     match x {
//         1..=5 => println!("one through five"),
//         _ => println!("something else"),
//     }
// }

// fn main() {
//     let x = 'c';

//     match x {
//         'a'..='j' => println!("early ASCII letter"),
//         'k'..='z' => println!("late ASCII letter"),
//         _ => println!("something else"),
//     }
// }

//#값을 해체하여 분리
// struct Point {
//     x: i32,
//     y: i32,
// }

// fn main() {
//     let p = Point { x: 0, y: 7 };

//     let Point { x, y } = p;
//     assert_eq!(0, x);
//     assert_eq!(7, y);
// }

// fn main() {
//     let p = Point { x: 0, y: 7 };

//     match p {
//         Point { x, y: 0 } => println!("On the x axis at {x}"),
//         Point { x: 0, y } => println!("On the y axis at {y}"),

//         Point { x, y } => {
//             println!("On neither axis: ({x}, {y})")
//         }
//     }
// }

//#열거형 해체
// enum Message {
//     Quit,
//     Move { x: i32, y: i32 },
//     Write(String),
//     ChangeColor(i32, i32, i32),
// }

// fn main() {
//     let msg = Message::ChangeColor(0, 169, 255);

//     match msg {
//         Message::Quit => {
//             println!("The Quit variant has no data to destructive.")
//         }
//         Message::Move { x, y } => {
//             println!("TMove in the x direction {x} and in the y direction {y}")
//         }
//         Message::Write(text) => {
//             println!("Text message: {text}")
//         }
//         Message::ChangeColor(r, g, b) => {
//             println!("Change the color to red {r}, green {g}, blue {b}")
//         }
//     }
// }

//#중첩된 구조체, 열거형 해체
// enum Color {
//     Rgb(i32, i32, i32),
//     Hsv(i32, i32, i32),
// }

// enum Message {
//     Quit,
//     Move { x: i32, y: i32 },
//     Write(String),
//     ChangeColor(Color),
// }

// fn main() {
//     let msg = Message::ChangeColor(Color::Hsv(0, 160, 255));

//     match msg {
//         Message::ChangeColor(Color::Rgb(r, g, b)) => {
//             println!("Change color to red {r}, green {g}, blue {b}.");
//         }
//         Message::ChangeColor(Color::Hsv(h, s, v)) => {
//             println!("Change color to hue {h}, saturation {s}, value {v}.");
//         }
//         _ => (),
//     }
// }

//#구조체와 튜플 해체
// fn main() {
//     let ((feet, inches), Point{ x, y }) = ((3, 10), Point {x: 3, y: -10});
// }

//패턴에서 값 무시하기
//# _
// fn foo(_: i32, y: i32) {
//     println!("This code only uses the y parameter: {}", y)
// }

// fn main() {
//     foo(3, 4);
// }

//#중첩된 _
// fn main() {
//     let mut setting_value = Some(5);
//     let new_setting_value = Some(10);

//     match (setting_value, new_setting_value) {
//         (Some(_), Some(_)) => {
//             println!("Can't overwrite an existing customized value");
//         }
//         _ => {
//             setting_value = new_setting_value;
//         }
//     }

//     println!("setting is {:?}", setting_value)
// }

// fn main() {
//     let numbers = (2, 4, 8, 16, 32);

//     match numbers {
//         (first, _, third, _, fifth) => {
//             println!("Some numbers: {first}, {third}, {fifth}");
//         }
//     }
// }

//#사용하지 않는 변수는 변수 이름앞에 _를 붙여서 오류무시(값이 바인딩되지않음)

//# ..
// struct Point {
//     x: i32,
//     y: i32,
//     z: i32,
// }
// fn main() {
//     let origin = Point { x: 0, y: 0, z: 0 };

//     match origin {
//         Point { x, .. } => println!("x is {}", x),
//     }
// }

//매치가드

// fn main() {
//     let num = Some(4);

//     match num {
//         Some(x) if x % 2 == 0 => println!("The number {} is even", x),
//         Some(x) => println!("The number {} is odd", x),
//         None => (),
//     }
// }

// fn main() {
//     let x = Some(5);
//     let y = 10;

//     match x {
//         Some(50) => println!("Got 50"),
//         Some(n) if n == y => println!("Matched, n = {n}"),
//         _ => println!("Defual case, x = {:?}", x),
//     }
//     println!("at the end: x = {:?}, y = {:?}", x, y)
// }

//@바인딩
enum Message {
    Hello { id: i32 },
}
fn main() {
    let msg = Message::Hello { id: 5 };

    match msg {
        Message::Hello {
            id: id_variable @ 3..=7, // match에서 ..는 사용할 수 없고 ..=만 사용가능
        } => println!("Found an id in range: {}", id_variable),
        Message::Hello { id: 10..=12 } => {
            println!("Found an id in another range")
        }
        Message::Hello { id } => println!("Found some other id: {}", id),
    }
}
