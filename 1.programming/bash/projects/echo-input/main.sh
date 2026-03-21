#!/usr/bin/env bash
# Project: echo input
# What it does: asks the user for their name and age, then prints them back
# Run: bash main.sh

read -p "Enter your name: " name
read -p "Enter your age: " age

echo ""
echo "You entered:"
echo "  Name: $name"
echo "  Age:  $age"
