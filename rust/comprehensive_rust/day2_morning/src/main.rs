//match
// fn main() {
//     let input = '0';
//     match input {
//         'q' => println!("Quitting"),
//         'a' | 's' | 'w' | 'd' => println!("이리저리 이동"),
//         '0'..='9' => println!("숫자입력"),
//         key if key.is_lowercase() => println!("소문자: {key}"),
//         _ => println!("기타"),
//     }
// }

//열거형 분해(역구조화)
// struct Foo {
//     x: (u32, u32),
//     y: u32,
// }

// fn main() {
//     let foo = Foo { x: (5, 2), y: 4 };
//     match foo {
//         Foo { x: (1, b), y } => println!("x.0 = 1, b = {b}, y = {y}"),
//         Foo { y: 2, x: i } => println!("y = 2, x = {i:?}"),
//         Foo { y, .. } => println!("y = {y}, 다른 필드는 무시됨"),
//     }
// }

// enum Result {
//     Ok(i32),
//     Err(String),
// }

// fn divide_in_two(n: i32) -> Result {
//     if n % 2 == 0 {
//         Result::Ok(n / 2)
//     } else {
//         Result::Err(format!("{n}을(를) 두 개의 동일한 부분으로 나눌 수 없음"))
//     }
// }

// fn main() {
//     let n = 99;
//     match divide_in_two(n) {
//         Result::Ok(half) => println!("{n}을(를) 둘로 나눈 값은 {half} 입니다."),
//         Result::Err(msg) => println!("죄송합니다. 오류가 발생했습니다, {msg}"),
//     }
// }

//if let
// fn sleep_for(secs:f32) {
//     let dur = if let Ok(dur) = std::time::Duration::try_from_secs_f32(secs) {
//         dur
//     } else {
//         std::time::Duration::from_millis(500)
//     };
//     std::thread::sleep(dur);
//     println!("{:?} 동안 잠들었습니다.", dur)
// }

// fn main() {
//     sleep_for(-10.0);
//     sleep_for(0.8);
// }

//let else expression
// fn hex_or_die_trying(maybe_string: Option<String>) -> Result<u32, String> {
//     let s = if let Some(s) = maybe_string {
//         s
//     } else {
//         return Err(String::from("None을 가져옴"));
//     };

//     let first_byte_char = if let Some(first_byte_char) = s.chars().next() {
//         first_byte_char
//     } else {
//         return Err(String::from("got empty string"));
//     };

//     if let Some(digit) = first_byte_char.to_digit(16) {
//         Ok(digit)
//     } else {
//         Err(String::from("16 진수가 아님"))
//     }
// }

// fn main() {
//     println!("결과: {:?}", hex_or_die_trying(Some(String::from("foo"))))
// }

// fn main() {
//     let mut name = String::from("Comprehensive Rust");
//     while let Some(c) = name.pop() {
//         println!("character: {c}");
//     }
// }

//let else
// fn hex_or_die_trying(maybe_string: Option<String>) -> Result<u32, String> {
//     let Some(s) = maybe_string else {
//         return Err(String::from("None을 가져옴"));
//     };

//     let Some(first_byte_char) = s.chars().next() else {
//         return Err(String::from("got empty string"));
//     };

//     let Some(digit) = first_byte_char.to_digit(16) else {
//         Err(String::from("16 진수가 아님"))
//     };

//     return Ok(digit);
// }

//연습문제: 표현식 평가
/// An operation to perform on two subexpressions.
// #[derive(Debug)]
// enum Operation {
//     Add,
//     Sub,
//     Mul,
//     Div,
// }

// /// An expression, in tree form.
// #[derive(Debug)]
// enum Expression {
//     /// An operation on two subexpressions.
//     Op {
//         op: Operation,
//         left: Box<Expression>,
//         right: Box<Expression>,
//     },

//     /// A literal value
//     Value(i64),
// }

// fn eval(e: Expression) -> Result<i64, String> {
//     match e {
//         Expression::Value(n) => Ok(n),
//         Expression::Op { op, left, right } => {
//             let left_value = eval(*left)?;
//             let right_value = eval(*right)?;
//             match op {
//                 Operation::Add => Ok(left_value + right_value),
//                 Operation::Sub => Ok(left_value - right_value),
//                 Operation::Mul => Ok(left_value * right_value),
//                 Operation::Div if right_value != 0 => Ok(left_value / right_value),
//                 Operation::Div => Err(String::from("division by zero")),
//             }
//         }
//     }
// }

