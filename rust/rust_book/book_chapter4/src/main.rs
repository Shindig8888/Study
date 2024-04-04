//#### 소유권 이해하기 ####

//### 소유권?
// 가비지 컬렉션 = 더 이상 사용하지 않는 메모리를 정기적으로 찾는 방식
// 다른언어 = 프로그래머가 직접 명시적으로 메모리 할당
//러스트: 소유권이라는 시스템을 만들고, 컴파일 중 컴파일러 규칙을 정해 메모리 관리

//$ 힙과 스택
//스택은 값이 들어온 순서대로 저장, 역순으로 제거, 후입선출
//힙 > 데이터를 힙에 넣을 때 먼저 저장할 공간이 있는지 운영체제에 물어봄, 메모리할당자는 커다란 힙 영역에서 빈 지점 할당, 힙에 대한 포인터는 스택에 저장(위치정보만)
// 스택이 힙보다 빠름

//##소유권 규칙
//#변수의 스코프
// //let s = "Hello";
// 변수가 선언된 시점부터 스코프를 벗어날 때 까지 문자열 리터럴 값이 유효

//#String 타입
//input으로 받는 문자열 ==> 문자열의 크기를 알 수 없음.
//따라서 String타입은 힙에 할당됨
// //let s = String::from("Hello");
//String은 mutable로 사용할 수 있음
// //let mut s = String::from("hello");
// //s.push_str(", world!");
// //println!({}, s)

// ##메모리와 할당
// String은 힙에 메모리를 할당하기 때문에 실행 중 메모리 할당자로부터 메모리를 요청해야 하고(String::from()), 
// 사용을 마쳤을 때 메모리를 해체할 방법이 필요(스코프를 벗어나는 순간 자동 해체; drop()
// String 값을 복사할 때, 스택만 복사되고 힙은 복사되지않음
// 문제는 이 복사된 String들이 메모리에서 해체될 때, 중복해체 에러가 발생; 
 // 따라서 같은 힙 값을 가지는 중복된 s1, s2이 있고, s1이 먼저 선언되었다면 s2가 선언된 이후로는 s1값은 유효하지 않음; 이동!
 // String의 힙 데이터까지 복사하고 싶을때는 .clone() 사용=>다른 일이 수행될 것을 알려주는 시각적인 표시이기도 함

 // 정수형은 모두 스택에 저장되기 때문에 차이없음
 // Copy 트레이트트가 구현되어있다면 이동되지않고 복사됨
  // 모든정수형 타입, bool, 부동소수점타입, char, copy가능한 튜플

// // #소유권과 함수
// fn main(){
//     let s = String::from("hello"); // String값이 s로 할당

//     takes_ownership(s); // 함수로 s가 이동, s는 더이상 유효하지 않음

//     let x = 5; // x가 scpoe안으로 들어옴

//     makes_copy(x); // x는 이동이 아니라 Copy이므로 x 유효

// } // 스코프를 벗어나 s의 메모리가 해체되어야하지만, 함수로 이동했으므로 아무것도 일어나지 않음

// fn takes_ownership(some_str:String){
//     println!("{}", some_str);
// } // some_string이 스코프 밖으로 벗어니고 drop 호출

// 소유권은 값을 반환하는 과정에서도 이동
// 함수를 통해 소유권을 돌려주는건 가능하지만 일반적이지않음

// ##참조와 대여
// fn main() {
//     let s1 = String::from("hello");
//     let len = calculate_length(&s1); // &s1이기 때문에 s1의 참조자, s1은 이동하지 않음 ==> 대여
//     println!("The length of '{}' is {}", s1, len);
// }

// fn calculate_length(s: &String) -> usize { // &String, 참조자를 받는걸 명시 s(&s1)->s1->힙데이터
//     s.len()
// }

//# 가변 참조자
// fn main() {
//     let mut s1 = String::from("hello");
//     change(&mut s1); 
// }

// fn change(some_string: &mut String) { 
//     some_string.push_str(", world")
// }
//어떤 값에 대한 가변 참조자가 있으면 다른 어떤 참조자도 같은 스코프안에 존재할 수 없음


//##댕글링 참조
// fn main(){
//     let refrerence_to_nothing = dangle();

// }
// fn dangle ()->&String { //참조자 반환
//     let s = String::from("hello");

//     &s //참조자 리턴
// } // 스코프를 벗어나 s가 버려짐, 메모리 해제, 참조할 것이 없음


//## 슬라이스
//#컬렉션의 일부를 참조, 소유권을 가지지 않음

// fn first_word(s: &String) -> usize {
//     let bytes = s.as_bytes(); // String을 byte단위로 쪼갬
//     for (i, &item) in bytes.iter().enumerate() { // 반목자를 iter()로 생성
//         //&item으로 iter().enumerate()에서 얻은 요소의 참조자를 설정
//         if item == b' ' {
//             return i; // 에러발생, 리턴타입은 String이 아니라 &String
//         }
//     }
// }

//#문자열 슬라이스
// let s = String::from("hello world");

// let hello = &s[0..5];
// let world = &[6..11];


fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes(); 
    for (i, &item) in bytes.iter().enumerate() { 
        if item == b' ' {
            return &s[0..1]; 
        }s
    }

&s[..]
}