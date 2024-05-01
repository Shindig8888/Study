use std::error;

// use std::error::Error;
// use std::fmt::{Display, Formatter};
use thiserror::Error;

#[derive(Debug, Error)]
#[non_exhaustive]
pub enum PuzzleError {
    #[error("Piece {0} doesn't fit!")]
    WontFit(u16),
    #[error("Missing a piece")]
    MissingPiece,
}

// impl Error for PuzzleError {}

// impl Display for PuzzleError {
//     fn fmt(&self, f: &mut Formatter) -> std::fmt::Result {
//         use PuzzleError::*;
//         match self {
//             MissingPiece => write!(f, "Missing a piece"),
//             WontFit(n) => write!(f, "Piece {} doesn't fit!", n),
//         }
//     }
// }

// fn main() {}
