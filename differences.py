# # Write a method that accepts a name from the user and then returns it.

# # Here's the javascript:
# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

# #Here's the python:
# name = input("What is your name?")
# print (f"My name is {name}");

# # Write a method that reverses a string.

# # Here's the javascript:
# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   console.log(reverse);
# };

# # Here's the python:

# reverseIt = input("What would you like to reverse")
# # reverseString(reverseIt)
# print (f"This is the reverse: {reverseIt[::-1]}")

# # Swap Em
# # Write a method that swaps the values of two variables around. 

# # Here's the javascript:
# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   console.log("a is now " + a + ", and b is now " + b);
# };

# # Here's the python:

# a = 10
# b = 30
# print(a, b)

# temp = b
# b = a
# a = temp
# print(f"a is now {a} and b is now {b}")

# # Multiply Array
# # Write a method that multiplies all numbers in a given array and returns the final product.

# # Here's the javascript:
# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# # Here's the python:'

# array = [1, 2, 3, 4, 5, 6, 7]

# mult = 1
# for i in array:
#     mult = mult * i
# print(mult)

# # Fizz Buzzer
# # Write a method that takes a number argument and returns "fizz" if the number is divisible by three, "buzz" if the number is divisible by five, and "fizzbuzz" if it's divisible by both.

# Here's the javascript:
# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

# # Here's the python:

# number = int(input("What number do you want"))

# if number % 3 == 0 and number % 5 == 0:
#     print('fizzbuzz')
# elif number % 3 == 0:
#     print('fizz')
# elif number % 5 == 0:
#     print('buzz')
# else:
#     print('archer')