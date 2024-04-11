// 컬렉션 : 여러 개 값을 포함하는 힙에 저장되는 데이터

// 벡터
//let v: Vec<i32> = Vec::new();
//일반적으로는:
// let v = vec![1,2,3];

//벡터 업데이트
// let mut v = Vec::new();
// v.push(5);
// v.push(6);

//벡터 요소 읽기
// fn main() {
//     let v = vec![1,2,3,4,5];
//     let third: &i32 = &v[2];
//     println!("The third element is {third}");

//     let third: Option<&i32> = v.get(2); // out of bound 방지
//     match third {
//         Some(third) => println!("The third element is {third}"),
//         None => println!("There is no third element"),
//     }
// }

// //아이템의 참조자를 가지고 있는 상태에서 벡터에 새로운 요소 추가
// fn main() {
//     let mut v = vec![1,2,3,4,5];
//     let first = &v[0]; //immutable borrow occurs
//     v.push(6); //immutable borrow used
//     //참조자를 설정한 후 벡터를 변경할 수 없음, 반대는 가능
//     println!("The first element is : {first}");
// }

//벡터 반복
// fn main() {
//     let v = vec![100,32,57];
//     for i in &v {
//         println!("{i}");
//     }
// }

// fn main() {
//     let mut v = vec![100,32,57];
//     for i in &mut v {
//         *i += 2;
//     }
// }

//열거형을 이용해 여러 타입 저장

// fn main() {
//     enum SpreadsheetCell {
//         Int(i32),
//         Float(f64),
//         Text(String),
//     }

//     let low = vec![
//         SpreadsheetCell::Int(3),
//         SpreadsheetCell::Text(String::from("Blue")),
//         SpreadsheetCell::Float(10.12),
//     ];
// }

// 벡터가 버려지면 벡터의 요소도 버려짐 =>> 정수일경우에도 버려짐

// // String
// let mut s = String::new(); // 빈 문자열 생성

// let data = "initial contensts";
// let s  = data.to_string();

// let s = "initial contents".to_string();
// let s = String::from("initial contens"); // 위 세가지 방법은 동일한 방법 수행

//문자열 업데이트하기

// fn main(){
//     let mut s = String::from("foo");
//     s.push_str("bar"); // 업데이트는 소유권을 가져오지않음
//     println!("{s}")
// }

// fn main() {
//     let mut s1 = String::from("foo");
//     let s2 = "bar";
//     s1.push_str(s2); // 소유권을 가져가지 않음
//     println!("s2 is {s2}");
// }

// fn main() {
//     let mut s = String::from("lo");
//     s.push('l'); // 캐릭터일경우에는 push
// }


//+연산자, 매크로

// fn main() {
//     let s1 = String::from("Hello");
//     let s2 = String::from("world");
//     let s3 = s1+&s2; // +를 사용할때는 첫번째 문자열은 참조자x, 이후 참조자를 이용

//     println!("{s3}")
// }

//format! 매크로

// fn main() {
//     let s1 = String::from("tic");
//     let s2 = String::from("tac");
//     let s3 = String::from("toe");

//     let s = format!("{s1}-{s2}-{s3}"); // 소유권이전없이 문자열 합치기
//     println!("{s1}, {s2}, {s3}, {s}");

// }

//문자열 내부의 인덱싱
//유니코드의 경우 인덱싱:
// let hello = "안녕하세요";
// let answer = &hell0[0];
// 과 같은 포멧을 지원하지않음. []속의 숫자는 바이트를 서치하는 것

//문자열 슬라이싱하기
// fn main() {
//     let hello = "안녕하세요";
//     let s = &hello[0..6]; // 한국어는 한글자가 3바이트이므로 3의배수가 아니라면 패닉
//     println!("{s}")
// }

//문자열 반복을 위한 메서드

// fn main() {
//     for c in "안녕".chars() { // .chars()는 문자열을 ch itter로 변환
//         println!("{c}");
//     }
// }

// fn main() {
//     for c in "안녕".bytes() { // .bytes()는 문자열을 bytes itter로 변환
//         println!("{c}");
//     }
// }

//해시맵 => 라이브러리:
// use std::collections::HashMap;
// fn main() {
//     let mut scores = HashMap::new();

//     scores.insert(String::from("Blue"), 10);
//     scores.insert(String::from("Yellow"), 50); // 키와 밸류 설정
    
// }

// 해시맵의 값 접근

// use std::collections::HashMap;

// fn main() {
//     let mut scores = HashMap::new();
//     scores.insert(String::from("Blues"), 10);
//     scores.insert(String::from("Yellow"), 50);

//     let team_name = String::from("Blue");
//     let score = scores.get(&team_name).copied().unwrap_or(0); // copied: &Option이 아닌 Option을 가져옴, unwrap_or: scores가 해당 키를 가지고있지 않을 경우 score = 0
// }

// use std::collections::HashMap;

// fn main() {
//     let mut scores = HashMap::new();

//     scores.insert(String::from("Blue"), 10);
//     scores.insert(String::from("Yellow"), 50);

//     for (key, value) in &scores {
//         println!("{key}: {value}");
//     }
// }

// 해시 맵과 소유권

