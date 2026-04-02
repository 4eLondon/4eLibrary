// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: npx ts-node main.ts

import * as readline from "readline";

const rl = readline.createInterface({ input: process.stdin });

rl.question("Enter your name: ", (name: string) => {
  rl.question("Enter your age: ", (age: string) => {
    console.log("\nYou entered:");
    console.log(`  Name: ${name}`);
    console.log(`  Age:  ${age}`);
    rl.close();
  });
});
