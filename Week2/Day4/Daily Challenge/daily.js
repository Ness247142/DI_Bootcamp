

// Ask a user for several words (separated by commas).
// Push the words into an array.
// Console.log them, one per line, in a rectangular frame.
// For example, if the user gives you: 
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]

// let words = prompt(" Give me a few words ");
//     words = words.split(" ");

// // function frame (){
// //     for(x = 0; x <= words.length; x++){

// //       stars = (" * ") + words[x] + (" * ")
// //     }
    
// //    console.log(stars)

// // }


let sentence = prompt(" Give me a few words for today ");

let words = sentence.split(" ");

let starRight = " *";

let starLeft = "* ";

let space = " ";

let temp = 0;


function frame (){

    for ( let x = 0; x < words.length; x++ ) {
        if ( temp < words[x].length ) {
            temp = words[x].length;
        }
    }
    
    temp +=4; 
    let star = "*";
    for ( let y = 0; y < temp; y++ ) {
        star += "*";
    }

    console.log(star);

    for ( let x = 0; x < words.length; x++ ) {
        let difference = temp-words[x].length-3;
        console.log(starRight + words[x] + space.repeat(difference) + starLeft);
    }

    console.log(star); 
}

frame();


