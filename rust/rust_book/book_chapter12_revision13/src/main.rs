//커맨드 라인 수정(클로저)

use std::{env, process};

use book_chapter12_revision13::Config;


fn main() {
    // let args: Vec<String> = env::args().collect(); // 유효하지 않은 유니코드에 대해서는 env::args_os // 를 사용하는 대신 config의 build()에 env::args() 이터레이터를 직접 넘김

    let config = Config::build(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}"); // 표준 에러출력: eprint!()
        process::exit(1);
    });


    if let Err(e) = book_chapter12_revision13::run(config) { // run의 Result값이 Err일 경우 e를 Err값에 바인딩
        eprintln!("Application error: {e}"); 
        process::exit(1);
    }
}

//cargo run > output.txt: 텍스트파일에 결과 저장