// use std::collections::HashMap;

// fn main() {
//     let field_name = String::from("Favorite color");
//     let field_value = String::from("Blue");

//     let mut map = HashMap::new();
//     map.insert(field_name, field_value); // field_name과 field_value는 더이상 유효하지않음
//     println!("{map}")

// }

//해시 맵 업데이트

//값 덮어쓰기

// use std::collections::HashMap;

// fn main() {
//     let mut scores = HashMap::new();

//     scores.insert(String::from("Blue"), 10);
//     scores.insert(String::from("Blue"), 50); // key값을 동일하게 설정하여 값 업데이트

//     println!("{:?}", scores);

// }

//키가 없을때만 키와 값 추가하기

// use std::collections::HashMap;

// fn main() {
//     let mut scores = HashMap::new();
//     scores.insert(String::from("Blue"), 10);

//     scores.entry(String::from("Yellow")).or_insert(50); // entry()로 "Yello" 값을 넣고, 해시맵에 key가 있는지 확인, 없으면 or_insert()로 밸류 투입
//     scores.entry(String::from("Blue")).or_insert(50); // 이미 Blue가 있기 때문에 pass

//     println!("{:?}", scores);
// }

// //예전 값에 기초하여 값 업데이트

// use std::collections::HashMap;

// fn main() {
//     let text = "hello world wonderful world";
//     let mut map = HashMap::new();

//     //split_whitespace()는 텍스트를 화이트스페이스를 기준으로 iterate
//     for word in text.split_whitespace() {
//         let count = map.entry(word).or_insert(0); // count: 생성된 key, value 중 value에 해당하는 가변참조자!!!
//         *count += 1; // *이미 key값이 있을 때 역참조, 가변참조자의 값을 변환해 기초값 수정
//     }
//     println!("{:?}", map);
// } // 해시맵의 반복처리는 임의로 일어남


//과제

//1. 정수리스트가 주어졌을 때 벡터를 사용하여 중간값, 최빈값 구하기

//중간값
// fn main() {
//     let v = vec![1,2,3,4,5,6,7,8];
//     let length = &v.len();
//     if length % 2 == 0 {
//         let median = (&v[length/2 -1] + &v[length/2]) as f64 / 2.0 ;
//         println!("{median}");
//         } else {
//         let median = &v[length/2];
//         println!("{median}");
//         };
//     }

//최빈값(gpt 도움)
// use std::collections::HashMap;

// fn finding_max(numbers:Vec<i32>) ->Option<i32> {
//     let mut count_map = HashMap::new();

//     for &number in &numbers {
//         let count = count_map.entry(number).or_insert(0);
//         *count+= 1;
//     }

//     let mut mode = None;
//     let mut max_count = 0;
//     for (num, count) in count_map {
//         if count > max_count {
//             mode = Some(num);
//             max_count = count;
//         }
    
//     }
//     mode
// }

// fn main() {
//     let numbers = vec![1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5];
//     if let Some(mode) = finding_max(numbers) {
//         println!("최빈값: {}", mode);
//     } else {
//         println!("최빈값이 없습니다.");
//     }
// }

//2. 피그 라틴(qpt도움)
// use std::io;

// fn pig_latin(sentence: &str) -> String {
//     let mut result = String::new();
//     for word in sentence.split_whitespace() {
//         let first_char = word.chars().next().unwrap(); // 단어의 첫 글자를 가져옵니다.
//         if "aeiou".contains(first_char) {
//             result.push_str(&format!("{}-hay ", word)); // 모음으로 시작하는 경우 "-hay"를 추가합니다.
//         } else {
//             let pig_latin_word = format!("{}-{}ay ", &word[1..], first_char); // 자음으로 시작하는 경우 첫 글자를 단어의 끝으로 옮기고 "-ay"를 추가합니다.
//             result.push_str(&pig_latin_word);
//         }
//     }
//     result
// }

// fn main() {
//     let mut input_string = String::new();

//     println!("문자열을 입력하세요:");
//     io::stdin().read_line(&mut input_string)
//         .expect("표준 입력에서 읽어들이는 데 실패했습니다.");

//     let pig_latin_result = pig_latin(&input_string.trim());

//     println!("입력한 문자열의 Pig Latin 변환 결과: {}", pig_latin_result);
// }

// // 3. 부서 이름 추가(나중에 다시 할 것)

// use std::io;
// use std::collections::HashMap;

// fn main() {
//     let mut input_string = String::new();

//     println!("명령어 혹은 summary를 입력하세요:");
//     io::stdin().read_line(&mut input_string)
//         .expect("표준 입력에서 읽어들이는 데 실패했습니다.");

//     let mut table = HashMap::new();
//     table.insert(String::from("Name"), String::from("Department"));

//     let words : Vec<&str> = input_string.split_whitespace().collect();

//     if let Some(name) = words.get(1) {
//         if let Some(department) = words.get(3) {
//             table.insert(name.to_string(), department.to_string());
//         }
//     } else if words.get(0).map_or("", |s| *s) == "summary" {
//         println!("{:?}", table);
//     } else {
//         println!("명령어가 올바르지 않습니다.")
//     }
// }
