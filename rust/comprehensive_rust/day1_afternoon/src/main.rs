//배열
// fn main() {
//     let mut a: [i8; 10] = [42; 10];
//     a[5] = 0;
//     println!("{:?}", a)
// }

//튜플
// fn main() {
//     let t: (i8, bool) = (7, true);
//     println!("{:?}", t.0);
//     println!("{:?}", t.1);
// }

//for문은 배열반복은 지원, 튜플은 지원하지 않음

//열거형 분해

// fn print_tuple(tuple: (i32, i32)) {
//     let (left, right) = tuple;
//     println!("left: {left}, right: {right}");
// }

// struct Foo {
//     a: i32,
//     b: bool,
// }

// fn print_foo(foo: Foo) {
//     let Foo { a, b } = foo;
//     println!("a:{a}, b:{b}")
// }

// fn main() {
//     let tuple: (i32, i32) = (32, 64);
//     print_tuple(tuple);

//     let foo: Foo = Foo { a: 32, b: true };
//     print_foo(foo);
// }

//연습문제: 중첩배열

// fn main() {
//     let array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
//     let new_array = transpose(array);

//     println!("{:?}", new_array);
// }

// fn transpose(array: [[i32; 3]; 3]) -> [[i32; 3]; 3] {
//     let mut new_array = [[0; 3]; 3];

//     for i in 0..3 {
//         for j in 0..3 {
//             new_array[j][i] = array[i][j];
//         }
//     }
//     new_array
// }

//[참조]
//공유참조
// fn main() {
//     let a = 'A';
//     let b = 'B';
//     let mut r = &a;
//     println!("r: {}", *r);
//     r = &b;
//     println!("r: {}", *r);
// }

//dangling 참조
// fn main() {
//     let mut point = (1,2);
//     let x_coord = &mut point.0;
//     *x_coord = 20;
//     println!("point: {:?}", point);
// }

//연습문제: 도형
// fn magnitude(array: &[f64; 3]) -> f64 {
//     (array[0].powf(2.0) + array[1].powf(2.0) + array[2].powf(2.0)).sqrt()
// }

// fn normalize(array: &mut [f64; 3]) {
//     let size = magnitude(array);
//     *array = [array[0] / size, array[1] / size, array[2] / size];
// }

// fn main() {
//     println!("단위 벡터의 크기기: {}", magnitude(&[0.0, 1.0, 0.0]));

//     let mut v = [1.0, 2.0, 9.0];
//     println!("{v:?}의 크기: {}", magnitude(&v));
//     normalize(&mut v);
//     println!("정규화 후의 {v:?}의 크기: {}", magnitude(&v))
// }

//[사용자정의타입]
//구조체
// struct Person {
//     name: String,
//     age: u8,
// }

// fn describe(person: &Person) {
//     println!("{}은(는) {}세입니다.", person.name, person.age);
// }

// fn main() {
//     let mut peter = Person {
//         name: String::from("피터"),
//         age: 27,
//     };
//     describe(&peter);

//     peter.age = 28;
//     describe(&peter);

//     let name = String::from("에이버리");
//     let age = 39;
//     let avery = Person { name, age };
//     describe(&avery);

//     let jackie = Person {
//         name: String::from("재키"),
//         ..avery
//     };
//     describe(&jackie)
// }

//튜플
// struct Point(i32, i32);

// fn main() {
//     let p = Point(17, 23);
//     println!("({}, {})", p.0, p.1);
// }

//열거형
// #[derive(Debug)]
// enum Direction {
//     Left,
//     Right,
// }

// #[derive(Debug)]
// enum PlayerMove {
//     Pass,
//     Run(Direction),
//     Teleport { x: u32, y: u32 },
// }

// fn main() {
//     let m: PlayerMove = PlayerMove::Run(Direction::Left);
//     println!("이번 차례: {:?}", m);
// }

//const, static, type

//연습문제: 엘리베이터 이벤트

#[derive(Debug)]
enum Event {
    CarArrived(i32),
    Door_open,
    Door_close,
    Button_Preessed(Button),
}

#[derive(Debug)]
enum Button {
    LobbyCall(i32, Direction),
    CarFloor(i32),
}

#[derive(Debug)]
enum Direction {
    Up,
    Down,
}

fn car_arrived(floor: i32) -> Event {
    Event::CarArrived(floor)
}

fn car_door_opened() -> Event {
    Event::Door_open
}

fn car_door_closed() -> Event {
    Event::Door_close
}

fn lobby_call_button_pressed(floor: i32, dir: Direction) -> Event {
    Event::Button_Preessed(Button::LobbyCall(floor, dir))
}

fn car_floor_button_pressed(floor: i32) -> Event {
    Event::Button_Preessed(Button::CarFloor(floor))
}

fn main() {
    println!(
        "1층 승객이 위쪽 버튼을 눌렀습니다. {:?}",
        lobby_call_button_pressed(0, Direction::Up)
    );
    println!("엘리베이터가 1층에 도착했습니다. {:?}", car_arrived(0));
    println!("엘리베이터 문이 열렸습니다. {:?}", car_door_opened());
    println!(
        "승객이 3층 버튼을 눌렀습니다. {:?}",
        car_floor_button_pressed(3)
    );
    println!("엘리베이터 문이 닫혔습니다: {:?}", car_door_closed());
    println!("엘리베이터가 3층에 도착했습니다. {:?}", car_arrived(3));
}
