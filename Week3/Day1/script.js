
//How to change the text content of the 3rd li to "John"

//get the body
let bodyWebsite = document.body
//get the div
let divWebsite = bodyWebsite.firstElementChild
				//bodyWebsite.children[0]
//get the ul
let ulWebsite = divWebsite.firstElementChild
//get the li
let liThirdWebsite = ulWebsite.lastElementChild
console.log(liWebsite)
​
//change the text node of the li
liThirdWebsite.textContent = "John"
​
//get the second li of the ul
let liSecondWebsite = liThirdWebsite.previousElementSibling
console.log("Second li : ", liSecondWebsite)
​
//get the parent of the li
console.log("parent of li: ", liSecondWebsite.parentNode)



// DOM Exercise 1
//get the body
let bodyWeb = document.body
console.log(bodyWeb);

// second way of getting the body
document.body

//get the div : GOOD
let divWeb = bodyWeb.firstElementChild
console.log(divWeb);

// second way of getting the div 
document.body.children[0]

//get the ul// UL IS NOT A CHILD OF THE DIV
let ulWeb = bodyWeb.lastElementChild
let liSecondWeb = ulWeb.lastElementChild
console.log(liSecondWeb);

// second way of getting the li with "Pete"
document.body.lastChild[1];



//Add 5 paragraphs and 5 images at the same time to the DOM
​
let bodyWebsite = document.body
let newDiv = document.createElement("div")
​
for (let i = 0; i < 5; i++){
	let newImage = document.createElement("img")
	newImage.setAttribute("src", "cat.jpg")
	let newParagraph = document.createElement("p")
	newParagraph.className = "welcomeUser"
	let newContent = document.createTextNode("Hello new users " + i)
	newParagraph.appendChild(newContent)
	newDiv.appendChild(newParagraph)
	newDiv.appendChild(newImage)
}
​
bodyWebsite.appendChild(newDiv)
