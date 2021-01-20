
// Exercise 1

// Ask the user for his age, and save the value into a variable
// Create a function called checkDriverAge() that will alert the user if he can drive depending on his age.
// if he is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if he is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if he just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// Instead of using prompt to ask the user for his age, make the checkDriverAge() function accept an argument age, so that if you enter: checkDriverAge(92); it alerts “You are old enough to drive, Powering On. Enjoy the ride!”


// let age = prompt("What is your age?")
function checkDriverAge(age) {
	if (age < 18) {
		alert("Sorry, you are too yound to drive this car. Powering off");
	} else if (age > 18) {
		alert("You are old enough to drive, Powering On. Enjoy the ride!");
	} else if (age === 18) {
		alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
}

checkDriverAge(92);



//Exercise 2

// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item. 
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// To illustrate: 
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

Quarters  = 0.25
Dimes = 0.10
Nickels = 0.05
Pennies = 0.01

let denom = [
  {name: "QUARTER", val: 0.25},
  {name: "DIME", val: 0.1},
  {name: "NICKEL", val: 0.05},
  {name: "PENNY", val: 0.01}
];

function change (money, string) {
  let change = [0.25, 0.10, 0.05, 0.01];
  let result = 0;
  for (let x = 0; x < change.length; x++) {
      result += change[x] * string[x];
  }
  if (result > money) {
      return true;
  } else {
      return false;
  }
}

console.log(change([0, 0, 20, 5], 0.75));



// Exercise 3

// Write a js function that console.log the multiples of 23 less than 500 and at the end return the sum of all of them.

// arrayNumber = [0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 
// 345, 368, 391, 414, 437, 460, 483] 
// The sum that we need to get : 5313
​
function multiples () {
	let arrayNumber = [];
	for (let number = 0; number <= 500; number++){
		if (number % 23 == 0){
			arrayNumber.push(number)	
		} else {
			continue;
		}
	}
	return arrayNumber;
}
​
function sumNumbers () {
	let listNumbers = multiples();
	let sum = 0;
	for (let i = 0; i < listNumbers.length; i++){
		sum += listNumbers[i]
	}
	console.log(`The sum is ${sum}`)
}
​
sumNumbers();



  // Exercise 4

//   Create a function called checkBasket(). 
// It should:
// ask the user for the item he wants
// and let him know if it’s in the basket or not
// Hint: Use the in keyword inside the conditional

  let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
  }
  
  function checkBasket(basket, lookingFor) {
    let item = prompt("Which item do you want?");
    for(item in basket) {
      console.log(item);
       if(item === lookingFor) {
        return `${lookingFor} is in your basket`;
      }     
     }
     return `${lookingFor} is not in your basket`;
  }
  
  checkBasket();



  //Exercise 5

//   Create an array called shoppingList with the values “banana”, “orange”, and “apple”.
// Copy these two above objects into your js file
// Create a function called myBill() that takes no argument. 
// Depending on the list of items that you have in your array shoppingList and the prices listed in the prices object, 
// return the price spent on shopping.
// Call the function myBill()
// Bonus: In the function above, only add the price if the item is in stock (use the stock object).
// If the item is in stock, decrease the item’s stock by 1


let shoppingList = ["banana", "orange", "apple"];

 let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

function myBill() {
  let total = 0;
  for (let x = 0; x < shoppingnewList[x]; x++) {

      if(shoppingnewList[x] in prices) {
          total += prices;
      }
  }

  console.log(total);
  return total;
}

myBill();



//Exercise 6

// John and his family went on a holiday and went to 3 different restaurants.
// To tip the waiter a fair amount, John created a simple tip calculator (as a function).

// He likes to tip:
// 20% of the bill when the bill is less than $50,
// 15% when the bill is between $50 and $200,
// and 10% if the bill is more than $200.

// Ask John for the amount of the 3 bills. He has to enter a list of bills, each one separated by a comma.
// Create the program explained above.
// In the end, John would like to have 2 arrays:
// Containing all three tips (one for each bill).
// Containing all three final paid amounts (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)

let john = {
	bills = [150, 40, 260],
	calcTips = function() {
		this.tips = [];
		this.finalValues = [];

		for (let x = 0; x < this.bills.length; x++) {
			let percentage;
			let bill = this.bills[x];

			if (bill <= 50) {
				percentage = 0.2;
			} else if (bill >= 50 && bill <= 200) {
				percentage = 0.15;
			} else {
				percentage = 0.10;
			}

			this.tips[x] = bill * percentage;
			this.finalValues[x] = bill + bill * percentage;
		}
	}
}

function calcAverage(tips) {
    let sum = 0;
    for (x = 0; x < tips.length; x++) {
        sum = sum + tips[x];
    }
    return sum/tips.length;
}

john.calcTips();
console.log(john);

john.average = calcAverage(john.tips);
console.log(john);


//Exercise 7

function hotel_cost(night) {
  let cost = 140*night 
  let words = prompt(" How many nights do you want to stay in the hotel? "); 
  {
    if (" " !== night) {
            alert(" How many nights do you want to stay in the hotel? ");
    }
    return cost
}
}


	function plane_ride_cost(city) {
    let cost1 = 183
    let cost2 = 220 
    let cost3 = 300
    let words = prompt(" What is your destination? "); 
  {
    if ("London" == city) {
      return cost1
    }
    else if ("Paris" == city) {
      return cost2
    }
    else if (" " !== city) {
      alert(" What is your destination? "); 
}
    else {
      return cost3
    }
} 
}
		
function rental_car_cost(days) {
  let cost1 = 40*days/0.5
  let cost2 = 40*days
  let words = prompt(" How many days do you want to rent the car? ");
  {
    if (" " !== days) {
      alert(" How many days do you want to rent the car? "); 
    }

    else if (days >= 10) {
      return cost1
    }

      else {
        return cost2
    }
}
}


function total_vacation_cost(night, city, days) {
    let totalCost = $x + $y + $z;
    let $x = hotel_cost(night);
    let $y = plane_ride_cost(city);
    let $z = rental_car_cost(days);
    return totalCost 
}

total_vacation_cost();
