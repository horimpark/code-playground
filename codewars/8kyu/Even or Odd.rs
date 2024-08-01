fn even_or_odd(number: i32) -> &'static str {
    let x = number % 2;
    if x == 0 {
        "Even"
    }
    else {
        "Odd"
    }
}