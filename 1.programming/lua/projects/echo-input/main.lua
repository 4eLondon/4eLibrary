-- Project: echo input
-- What it does: asks the user for their name and age, then prints them back
-- Run: lua main.lua

io.write("Enter your name: ")
local name = io.read()

io.write("Enter your age: ")
local age = io.read()

print("\nYou entered:")
print("  Name: " .. name)
print("  Age:  " .. age)
