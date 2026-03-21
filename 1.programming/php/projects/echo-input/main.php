<?php
// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: php main.php

echo "Enter your name: ";
$name = trim(fgets(STDIN));

echo "Enter your age: ";
$age = trim(fgets(STDIN));

echo "\nYou entered:\n";
echo "  Name: $name\n";
echo "  Age:  $age\n";
