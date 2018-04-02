# COMP 511: Written Assignment 2
Vu Phan, `vhp1`

## Topic
type inference

## Exemplifying PL feature or idiom
Scala compiler's local type inference (not Hindley-Milner global type inference)

## Description of features and limitations

### Scala

- The Scala compiler can infer expression types in some cases.

  ```scala
  val name = "Alan"
  ```

  The inferred type for the value `name` is `String`.

- The compiler can also infer the result type of a non-recursive method.

  ```scala
  def minus(x: Int) = -x

  ```
  In this case, the inferred result type is `Int`.

- However, result type inference fails for recursive functions.

  ```scala
  def factorial(n: Int) = if (n < 2) 1 else n * factorial(n - 1) // fails

  ```
  The programmer must explicitly specify that a `factorial` application returns an `Int`.

- Also, the compiler may infer a too specific type.

  ```scala
  var v = null
  v = new Object() // fails
  ```

  The compiler evaluates line 1 above and infers that `v` is of the singleton type `Null`. So the programmer cannot later reassign a non-`null` value to `v` as in line 2.

### Scala versus Jam

A big difference between Scala and Jam is: Scala employs local type inference instead of Hindley-Milner global type inference. The reason is that Hindley-Milner inference does not work with object-oriented programming (more specifically, type-polymorphism).

Another difference is that the Scala syntax is more flexible than the typed Jam syntax (both with type annotations as in project 5 and without them as in project 5xc). In Scala, some type annotations are optional, such as the result type of a non-recursive function.

## Reference

[https://docs.scala-lang.org/tour/type-inference.html](https://docs.scala-lang.org/tour/type-inference.html)

[https://stackoverflow.com/a/3691495](https://stackoverflow.com/a/3691495)
