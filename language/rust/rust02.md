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