Here are concise file read/write examples for all languages:

## **Bash**
```bash
# Write
echo "Hello" > file.txt

# Read
cat file.txt
# or line by line
while read line; do echo "$line"; done < file.txt
```
[[12]]

## **C**
```c
#include <stdio.h>

// Write
FILE *f = fopen("file.txt", "w");
fprintf(f, "Hello");
fclose(f);

// Read
FILE *f = fopen("file.txt", "r");
char buf[100];
fgets(buf, 100, f);
fclose(f);
```
[[21]]

## **C++**
```cpp
#include <fstream>

// Write
std::ofstream f("file.txt");
f << "Hello";
f.close();

// Read
std::ifstream f("file.txt");
std::string line;
std::getline(f, line);
f.close();
```
[[34]]

## **C#**
```csharp
// Write
File.WriteAllText("file.txt", "Hello");

// Read
string content = File.ReadAllText("file.txt");
```
[[43]]

## **Elixir**
```elixir
# Write
File.write("file.txt", "Hello")

# Read
{:ok, content} = File.read("file.txt")
```
[[48]]

## **Go**
```go
// Write
os.WriteFile("file.txt", []byte("Hello"), 0644)

// Read
data, _ := os.ReadFile("file.txt")
```
[[61]]

## **Haskell**
```haskell
-- Write
writeFile "file.txt" "Hello"

-- Read
content <- readFile "file.txt"
```
[[73]]

## **Java**
```java
// Write
FileWriter f = new FileWriter("file.txt");
f.write("Hello");
f.close();

// Read
BufferedReader br = new BufferedReader(new FileReader("file.txt"));
String line = br.readLine();
```
[[77]]

## **Lua**
```lua
-- Write
f = io.open("file.txt", "w")
f:write("Hello")
f:close()

-- Read
f = io.open("file.txt", "r")
content = f:read("*all")
f:close()
```
[[87]]

## **Python**
```python
# Write
with open("file.txt", "w") as f:
    f.write("Hello")

# Read
with open("file.txt") as f:
    content = f.read()
```
[[99]]

## **Rust**
```rust
// Write
std::fs::write("file.txt", "Hello").unwrap();

// Read
let content = std::fs::read_to_string("file.txt").unwrap();
```
[[110]]

## **Assembly**
Assembly requires system calls and varies by platform. On Linux x86-64:
- Use `sys_open`, `sys_read`, `sys_write`, `sys_close`
- Much more verbose than high-level languages
[[4]]
