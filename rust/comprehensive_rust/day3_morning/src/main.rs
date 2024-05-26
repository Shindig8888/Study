//ownership
// struct Point(i32, i32);
// fn main() {
//     {
//         let p = Point(3, 4);
//         println!("x: {}", p.0);
//     }
//     println!("y:{}", p.1);
// }

//move
// fn main() {
//     let s1: String = String::from("hello!");
//     let s2: String = s1;
//     println!("s2: {s2}");
// }

// fn say_hello(name:String) {
//     println!("안녕하세요 {name}");
// }

// fn main() {
//     let name = String::from("Alice");
//     say_hello(name);
// }

//clone
// #[derive(Default)]
// struct Backends {
//     hostnames: Vec<String>,
//     weights: Vec<f64>,
// }

// impl Backends {
//     fn set_hostnames(&mut self, hostnames: &Vec<String>) {
//         self.hostnames = hostnames.clone();
//         self.weights = hostnames.iter().map(|_| 1.0).collect();
//     }
// }

//복합타입
// fn main() {
//     let x = 42;
//     let y = x;
//     println!("x:{x}");
//     println!("y:{y}");
// }

// #[derive(Copy, Clone, Debug)]
// struct Point(i32, i32);

// fn main() {
//     let p1 = Point(3, 4);
//     let p2 = p1;
//     println!("p1: {p1:?}");
//     println!("p2: {p2:?}");
// }

//Drop

// struct Droppable {
//     name: &'static str,
// }

// impl Drop for Droppable {
//     fn drop(&mut self) {
//         println!("{} 삭제 중", self.name);
//     }

// }

// fn main() {
//     let a = Droppable {name: "a"};
//     {
//         let b = Droppable {name: "b"};
//         {
//             let c = Droppable {name: "c"};
//             let d = Droppable {name: "d"};
//             println!("B블록에서 나가기");
//         }
//         println!("A블록에서 나가기");
//     }
//     drop(a);
//     println!("main블록에서 나가기");
// }

//연습문제: 빌드 타입

// #[derive(Debug)]
// enum Language {
//     Rust,
//     Java,
//     Perl,
// }

// #[derive(Clone, Debug)]
// struct Dependency {
//     name: String,
//     version_expression: String,
// }

// /// A representation of a software package.
// #[derive(Debug)]
// struct Package {
//     name: String,
//     version: String,
//     authors: Vec<String>,
//     dependencies: Vec<Dependency>,
//     language: Option<Language>,
// }

// impl Package {
//     /// Return a representation of this package as a dependency, for use in
//     /// building other packages.
//     fn as_dependency(&self) -> Dependency {
//         Dependency {
//             name: self.name.clone(),
//             version_expression: self.version.clone(),
//         }
//     }
// }

// /// A builder for a Package. Use `build()` to create the `Package` itself.
// struct PackageBuilder(Package);

// impl PackageBuilder {
//     fn new(name: impl Into<String>) -> Self {
//        Self(Package{
//         name: name.into(),
//         version: "0.1".into(),
//         authors: vec![],
//         dependencies: vec![],
//         language: None,
//        })
//     }

//     /// Set the package version.
//     fn version(mut self, version: impl Into<String>) -> Self {
//         self.0.version = version.into();
//         self
//     }

//     /// Set the package authors.
//     fn authors(mut self, authors: Vec<String>) -> Self {
//         self.0.authors = authors;
//         self
//     }

//     /// Add an additional dependency.
//     fn dependency(mut self, dependency: Dependency) -> Self {
//         self.0.dependencies.push(dependency);
//         self
//     }

//     /// Set the language. If not set, language defaults to None.
//     fn language(mut self, language: Language) -> Self {
//         self.0.language = Some(language);
//         self
//     }

//     fn build(self) -> Package {
//         self.0
//     }
// }

// fn main() {
//     let base64 = PackageBuilder::new("base64").version("0.13").build();
//     println!("base64: {base64:?}");
//     let log =
//         PackageBuilder::new("log").version("0.4").language(Language::Rust).build();
//     println!("log: {log:?}");
//     let serde = PackageBuilder::new("serde")
//         .authors(vec!["djmitche".into()])
//         .version(String::from("4.0"))
//         .dependency(base64.as_dependency())
//         .dependency(log.as_dependency())
//         .build();
//     println!("serde: {serde:?}");
// }

//Box
// #[derive(Debug)]
// enum List<T> {
//     Element(T, Box<List<T>>),
//     Nil,
// }

// fn main() {
//     let list: List<i32> =
//         List::Element(1, Box::new(List::Element(2, Box::new(List::Nil))));
//     println!("{list:?}")
// }

