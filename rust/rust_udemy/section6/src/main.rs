//closures

// fn main() {
//     let add = |x, y| { x + y };

//     add(1,2)
// }

//threads

use std::thread;

fn main() {
    let handle = thread::sqawn(move || {
        //do stuff in a child thread
    });

    //do stuff simultaneously in the main thread

    //wait until thread has exites
    handle.join().unwrap(); // 쓰레드 실행 결과는 Result이기때문에 unwrap()
}