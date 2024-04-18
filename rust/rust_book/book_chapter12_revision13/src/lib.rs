use std::error::Error;
use std::{fs, env};


pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}

impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>, //타입을 String을 반환하는 이터레이터로 명시
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a pile path")
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();


        Ok(Config { query, file_path, ignore_case, })
    }
}

// IGNORE_CASE=1 cargo run to poem.txt // rust bash에서
// $Env:IGNORE_CASE=1; cargo run -- to poem.txt // powercell에서



pub fn run(config: Config) -> Result<(), Box<dyn Error>>{
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }
    Ok(())
}

pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> { // 결과물이 contents만큼 오래 살아있어야함
    // let mut results = Vec::new();

    // for line in contents.lines() {
    //     if line.contains(query) {
    //         results.push(line);
    //     }
    // }
    // results
    contents
        .lines() // 각 라인을 이터레이터로
        .filter(|line|line.contains(query))// 클로저
        .collect() // 가공된 이터레이터를 벡터로 변환하여 리턴
}

pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.to_lowercase().contains(&query) {
            results.push(line);
        }
    }
    results
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
Safe, fast, productive.
Pick three.";

        assert_eq!(vec!["Safe, fast, productive."], search(query, contents));

    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three
Trust me.";
        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
