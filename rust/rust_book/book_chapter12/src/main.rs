//커맨드 라인 프로그램 만들기

use std::{env, process};

use book_chapter12::Config;


fn main() {
    let args: Vec<String> = env::args().collect(); // 유효하지 않은 유니코드에 대해서는 env::args_os

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}"); // 표준 에러출력: eprint!()
        process::exit(1);
    });


    if let Err(e) = book_chapter12::run(config) { // run의 Result값이 Err일 경우 e를 Err값에 바인딩
        eprintln!("Application error: {e}"); 
        process::exit(1);
    }
}

//cargo run > output.txt: 텍스트파일에 결과 저장