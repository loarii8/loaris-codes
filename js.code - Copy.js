function generateRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Example usage
let min = 1;
let max = 100;
let randomNumber = generateRandomNumber(min, max);

console.log(`Generated random number between ${min} and ${max}: ${randomNumber}`);