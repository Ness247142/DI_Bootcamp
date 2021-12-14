//Exercise 1
let language = prompt("Which language do you speak?");

switch (language) {
    case "French":
      console.log("Bonjour");
      break;
    case "English":
        console.log("Hello");
      break;
    case "Hebrew":
      console.log("Shalom");
      break;
    default:
      console.log("01110011 01101111 01110010 01110010 01111001");
  }



// Exercise 2
let grade = prompt("What is your grade?");

if (grade > 90) {
    console.log("A");

} else if (80 <= grade && grade <= 90) {
    console.log("B");

} else if (70 <= grade && grade <= 80) {
    console.log("C");

} else {
    console.log("D");
};


//Exercise 3
let verbing = "swimming";

if (verbing.length >= 3) {
    console.log(verbing + "ing");

} else if (verbing + "ing") {
    console.log(verbing + "ly");
}
    else {
      console.log(verbing.length < 3);
    }
