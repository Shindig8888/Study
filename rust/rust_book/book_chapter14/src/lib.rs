//! # Art
//!
//! A library for modeling artistic concepts.
pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    /// The primary colors according to the RYB color model
    pub enum PrimaryColor {
        Red,
        Yellow,
        Blue,
    }

    ///The secondary colors according to the RYB color model.
    #[derive(Debug)]
    pub enum SecondaryColor {
        Orange,
        Green,
        Purple,
    }
}

pub mod utils {
    use crate::kinds::*;
    use std::io;

    /// Combines two primary colors in equal amounts to create
    /// a secondary color.
    pub fn mix(c1: PrimaryColor, c2: PrimaryColor) -> Result<SecondaryColor, io::Error> {
        match (c1, c2) {
            (PrimaryColor::Red, PrimaryColor::Yellow) => Ok(SecondaryColor::Orange),
            (PrimaryColor::Yellow, PrimaryColor::Blue) => Ok(SecondaryColor::Green),
            (PrimaryColor::Blue, PrimaryColor::Red) => Ok(SecondaryColor::Purple),
            (PrimaryColor::Yellow, PrimaryColor::Red) => Ok(SecondaryColor::Orange),
            (PrimaryColor::Blue, PrimaryColor::Yellow) => Ok(SecondaryColor::Green),
            (PrimaryColor::Red, PrimaryColor::Blue) => Ok(SecondaryColor::Purple),
            _ => Err(io::Error::new(
                io::ErrorKind::Other,
                "Invalid color combination",
            )),
        }
    }
}

// //! #My Crate
// //!
// //! 'my_crate is a collection of utilities to make performing certain
// //! calculations more convinient.
// ///Adds one to the number given.
// ///
// /// # Examples
// ///
// /// '''
// /// let arg =5;
// /// let answer = my_crate::add_one(arg);
// ///
// /// assert_equ!(6, answer);
// /// '''
// pub fn add_one(x: i32) -> i32 {
//     x + 1
// }

// //cargo, crates.io

// // //문서화 주석: ///cargo doc
// // //#Examples
// // //#Panics
// // //#Errors
// // //#Saefty

// //주석이 포함된 아이템 : //!, 가장 첫줄에 와야됨
