### compound data types
#### arrays 
- continious group of items 
- fixed length
- length known at compile time 
-  heterogeneous (동일한 자료형을 써야 됨)
```rust
let array := [u32 , 3] = [1, 2, 3];
```
#### tuples 
- continious group of items 
- fixed length
- length known at compile time 
- homogenous (다른 자료형을 사용회도 됨 :))
- empty tuple called `unit`
```rust
let tuple : (bool , u16 , u8) = (true ,2 , 3);
```
- indexing 
- - access items by index `let first_item = tuple.0;`


### function
#### function
```rust
fn exclaim(input : String) -> String{
    ...
}
```
- argument types always required
- return type always required if value returned
- if not retun type is unit(`empty tuple`)
- - Opional `retturn` keyword
- - last value is returned

### struct 
- a type that's composed of other types
- can contain different types
- three flavors of structs
- - classic
- - tuple
- - unit 
```rust 
struct Car {
    name: String,
    model: String,
    year: u32,
}

fn main (){
    let car1 = Car {
        make: String::from("Ford"),
        modle: String::from("Mustang"),
        year: 2022,
    };
}
```
### enum
- use the keyword enum followed by name
- list all variations 