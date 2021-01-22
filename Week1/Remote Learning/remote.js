
// Exercise_1
// Analyse the code below without running it, what will be the output ?

var num = 8;
var num = 10;
console.log(num);

// The expected output will be num == 10;
// The second variable (var num = 10) will override the first variable (var num = 8) in a hierarchical way. It's the "Cascading order".



// Exercise_2
// Change the code so the var i will be undefined outside of the for loop

function numbers() {
    var i;

for (i = 0; i < 5; i += 1) {
    
    console.log(i);
}
    console.log(i);
}

numbers();



//Exercise_3

// Create a global variable that save the amount of money you have in your account
// Create a variable that saves the amount of VAT
// Create a variable that saves the amout of all the expenses and revenu you did /received for the past last month
// Create a JS code that multiplies of the expenses by the VAT
// Create a JS code that changes the amount of the money you have in your account depending on your expenses/revenu.
// Display it

let myAccount = 50000;

const vatIsrael = 0.17;

let expenses = 4000;

let vatAmount = expenses * vatIsrael;


console.log(`Expenses and revenu received last month: ${myAccount}`);

console.log(`Expenses: ${expenses}. Value Added Tax is ${vatIsrael*100}%`);

myAccount -= (expenses - vatAmount);

console.log(`Amount of money depending on expenses/revenu : ${myAccount}`);