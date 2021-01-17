function mixUp(mix, pod) {
    return pod.slice(0, 2) + mix.slice(2) + " " + mix.slice(0, 2) + pod.slice(2);
  }
  
console.log(mixUp('mix', 'pod'));

// Create a variable which value is the concatenation of the two strings (separated by a space) slicing out and swapping the first 2 characters of each.