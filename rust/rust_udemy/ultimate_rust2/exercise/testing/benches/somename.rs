use criterion::{criterion_group, criterion_main, Criterion};
use testing::{splish, sploosh};

pub fn sp_bench(c: &mut Criterion) {
    c.bench_function("sploosh(8, 9, 10)", |b| b.iter(|| sploosh(8, 9, 10)));
}

criterion_group!(benches, sp_bench);
criterion_main!(benches);