//Rc
// use std::rc::Rc;

// fn main() {
//     let a = Rc::new(10);
//     let b = Rc::clone(&a);

//     println!("a = {a}");
//     println!("b = {b}");
// }

//트레잇 객체

// struct Dog {
//     name: String,
//     age: i8,
// }

// struct Cat {
//     lives: i8,
// }

// trait Pet {
//     fn talk(&self) -> String;
// }

// impl Pet for Dog {
//     fn talk(&self) -> String {
//         format!("멍멍, 제 이름은 {}입니다.", self.name)
//     }
// }

// impl Pet for Cat {
//     fn talk(&self) -> String {
//         String::from("냐옹!")
//     }
// }

// fn main() {
//     let pets: Vec<Box<dyn Pet>> = vec![
//         Box::new(Cat { lives: 9 }),
//         Box::new(Dog {
//             name: String::from("Fido"),
//             age: 5,
//         }),
//     ];
//     for pet in pets {
//         println!("Hello, who are you? {}", pet.talk());
//     }
// }

//연습문제: 바이너리 트리

use std::cmp::Ordering;

/// A node in the binary tree.
#[derive(Debug)]
struct Node<T: Ord> {
    value: T,
    left: Subtree<T>,
    right: Subtree<T>,
}

/// A possibly-empty subtree.
#[derive(Debug)]
struct Subtree<T: Ord>(Option<Box<Node<T>>>);

/// A container storing a set of values, using a binary tree.
///
/// If the same value is added multiple times, it is only stored once.
#[derive(Debug)]
pub struct BinaryTree<T: Ord> {
    root: Subtree<T>,
}

impl<T: Ord> BinaryTree<T> {
    fn new() -> Self {
        Self {
            root: Subtree::new(),
        }
    }

    fn insert(&mut self, value: T) {
        self.root.insert(value);
    }

    fn has(&self, value: &T) -> bool {
        self.root.has(value)
    }

    fn len(&self) -> usize {
        self.root.len()
    }
}

impl<T: Ord> Subtree<T> {
    fn new() -> Self {
        Self(None)
    }

    fn insert(&mut self, value: T) {
        match &mut self.0 {
            None => self.0 = Some(Box::new(Node::new(value))),
            Some(n) => match value.cmp(&n.value) {
                Ordering::Less => n.left.insert(value),
                Ordering::Equal => {}
                Ordering::Greater => n.right.insert(value),
            },
        }
    }

    fn has(&self, value: &T) -> bool {
        match &self.0 {
            None => false,
            Some(n) => match value.cmp(&n.value) {
                Ordering::Less => n.left.has(value),
                Ordering::Equal => true,
                Ordering::Greater => n.right.has(value),
            },
        }
    }

    fn len(&self) -> usize {
        match &self.0 {
            None => 0,
            Some(n) => 1 + n.left.len() + n.right.len(),
        }
    }
}

impl<T: Ord> Node<T> {
    fn new(value: T) -> Self {
        Self {
            value,
            left: Subtree::new(),
            right: Subtree::new(),
        }
    }
}

fn main() {
    let mut tree = BinaryTree::new();
    tree.insert("foo");
    assert_eq!(tree.len(), 1);
    tree.insert("bar");
    assert!(tree.has(&"foo"));
}
// Implement `new`, `insert`, `len`, and `has` for `Subtree`.

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn len() {
        let mut tree = BinaryTree::new();
        assert_eq!(tree.len(), 0);
        tree.insert(2);
        assert_eq!(tree.len(), 1);
        tree.insert(1);
        assert_eq!(tree.len(), 2);
        tree.insert(2); // not a unique item
        assert_eq!(tree.len(), 2);
    }

    #[test]
    fn has() {
        let mut tree = BinaryTree::new();
        fn check_has(tree: &BinaryTree<i32>, exp: &[bool]) {
            let got: Vec<bool> = (0..exp.len()).map(|i| tree.has(&(i as i32))).collect();
            assert_eq!(&got, exp);
        }

        check_has(&tree, &[false, false, false, false, false]);
        tree.insert(0);
        check_has(&tree, &[true, false, false, false, false]);
        tree.insert(4);
        check_has(&tree, &[true, false, false, false, true]);
        tree.insert(4);
        check_has(&tree, &[true, false, false, false, true]);
        tree.insert(3);
        check_has(&tree, &[true, false, false, true, true]);
    }

    #[test]
    fn unbalanced() {
        let mut tree = BinaryTree::new();
        for i in 0..100 {
            tree.insert(i);
        }
        assert_eq!(tree.len(), 100);
        assert!(tree.has(&50));
    }
}
