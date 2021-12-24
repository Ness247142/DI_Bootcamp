
// //Exercise 1
// Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.

// Give to all paragraphs inside the <article> tag the class of para_article.
let paragraph = document.getElementsByTagName("p")
for (i = 0; i < paragraph.length; i++)
{
paragraph[i].classList.add("para_article")
}
console.log(paragraph[1]);

// Remove the last paragraph in the article.
let lastParagraph = document.body.firstElementChild.lastElementChild;
lastParagraph.remove();

// Add an event listener so that when you click on the h2, it is removed from the DOM.
let headingTwo = document.getElementById("h2")
headingTwo.addEventListener("click", remove_h2)
function remove_h2 (event){
    headingTwo.target.remove();
}

// Set the font size of the h1 to be a random pixel size from 0 to 100.
let headingOne = document.body.firstElementChild.textContent;
function headingOne () {
    for (i = 0; i <= 100; i++)
{
headingOne[i].style.fontSize = "x-large"
}
}

// Hide the 1st paragraph, when it’s clicked. (use the display property )
let paragraph1 = headingTwo.body.firstElementChild.children[2];

paragraph1.addEventListener("click", hide_p1)
function hide_p1 (event) {
    event.target.style.display = "none";
}

// Get the values from the inputs and append them to the end of the html, inside a table.
function addRow() {
    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(-1);
  
    // Insert a cell in the row at index 0
    let newCell = newRow.insertCell(0);
  
    // Append the values of the inputs to the cell
    let inputValues = document.getElementsByTagName("input").value;
    newCell.appendChild(inputValues);
  }
  addRow("my-table");
