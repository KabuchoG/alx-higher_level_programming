#!/usr/bin/node
function largest () {
  const numbers = process.argv;
  let temp = 1;
  if (numbers.length < 3 || numbers.length === 3) {
    console.log(0);
  } else {
    for (let i = 2; i < numbers.length; i++) {
      if (parseInt(numbers[i]) > temp) {
        temp = numbers[i];
      }
    } console.log(temp);
  }
}
largest();
