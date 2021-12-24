
// Exercise 1
// In the div above, change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new li to the ul.
// First, create a new li tag (use the createElement method)
// Then create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstChild and the lastChild properties to retrieve the first and last li elements under the parent ul node. Display the text of each link.(Hint: nodeValue property).

let navBar = document.getElementById("id")
console.log(navBar)
navBar.setAttribute("id", "socialNetworkNavigation");

let ul = document.getElementByTagName("ul")[0]
console.log(ul);

let newList = document.createElement("li");
let anchor = document.createElement("a")
let att = document.createAttribute("href")
att.value = "#"
anchor.setAttributeNode(att);
let text = document.createTextNode("Logout");
anchor.appendChild(text)
newList.appendChild(anchor)
ul.appendChild(newList)

console.log(newList);


//Exercise 2
// Change the name “Pete” by “Richard”
// Change each first name of the <ul> by your name
// Add at the end of each <ul>, a <li> that says “Hey students”
// Delete the <li> Sarah
// Bonus
// Add a class “student_list” to both of the <ul>
// Add the class “university” and “attendance” to the first <ul>


console.log(document.body.children[1].lastChild[1].innerHTML = "Richard");

let collection = document.getElementsByTagName("li").length; 

for (let i = 0; i < collection; i++) {
    let liTwo = document.getElementsByTagName("li")[i].innerHTML = "Nessim";
}

let ulTwo = document.getElementsByTagName("ul");

for (let selectedUl of ulTwo) {
    selectedUl.firstElementChild.innerHTML = "Nessim"
    console.log(selectedUl.firstElementChild.innerHTML);
}

let allUl = document.getElementsByTagName("ul");


for (let selectedUl of allUl) {
    selectedUl.firstElementChild.innerHTML = "Nessim"
    let liNew = document.createElement("li");
    let text = document.createTextNode("Hey students")
    liNew.appendChild(text);
    selectedUl.appendChild(liNew);

}

let liFive = document.getElementsByTagName("li")[4]
console.log(liFive);

let secondUl = document.getElementsByTagName("ul")[1];
secondUl.removeChild(liFive);
console.log(liFive);


// Exercise 3 
// Open up Github in Chrome or Firefox, and open up the console.
// Find the Github navbar and store it in a variable. Use the DOM properties and methods to retrieve the element node. Don’t add an id or a class the the element.
// Change the color of the navbar.
// Find your Github name and store it in a variable.
// Change your name by “The Boss”



// Exercise 4
// 1. Add a “light blue” background color and some padding to the div above.
// 2. Do not display the first name (John) in the list and add a border to the second name (Pete).
// 3. Change the font size of the whole body.
// 4. Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div)

console.log(document.body.firstElementChild.style.backgroundColor = "lightblue");

console.log(document.body.firstElementChild.style.padding = "50px 10px 20px 30px");

console.log(document.body.children[1].firstElementChild.innerHTML = " ");

console.log(document.body.children[1].lastElementChild.style.border = "3px solid red");

console.log(document.body.style.fontSize = "3-large");
