
// Creating HTML text and higlighting it
let container = document.getElementById("container")
container.innerHTML = "<p>Hello <span>how</span> are you?</p>"
document.getElementsByTagName("span")[0].style.color = "red"


//Quizz review
let username = "David"
// variable -> collect or save values -> reuse them after in the code

dataType : boolean, string, numbers (primitive data type)
complex data type : arrays & objects

= assign a value to a variable
== or === comparing 2 values


// the computer checks if the condition is true or false automatically
if (condition) {
    statement
} else if (condition) {
statement
} else {
statement
}

let username = "David"
--> program that checks --> if it's david -- brother
--> --> if it's john -- father
switch(username){
    case "David":
        xxx
    break;
    case "John":
        xxx
    break;
    default:
        xxx
}
----------------------------
---OBJECTS---
let family = {
    name : "Doe"
}
console.log(family.name)
* What is the DOM ? --> representation of the HTML , all HTML element -> Node -> object
                    --> apply method & property to a Node
* Nested objects
                    document.body.firstElementChild.style
                    document.getElementById().
                    let document = {
                        body : {
                            style : "backgroundColor"
                            xxx : {
                                ccc : {
                                }
                            }
                        }
                    }
JS methods to retrieve an element of the DOM : Relationship 
children[0] - 
firstElementChild
lastElementChild
previousElementSibling
id - getElementById
tag
class
queryselector
for loop : goal -> repetition action until condition false
for (let index = 1; index <= 3; index ++) {
    console.log("hello")
}
Loop runs
index = 1 - check the condition - true -  console.log()
index = 2 - check the condition - true - console.log()
index = 3 - check the condition - true - console.log()
index = 4 - check the condition - false - GO OUT
x : starting value of the counter - 1
    y : condition - loop will run if the index (counter) is smaller or equal to 3
                  - loop will run if the condition (index <= 3) is true
                  - if the index > 3, the loops : condition (index <= 3) is false
    z : final part : increments the counter to whatever number
                   : increment - continues the loop
                   : if we don't increment - loop forever
                   
--- LOOPS WITH ARRAY---
for (let index = 0; index <= 2; index ++) {
    console.log("hello")
}
let colors = ["blue", "black", "yellow"]
                0       1        2
WE DONT HAVE A L00P  - WE NEED A LOOP
colors[0]            - changing : position
colors[1]            - staying : colors[index] - 0, 1, 2
colors[2]
    
// built-in function-method
// setTimeout(paramaters,parameters);
// setTimeout(function, timer)
​
function sayHi(message) {
	console.log("console.log in settimeout")
	let container = document.getElementById("container")
	container.textContent = message
	container.style.backgroundColor="yellow"
}
​
​
// //1
console.log("1st console.log Before set timeout")
​
// //2 - wait 2 second 
setTimeout(sayHi, 2000, "Your cart is empty");
​
// //3
console.log("2st console.log After set timeout")
​
--- setInterval
​
let bye = document.getElementById("containerBye")
​
//set the setinterval : the interval is called "timing"
let timing = setInterval(sayHi, 2000);
​
bye.addEventListener("click", stopTimer)
​
function sayHi() {
	console.log("console.log in setinterval")   
}
​
function stopTimer(){
	//stop the interval called "timing"
	clearInterval(timing)
}
