
let height = 7;
let width = (2 * height) - 1;

// FUNCTION to print the pattern of 'A' 
function letterA() {
    let n = width / 2, i, j;
    for (let i = 0; i < height; i++) {
        for (let j = 0; j <= width; j++) {
            if (j == n || j == (width - n) || (i == height / 2 && j > n && j < (width - n)))
                console.log("*");
            else
                console.log(" ");
        }
        console.log(" ");
        n--;
    }
}

letterA(7);