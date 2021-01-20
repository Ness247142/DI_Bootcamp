
//Exercise 1
let colors = ["red", "blue", "green", "yellow"];
for (let i = 0; i < colors.length; i++) {
    console.log("My #" + (i + 1) + " color is " + colors[i]);
}

for (let i = 0; i < colors.length; i++) {
    let colorsNum = i + 1;
    let colorsNumSuffix;
    if (colorsNum == 1) {
        colorsNumSuffix = 'st';
    } else if (colorsNum == 2) {
        colorsNumSuffix = 'nd';
    } else if (colorsNum == 3) {
        colorsNumSuffix = 'rd';
    } else {
        colorsNumSuffix = 'th';
    }
    console.log(" My " + colorsNum + colorsNumSuffix + " color is " + colors[i]);
}


// Exercise 2

let people = ["Greg", "Mary", "Devon", "James"]

for(let i = 0; i < people.length; i++) {
    console.log(people[i]);
  }

people.shift();

console.log(people[3]);
people[3] = "Jason";

people.push("Nessim"); 

for (let counter = 0; counter <= people.length; counter++){
    if(counter == "Mary") {
        console.log("exit")
        break;
}
}

console.log(people.slice(0, 3));

people.indexOf("Mary");

people.indexOf(people.length-1);

let last = people[3];



//Exercise 3
let numbers = prompt("Give me a new number");
let i = 0;

while(i < 10){
    i++;
    console.log(i)
    prompt("Give me another number");
	
}
alert("Good job!")



// Exercise 4
let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
  }

  let name = prompt("What is your name?");
  let sentence = "Hi! I'm " + guestList + ", and I'm from " + guestList["country"];

  if (i == guestList.length) {
    console.log(sentence);
}
else {
    console.log(" Hi! I'm a guest. ");
}



//Exercise 5
let family = { firstName: "Henri", lastName: "Azoulay", age: 62 };
for (let x in family) {
    console.log(x + ": " + family[x])
}


//Exercise 6

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]

let sortedNames = names.sort();
let secondList = " ";

for (let i in sortedNames) {
    secondList += sortedNames[i][0];
}

console.log(secondList);

