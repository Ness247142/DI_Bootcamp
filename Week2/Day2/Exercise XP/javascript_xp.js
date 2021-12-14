// Exercise 1
let x = 5;
let y = 2;

if (x > y ){
    console.log("x is the biggest number");
} else {
    console.log("y is the biggest number");
}

// Exercise 2
let newDog = "Chihuahua";

console.log(newDog.length);

console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog == "Chihuahua"){
    console.log("I love Chihuahua, it’s my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}

//Exercise 3
let x = prompt("What is your favorite number?");

if (x % 2 == 0){
    console.log("x is an even number");
} else {
    console.log("x is not an even number");
}


// Exercise 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let numberOfUsers = users.length;
let numberOfPeopleRemaining = numberOfUsers-2;

if (users.length == 0) {
    console.log("no one is online");

} else if (users.length == 1){
    console.log(users[0] + "is online");

} else if (users.length == 2){
    console.log(users[0] + users[1] + " are online ");

} else if (users.length > 2){
    console.log(users[0] + users[1] + " and " + numberOfPeopleRemaining + " more are online ");

} else {
    console.log("HAPPY");
};



