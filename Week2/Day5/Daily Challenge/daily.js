

// You know the infamous song “99 Bottles of Beer?”

// You need to generate in JavaScript the lyrics to the song 99 Bottles of Beer as an output.

// Ask the user to input a starting number of bottles of beer, and start the bottles falling.
// But instead of 1 falling each time, the number falling goes up by one each time.


let sentence = prompt("Between 0 to 100; how many bottles of beer do you want?");

let maxBottles = 99;

let x = 1; 

let number = parseInt(sentence);


while(number > 0) {

    console.log(`${number} bottels of beer on the wall,`);

    console.log(`${number} bottels of beer on the wall,`);

    console.log(`${number} bottels of beer.`); 

    if (x == 1) {

        console.log(`Take ${x} down, pass it around.`);

    } else {

        console.log(`Take ${x} down, pass them around.`);
    }

    number -= x;

    x++;
}

console.log("0 bottels of beer on the wall.");

console.log("Let's go to the store and buy new bottles of beer.");



// Incomplete Solution

// let number = prompt(" Give me a number between 1 and 100 ");
// let bottles;
// let bottle;

// function beerSong() {  
//   for (let x = 99; x >= 0; x --) {
//     let y = "bottle";

//    if (x <= 0) {
//     bottleRest = "bottles";
//       console.log("No more " + y + " of beer on the wall."); 
//       console.log("No more " + y + " of beer,");
//       console.log("Go to the store and buy new bottles of beer");
//    }
//    else if (x == 1) {
//     bottleRest = "bottle";
//        console.log(x + " " + y + " of beer on the wall");
//        console.log(x + " " + y + " of beer,");
//        console.log("Take one down, pass it around,");
//    }
//    else if (x >= 2) {
//       bottleRest = "bottles";
//        console.log(x + " " + y + " of beer on the wall");
//        console.log(x + " " + y + " of beer,");
//        console.log("Take " + x +  " down, pass them around,");
 
//    }
//   }
// }

//    beerSong();
