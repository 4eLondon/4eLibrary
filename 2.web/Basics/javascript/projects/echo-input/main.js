// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: node main.js

const readline = require("readline");

const rl = readline.createInterface({ input: process.stdin });

rl.question("Enter your name: ", (name) => {
  rl.question("Enter your age: ", (age) => {
    console.log("\nYou entered:");
    console.log(`  Name: ${name}`);
    console.log(`  Age:  ${age}`);
    rl.close();
  });
});
