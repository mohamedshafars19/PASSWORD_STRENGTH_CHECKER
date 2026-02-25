# PASSWORD_STRENGTH_CHECKER

## Project Overview
This project is a Password Strength Checker developed using Python.  
The program checks the strength of a password entered by the user and classifies it as **Poor**, **Good**, or **Excellent**.

Based on the strength result, the program asks the user to change the password until a strong password is entered.

---

## What This Program Does
- Displays the rules required for creating a strong password
- Accepts a password from the user as input
- Checks the password using multiple conditions
- Classifies the password strength as:
  - Poor
  - Good
  - Excellent
- If the password is not strong enough, the user is asked to change it
- The process continues until an excellent password is entered

---

## Password Strength Criteria
The strength of the password is checked based on the following rules:
- Minimum of 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

---

## Concepts Used in This Project
- Conditional statements (`if`, `elif`, `else`)
- Looping (`while`, `for`)
- Python data structures:
  - Tuple (to store password rules)
  - List (to analyze password characters)
  - Set (to store special characters)
  - Dictionary (to track condition status)
- String methods

---

## Purpose of the Project
The purpose of this project is to understand how password security works and how Python can be used to validate and improve password strength using logical conditions and data structures.

---

## Conclusion
This project helps users create secure passwords and demonstrates practical usage of Python programming concepts without using classes.
