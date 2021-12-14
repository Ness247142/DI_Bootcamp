
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

let people = ["Greg", "Mary", "Devon", "James"];

for (i = 0; i < people.length; i++) {
    console.log(people[i]);
}

let index = people.indexOf("Greg");

if (index !== -1) {
    people.splice(index, 1);
}
console.log(people);

let index = people.indexOf("James");

if (index !== -1) {
    people.splice(index, 1, "Jason");
}

console.log(people);

people.push("Nessim");

console.log(people);

let index = people.indexOf("Jason");

for(i = 0; i < people.length; i++) {

    console.log(people[i]);

    if (i == index) {
        break;
    }
}

let index_2 = people.indexOf("Nessim");

let people_2 = people.slice(index-1, index_2);

console.log(people_2);

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo"));

let last = people[people.length-1];

console.log(last);

//Exercise 3
let numbers = prompt("Give me a number");

while (number < 10) {
    alert("Your number must be bigger than 10");
    number = prompt("Pick another number");
}

alert(`Your number is: ${number}`);



// Exercise 4
let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
  }

  for (const i in guestList) {
    if (guest != i) {
        continue;
    } else if (guest == i){
        alert(`Hi! I'm ${i}, and I'm from ${guestList[i]}.`);
        break;
    } else {
        alert(`Hi, I am a guest`);
        break;
    }
}

console.log(guestList);


//Exercise 5
let family = { firstName: "Henri", lastName: "Azoulay", age: 62 };
for (let x in family) {
    console.log(x + ": " + family[x])
}

//Exercise 6

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]

let sortedNames = names.sort();
let secondList = "";

for (let i in sortedNames) {
    secondList += sortedNames[i][0];
}

console.log(secondList);

