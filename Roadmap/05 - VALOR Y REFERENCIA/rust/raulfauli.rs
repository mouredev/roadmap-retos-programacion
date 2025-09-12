/// #05 VALOR Y REFERENCIA
///
/// `rustc ./Roadmap/05\ -\ VALOR\ Y\ REFERENCIA/rust/raulfauli.rs && ./raulfauli && rm raulfauli`
///
fn main() {

  // Paso por valor un tipo primitivo
  let mut foo = 42;
  let f = foo;
  foo = 13;
  println!("{}", f); // 42
  println!("{}", foo); // 13

  // Paso por valor una lista
  let mut list = [1, 2, 3];
  let l = list;
  list[0] = 4;
  println!("{:?}", l); // [1, 2, 3]

  // Paso por referencia
  let mut foo = 42;
  let f = &mut foo;
  let bar = *f; // guardo el valor de la referencia
  *f = 13;      // modifico el valor de la referencia
  println!("{}", bar); // 42
  println!("{}", foo); // 13

  // Paso por referencia una lista
  let mut list = [1, 2, 3];
  let l = &mut list;
  let bar = &mut l[0]; // guardo la referencia
  *bar = 4;            // modifico el valor de la referencia
  println!("{:?}", l); // [4, 2, 3]



  // Funciones con paso por referencia
  fn to_upper(s: &mut String) {
    s.make_ascii_uppercase();
  }

  let mut hola = String::from("hola");
  to_upper(&mut hola);
  println!("{hola}"); // HOLA


  // Extra
  let mut a = 1;
  let mut b = 2;

  fn swap_values(a: i32, b: i32) -> (i32, i32) {
    (b, a)
  }

  let (c, d) = swap_values(a, b);

  println!("a: {a}, b: {b}"); // a: 1, b: 2
  println!("c: {c}, d: {d}"); // c: 2, d: 1

  fn swap_references(a: &mut i32, b: &mut i32) {
    let t = *a;
    *a = *b;
    *b = t;
  }

  swap_references(&mut a, &mut b);
  println!("a: {a}, b: {b}"); // a: 2, b: 1
}
