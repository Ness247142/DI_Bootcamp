

for (let i = 0; i < 3; i ++){
    console.log("variable i : ", i)
    console.group()


    //Nested for loop
    // Running 5 times
    for (let x = 10; x <= 14, x++){
    console.log("variable x : ", x)
    }
}

//declaring a function
function userInfo (username, age, height) {
    console.log("Hello" + username)
    console.log("Age" + age)
    console.log("Height" + height)
}


//invoke/call the function
userInfo("David", 25, 1.7)


// Create a structured html file linked to a js file

// 2. Write a JS function that takes a parameter: myAge

// 3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)

// 4. Call the function


function age(myAge) {
    let ageMom = 2*myAge;
    let ageDad = 1.2*ageMom
    console.log(" My mum is " + ageMom + " years old " + " and my dad is " + ageDad + " years old ")}

age(24);


//DECLARING
function familyAge (myAge) {
	// display the age of the mum : twice my age
	// display the age the dad : 1.2 times the age the mum
	let ageMum = myAge*2
	let ageDad = ageMum*1.2
	console.log("The age of my mum is " + ageMum + " the age of my dad is " + ageDad)
	//the same as
	console.log(`The age of my mum is ${ageMum}, the age of my dad is ${ageDad}`)
}
​
//INVOKE
familyAge(60)


function age(myAge) {
    let ageMum = myAge*2
    return ageMum 
}

function ageDetail(){
    let mumDetail = age(24)
    console.log ("The age of my mum is " + ageMum)
}

ageDetail()

let retrieveAgeMum = age(24)
console.log("My mum is " + ageMum)

myAge(24)


// 1 FUNCTION = 1 ACTION
​
//calculating the age of the dad
function familyAge(myAge){ //4th step
	let ageDad = myAge*2 
	return ageDad //5th step
}
​
//displaying the details about the dad
function familyDetail(){ //2nd step
	//dadDetail = ageDad = 40
	let dadDetail = familyAge(20) //3rd step //6th step
	console.log(`My dad is ${dadDetail}`)
}
​
familyDetail() //1r step


//global variable
// decared in the global scope
let username = "Lea"
​
console.log("1:", username) // display Lea
​
//DECLARING
function familyAge (myAge) {
	console.log("2:",username) // display Lea
	// In the local scope I can modify a
	// variable that was declared in the global scope
	// and I can change the global variable
	username = "David"
	console.log("3:",username) // display David
	//local variables
	let ageMum = myAge*2
	let ageDad = ageMum*1.2
	console.log(`The age of my mum is ${ageMum}, the age of my dad is ${ageDad}`)
}
​
//INVOKE
familyAge(60)
​
console.log("4:",username) // display David
​
​
​
//global scope
console.log(ageMum) // undefined
​
// // LOCAL VARIABLE: IS A VARIABLE DECLARED IN THE LOCAL SCOPE
// // YOU CANNOT ACCESS A LOCAL VARIABLE IN THE GLOBAL SCOPE


// declaring a function
				// PARAMETERS
                function userInfo (username,age,height) {
                    console.log("Hello " + username)
                    console.log("Age " + age)
                    console.log("Height " + height)
                }
                ​
                //global scope
                console.log("username :", username)
                ​
                // Local means used in the local scope : in a block
                // functions, loops, conditionals
                ​
                // Global means used in the global scope
                // outside of a local
                ​
                ​
                // invoke/call the function
                // ARGUMENT
                userInfo("David",25, 1.7)


let array = [1,2,3]
let sum = 0;
​
sum = sum + array[0] // so SUM is equal to 1  // THE SAME AS --- sum += array[0]
sum = sum + array[1] // so SUM is equal to 3  // THE SAME AS --- sum += array[1]
sum = sum + array[2] // so SUM SUM is equal to 6  // THE SAME AS --- sum += array[2]
​
// loop --> faster to write
​
for (let i = 0; i<array.length; i++) {
	sum += array[i]
}
​
console.log("sum : ", sum)