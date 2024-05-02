use testing::{splish, sploosh};

#[test]
fn sploosh_integration() {
    assert!(sploosh(splish(-1, 0), splish(1, 1), splish(3, 2)) == 4)
}
