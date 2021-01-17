let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift(); 
console.log( fruits );// Remove "Banana" from the array.

fruits.sort();
console.log(fruits); // Sort the array in order.

fruits.push("Kiwi"); // Put “Kiwi” at the end of the array.

fruits.splice(1, 1); // Remove “Apples” from the array. 

fruits.reverse(); // Reverse the order of the elements in an array.

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(fruits[0][1][0]) //Get fruit "Oranges"