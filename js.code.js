function generateRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Example usage
var min = 1;
var max = 1000;
var randomNumber = generateRandomNumber(min, max);

// Use WScript.Echo to output the message
WScript.Echo("gjenrato ni numer o nan e dugit " + min + " and " + max + ": " + randomNumber);
