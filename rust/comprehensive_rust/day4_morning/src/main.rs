//iterator

// struct Fibonacci {
//     curr: u32,
//     next: u32,
// }

// impl Iterator for Fibonacci {
//     type Item = u32;

//     fn next(&mut self) -> Option<Self::Item> {
//         let new_next = self.curr + self.next;
//         self.curr = self.next;
//         self.next = new_next;
//         Some(self.curr)
//     }
// }

// fn main() {
//     let fib = Fibonacci { curr: 0, next: 1 };
//     for (i, n) in fib.enumerate().take(5) {
//         println!("fib({i}): {n}");
//     }
// }

//IntoIterator
// struct Grid {
//     x_coords: Vec<u32>,
//     y_coords: Vec<u32>,
// }

// impl IntoIterator for Grid {
//     type Item = (u32, u32);
//     type IntoIter = GridIter;
//     fn into_iter(self) -> GridIter {
//         GridIter {
//             grid: self,
//             i: 0,
//             j: 0,
//         }
//     }
// }

// struct GridIter {
//     grid: Grid,
//     i: usize,
//     j: usize,
// }

// impl Iterator for GridIter {
//     type Item = (u32, u32);

//     fn next(&mut self) -> Option<(u32, u32)> {
//         if self.i >= self.grid.x_coords.len() {
//             self.i = 0;
//             self.j += 1;
//             if self.j >= self.grid.y_coords.len() {
//                 return None;
//             }
//         }
//         let res = Some((self.grid.x_coords[self.i], self.grid.y_coords[self.j]));
//         self.i += 1;
//         res
//     }
// }

// fn main() {
//     let grid = Grid {
//         x_coords: vec![3, 5, 7, 9],
//         y_coords: vec![10, 20, 30, 40],
//     };
//     for (x, y) in grid {
//         println!("point = {x}, {y}")
//     }
// }

//FromIterator
// fn main() {
//     let primes = vec![2, 3, 5, 7];
//     let prime_squares: Vec<_> = primes.into_iter().map(|p| p * p).collect();
//     println!("prime_squeares: {prime_squares:?}");
// }

// use std::ops::Sub;

// //연습문제: 반복자 메서드 체이닝
// /// Calculate the differences between elements of `values` offset by `offset`,
// /// wrapping around from the end of `values` to the beginning.
// ///
// /// Element `n` of the result is `values[(n+offset)%len] - values[n]`.
// fn offset_differences<N>(offset: usize, values: Vec<N>) -> Vec<N>
// where
//     N: Copy + std::ops::Sub<Output = N>,
// {
//     let a = (&values).into_iter();
//     let b = (&values).into_iter().cycle().skip(offset);
//     a.zip(b).map(|(a, b)| *b - *a).collect()
// }

// #[test]
// fn test_offset_one() {
//     assert_eq!(offset_differences(1, vec![1, 3, 5, 7]), vec![2, 2, 2, -6]);
//     assert_eq!(offset_differences(1, vec![1, 3, 5]), vec![2, 2, -4]);
//     assert_eq!(offset_differences(1, vec![1, 3]), vec![2, -2]);
// }

// #[test]
// fn test_larger_offsets() {
//     assert_eq!(offset_differences(2, vec![1, 3, 5, 7]), vec![4, 4, -4, -4]);
//     assert_eq!(offset_differences(3, vec![1, 3, 5, 7]), vec![6, -2, -2, -2]);
//     assert_eq!(offset_differences(4, vec![1, 3, 5, 7]), vec![0, 0, 0, 0]);
//     assert_eq!(offset_differences(5, vec![1, 3, 5, 7]), vec![2, 2, 2, -6]);
// }

// #[test]
// fn test_custom_type() {
//     assert_eq!(
//         offset_differences(1, vec![1.0, 11.0, 5.0, 0.0]),
//         vec![10.0, -6.0, -5.0, 1.0]
//     );
// }

// #[test]
// fn test_degenerate_cases() {
//     assert_eq!(offset_differences(1, vec![0]), vec![0]);
//     assert_eq!(offset_differences(1, vec![1]), vec![0]);
//     let empty: Vec<i32> = vec![];
//     assert_eq!(offset_differences(1, empty), vec![]);
// }

// 연습문제: 룬 알고리즘

pub fn luhn(cc_number: &str) -> bool {
    let mut sum = 0;
    let mut double = false;
    let mut digits = 0;

    for c in cc_number.chars().rev() {
        if let Some(digit) = c.to_digit(10) {
            digits += 1;
            if double {
                let double_digit = digit * 2;
                sum += if double_digit > 9 {
                    double_digit - 9
                } else {
                    double_digit
                };
            } else {
                sum += digit;
            }
            double = !double;
        } else if c.is_whitespace() {
            continue;
        } else {
            return false;
        }
    }

    digits >= 2 && sum % 10 == 0
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_valid_cc_number() {
        assert!(luhn("4263 9826 4026 9299"));
        assert!(luhn("4539 3195 0343 6467"));
        assert!(luhn("7992 7398 713"));
    }

    #[test]
    fn test_invalid_cc_number() {
        assert!(!luhn("4223 9826 4026 9299"));
        assert!(!luhn("4539 3195 0343 6476"));
        assert!(!luhn("8273 1232 7352 0569"));
    }
}
