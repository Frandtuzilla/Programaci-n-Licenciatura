// Task 1: Use `map` to create a new array with the length of each string
const names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'];
const nameLengths = names.map(name => name.length);
console.log("Lengths of names:", nameLengths); // [5, 3, 7, 5, 3]

// Task 2: Use `filter` to create a new array with numbers greater than 10
const numbers = [5, 12, 8, 21, 3, 18];
const filteredNumbers = numbers.filter(number => number > 10);
console.log("Numbers greater than 10:", filteredNumbers); // [12, 21, 18]

// Task 3: Use `reduce` to calculate the sum of all numbers in the array
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log("Sum of all numbers:", sum); // 67