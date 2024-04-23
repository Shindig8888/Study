//스레드를 이용해 코드를 동시 실행
// use std::thread;
// use std::time::Duration;
// fn main() {
//     thread::spawn(|| {
//         for i in 1..10 {
//             println!("hi number {} from the spawned thread!", i);
//             thread::sleep(Duration::from_millis(1))
//         }
//     });

//     for i in 1..5 {
//         println!("hi number {} from the main thread!", { i });
//         thread::sleep(Duration::from_millis(1));
//     }
// }

//join 핸들
// use std::thread;
// use std::time::Duration;
// fn main() {
//     let handle = thread::spawn(|| {
//         for i in 1..10 {
//             println!("hi number {} from the spawned thread!", i);
//             thread::sleep(Duration::from_millis(1))
//         }
//     });
//     handle.join().unwrap();
//     for i in 1..5 {
//         println!("hi number {} from the main thread!", { i });
//         thread::sleep(Duration::from_millis(1));
//     }

// }

//move 클로저

// use std::thread;

// fn main() {
//     let v = vec![1,2,3];

//     let handle = thread::spawn(move || {
//         println!("Here's a vector: {:?}", v);

//     });
//     handle.join().unwrap();
// }

//메시지 패싱
// use std::sync::mpsc;
// use std::thread;

// fn main() {
//     let (tx, rx) = mpsc::channel();

//     thread::spawn(move || {
//         let val = String::from("hi");
//         tx.send(val).unwrap();
//     });

//     let received = rx.recv().unwrap();
//     println!("Got {}", received);
// }

//채널과 소유권 이동
// use std::sync::mpsc;
// use std::thread;

// fn main() {
//     let (tx, rx) = mpsc::channel();

//     thread::spawn(move || {
//         let val = String::from("hi");
//         tx.send(val).unwrap();
//         println!("val is {}", val);
//     });

//     let received = rx.recv().unwrap();
//     println!("Got {}", received);
// }

//여러값 보내기와 수신자가 기다리는지 알아보기
// use std::sync::mpsc;
// use std::thread;
// use std::time::Duration;

// fn main() {
//     let (tx, rx) = mpsc::channel();

//     thread::spawn(move || {
//         let vals = vec![
//             String::from("hi"),
//             String::from("from"),
//             String::from("the"),
//             String::from("thread"),
//         ];
//         for val in vals {
//             tx.send(val).unwrap();
//             thread::sleep(Duration::from_secs(1))
//         }
//     });

//     for received in rx { // 기다림
//         println!("Got {}", received);
//     }
// }

//송신자 복제
// use std::sync::mpsc;
// use std::thread;
// use std::time::Duration;

// fn main() {
//     let (tx, rx) = mpsc::channel();

//     let tx1 = tx.clone();
//     thread::spawn(move || {
//         let vals = vec![
//             String::from("hi"),
//             String::from("from"),
//             String::from("the"),
//             String::from("thread"),
//         ];
//         for val in vals {
//             tx.send(val).unwrap();
//             thread::sleep(Duration::from_secs(1))
//         }
//     });

//     thread::spawn(move || {
//         let vals = vec![
//             String::from("more"),
//             String::from("messages"),
//             String::from("for"),
//             String::from("you"),
//         ];
//         for val in vals {
//             tx1.send(val).unwrap();
//             thread::sleep(Duration::from_secs(1))
//         }
//     });

//     for received in rx {
//         // 기다림
//         println!("Got {}", received);
//     }
// }

//공유 상태 동시성
// use std::sync::Mutex;

// fn main() {
//     let m = Mutex::new(5);

//     {
//         let mut num = m.lock().unwrap();
//         *num = 6;
//     }

//     println!("m = {:?}", m);
// }

//여러 스레드 사이에서 Mutex<T> rhddb
// use std::rc::Rc;
// use std::sync::Mutex;
// use std::thread;

// fn main() {
//     let counter = RC::new(Mutex::new(0));
//     let mut handles = vec![];

//     for _ in 0..10 {
//         let counter = Rc::clone(&counter);
//         let handle = thread::spawn(move ||{
//             let mut num = counter.lock().unwrap();

//             *num += 1;
//         });

//         handles.push(handle);
//     }

//     for handle in handles {
//         handle.join().unwrap();
//     }

//     println!("Result: {}", *counter.lock().unwrap());
// }

//Arc<T>

// use std::sync::{Arc, Mutex};
// use std::thread;

// fn main() {
//     let counter = Arc::new(Mutex::new(0));
//     let mut handles = vec![];

//     for _ in 0..10 {
//         let counter = Arc::clone(&counter);
//         let handle = thread::spawn(move || {
//             let mut num = counter.lock().unwrap();

//             *num += 1
//         });

//         handles.push(handle);
//     }
//     for handle in handles {
//         handle.join().unwrap();
//     }
//     println!("Result: {}", *counter.lock().unwrap());

// }

//Send와 Sync는 이후 학습
