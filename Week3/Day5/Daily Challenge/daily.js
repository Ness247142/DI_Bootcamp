
// FUNCTION to print the pattern of the letter 'A' in stars

function letter_A() {
  for (let i = 0; i < 7; i++) {
    if (i == 0) {
      console.log('  ***');
    } else if (i == 1) {
      console.log(' *   *');
    } else if (i == 2) {
      console.log(' *   *');
    } else if (i == 3) {
      console.log(' *****');
    } else if (i == 4) {
      console.log(' *   *');
    } else if (i == 5) {
      console.log(' *   *');
    } else if (i == 6) {
      console.log(' *   *');
    }
  }
}

letter_A();
