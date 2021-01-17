// Data Types
// Primitive --> holds 1 value


//String
let username = "David"
let poem ="It's a beautiful morning, no ?"

//concatenate
let nationality = "Israeli"
let mood = "happy"


let user = "David";
let intelligence = " is smart";
let sentence = user + " is" + intelligence

// console.log("the sentence is :", user + intelligence)


"D a  v  i  d"
0, 1, 2, 3, 4

// index: postion of each letter, the position always starts at 0
"David".chartAt(3) --> i

"Sun".chartAt(2) --> n

"Sun".chartAt(0) --> S

//string.nameOfMethod()
"David".indexOf("v") --> 2

"David".indexOf("d") --> 4

let user = "David"
user.indexOf("D")

//Properties
//datatype
//string.nameOfProperty

"David".length --> 5


"D A V I D"
//position or index
0 1 2 3 4
//length 
1 2 3 4 5 -> 5 letters


// I want to retrieve the last letter of the username
// the username has an infinite number of letters
let username = "zzzzzzzzzzzzzzzzzzzzzzA"
username.indexOf(username.length-1)
username.charAt(username.length-1)


//NUMBER
let age = 23
let ageBefore = age - 1


//typeof = allows us to know the kind of variable (number, string, boolean...)

// = : assign a value to a variable

// == : comparing two values

// === : 

12 == "12" --> true

12 === "12" --> false


// ARRAY : list

let colors = ["blue", "red", "yellow", "pink"]
//nameOfTheVariable[index/position of the element]
colors[0] // "blue"
colors[0] // "red"

console.log(colors[3])

// 2 ways
console.log(colors[colors.length-1]) --> green
console.let(colors[4]) --> green

colors[2] = "white" --> replace "yellow" with "white";

let favoriteColor = color[3]

console.log("My favorite color is " + favoriteColor)

// colors.join("!") / join method

let joined = colors.join("!")

typeof(joined) --> "string"

colors.push("black") --> add "black";

color.pop --> take out the last element of an array

let pets = ["cat", "dog", "fish", "rabbit", "cow"];

console.log(pets[1]) // "dog";

pets.push("horse"); // add "horse" at the end of the array

pets.pop("rabbit"); // remove "rabbit" to the array

console.log(pets.length); // "display the array length"


colors.splice(1, 1) // delete the color "red"

colors.splice(2,0, "yellow") // add the color "yellow"

colors.splice(1, 3, "black", "red") // delete "white", "yellow" and "pink" and add "black" and "red"


let colors = ["yellow", ["red","pink"]]
//Get color "red"
console.log(colors[1][0])