// #[test]
// fn test_value() {
//     assert_eq!(eval(Expression::Value(19)), Ok(19));
// }

// #[test]
// fn test_sum() {
//     assert_eq!(
//         eval(Expression::Op {
//             op: Operation::Add,
//             left: Box::new(Expression::Value(10)),
//             right: Box::new(Expression::Value(20)),
//         }),
//         Ok(30)
//     );
// }

// #[test]
// fn test_recursion() {
//     let term1 = Expression::Op {
//         op: Operation::Mul,
//         left: Box::new(Expression::Value(10)),
//         right: Box::new(Expression::Value(9)),
//     };
//     let term2 = Expression::Op {
//         op: Operation::Mul,
//         left: Box::new(Expression::Op {
//             op: Operation::Sub,
//             left: Box::new(Expression::Value(3)),
//             right: Box::new(Expression::Value(4)),
//         }),
//         right: Box::new(Expression::Value(5)),
//     };
//     assert_eq!(
//         eval(Expression::Op {
//             op: Operation::Add,
//             left: Box::new(term1),
//             right: Box::new(term2),
//         }),
//         Ok(85)
//     );
// }

// #[test]
// fn test_error() {
//     assert_eq!(
//         eval(Expression::Op {
//             op: Operation::Div,
//             left: Box::new(Expression::Value(99)),
//             right: Box::new(Expression::Value(0)),
//         }),
//         Err(String::from("division by zero"))
//     );
// }

// trait Animal {
//     fn leg_count(&self) -> u32;
// }

// trait Pet: Animal {
//     fn name(&self) -> String;
// }

// struct Dog(String);

// impl Animal for Dog {
//     fn leg_count(&self) -> u32 {
//         4
//     }
// }

// impl Pet for Dog {
//     fn name(&self) -> String {
//         self.0.clone()
//     }
// }

// fn main() {
//     let puppy = Dog(String::from("렉스"));
//     println!("{} has {} legs", puppy.name(), puppy.leg_count());
// }

// #[derive(Debug)]
// struct Meters(i32);
// #[derive(Debug)]
// struct MetersSquared(i32);

// trait Multiply {
//     type Output;
//     fn multipy(&self, other: &Self) -> Self::Output;
// }

// impl Multiply for Meters {
//     type Output = MetersSquared;
//     fn multipy(&self, other: &Self) -> Self::Output {
//         MetersSquared(self.0 * other.0)
//     }
// }

// fn main() {
//     println!("{:?}", Meters(10).multipy(&Meters(20)))
// }

//연습문제: 일반 min
// use std::fmt::Display;

// pub trait Logger {
//     /// Log a message at the given verbosity level.
//     fn log(&self, verbosity: u8, message: impl Display);
// }

// struct StderrLogger;

// impl Logger for StderrLogger {
//     fn log(&self, verbosity: u8, message: impl Display) {
//         eprintln!("verbosity={verbosity}: {message}");
//     }
// }

// fn do_things(logger: &impl Logger) {
//     logger.log(5, "FYI");
//     logger.log(2, "Uhoh");
// }

// struct VerbosityFilter {
//     max_verbosity: u8,
//     inner: StderrLogger,
// }

// impl Logger for VerbosityFilter {
//     fn log(&self, verbosity: u8, message: impl Display) {
//         if verbosity <= self.max_verbosity {
//             self.inner.log(verbosity, message)
//         }
//     }
// }

// // TODO: Define and implement `VerbosityFilter`.

// fn main() {
//     let l = VerbosityFilter {
//         max_verbosity: 3,
//         inner: StderrLogger,
//     };
//     do_things(&l);
// }

//제네릭타입
// fn pick<T>(n: i32, even: T, odd: T) -> T {
//     if n % 2 == 0 {
//         even
//     } else {
//         odd
//     }
// }

// fn main() {
//     println!("선택한 숫자:{:?}", pick(97, 222, 333))
// }
use std::cmp::Ordering;

fn min<T: PartialOrd + Copy>(a: T, b: T) -> T {
    if a < b {
        a
    } else {
        b
    }
}

// TODO: implement the `min` function used in `main`.

fn main() {
    assert_eq!(min(0, 10), 0);
    assert_eq!(min(500, 123), 123);

    assert_eq!(min('a', 'z'), 'a');
    assert_eq!(min('7', '1'), '1');

    assert_eq!(min("hello", "goodbye"), "goodbye");
    assert_eq!(min("bat", "armadillo"), "armadillo");
}
