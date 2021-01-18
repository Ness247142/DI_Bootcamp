let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift(); // Remove "Banana" from the array.

fruits.sort(); // Sort the array in order.

fruits.push("Kiwi"); // Put “Kiwi” at the end of the array.

fruits.splice(0, 1); // Remove “Apples” from the array. 

fruits.reverse(); // Reverse the order of the elements in an array.

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]) // Get fruit "Oranges"
