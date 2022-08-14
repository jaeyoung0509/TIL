## origin 
ms rust beginners 

### what is rust and why u learn 
- no garbage collection
- memory safety
- - use after free 
- - dangling pointers 
- - null pointer exceptions
- - data races 
- - iterator invalidation
-> zero cost abstractions 

### rust community 
- users.rust-lang.org

### cargo (all rolled into one)
-  rust build tool
-  dependency manager 
-  test runner 
-  project bootsrapper  
  
### declare variables 
- bound to values using the keyword `let` 
- `immutable` by default  
- - creates predictability in our code 
- - can be more convenient to make  variables mutable 
- - there are trade-offs either way 
- - a similar concept as `constants`
#### const 
```rust
fn main() {
    const SCORE_LIMIT :u32 = 100;
}
```
- name of the constant should be capitalized , with underscores in between words 
- can only be set to an expression

#### shadow a variable
- declare a new variable with the same name as the previous , creating a new binding
- the new variable shadows the previous variable
- 타입 변경도 가능
  
```rust 
func main(){
    let x=5;
    let x = x +1 ; // creating new binding
}
```

