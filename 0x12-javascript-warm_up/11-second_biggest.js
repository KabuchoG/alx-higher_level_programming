#!/usr/bin/node
function secondLargest () {
  const numbers = process.argv;
  let temp = 0;
  let fin = 0;
  if (numbers.length < 3 || numbers.length === 3) {
    console.log(0);
  } else {
    for (let i = 2; i < numbers.length; i++) {
      if (parseInt(numbers[i]) > temp) {
        temp = numbers[i];
      }
    }
    for (let i = 2; i < numbers.length; i++) {
      if (numbers[i] !== temp) {
        if (parseInt(numbers[i]) > fin) {
          fin = numbers[i];
        }
      }
    } console.log(fin);
  }
}
secondLargest();
