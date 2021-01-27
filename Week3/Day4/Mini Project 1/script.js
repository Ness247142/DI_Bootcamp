
//                       ----STEPS : structure----
// Create the structure: need a loop in JS that add 2000 divs
// We need to use some classes to add grid on CSS
// Create 21 div, using a loop and assign to each one of them a different background color

//                   ----STEPS : retrieving each color----
// Paint: I need to select/choose the color
// Click on div - event listener - click
// All the divs need to be clickable
// Means : assign some event to ALL the div - using a loop
// Click on the div to select the color
// Store the background-color in a variable
// Value of the background-color
// Need to use the style attribute to retrieve the background color of each div

//                              ---STEPS----
// 1. add this color to whatever div I click on
// 2. Make all the div of the grid clickable
// 3. Use event mousedown to click on the grid
// 4. To add the color to the grid : change the background of the grid - use the style attribute
// 5. grid.addEventListener("mousedown", paint)
// 6. grid.addEventListener("mouseover", paint)
//    function paint (event) {
//         //use the event object to change the background color of the grid
//         //IMPORTANT : USE THE EVENT OBJECT
//    }
//    Set a variable in your onmousedown, and clear it in your onmouseup.
//    Then, in your onmousemove, check the variable. If it's set the mouse is down, if not it's up.


let color = null;
let mousedown = false;

let colors = document.querySelectorAll("#colors > *");
let button = document.getElementsByTagName("button")[0];
let body = document.getElementsByTagName("body")[0];
let blocks = document.querySelectorAll("#blocks > *");

for (brush of blocks) {
    brush.addEventListener("mousedown", function (event) {
        if (color != null) event.target.style.backgroundColor = color;
    });
    brush.addEventListener("mouseover", function (event) {
        if (mousedown && color != null) event.target.style.backgroundColor = color;
    });
    console.log(brush + blocks);
}

for (click of colors) {
    click.addEventListener("click", function (event) {
        color = event.target.style.backgroundColor;
        console.log(click + colors);
    });
}

button.addEventListener("click", function () {
    for (brush of blocks) {
        brush.style.backgroundColor = "white";
        console.log(button);
    }
});

body.addEventListener("mousedown", function () {
    mousedown = true;
    console.log(body);
})

body.addEventListener("mouseup", function () {
    mousedown = false;
    console.log(body);
})
