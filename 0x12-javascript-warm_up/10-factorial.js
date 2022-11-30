#!/usr/bin/node
function factorial (a) {
  let res = parseInt(a);
  let fact = 1;
  for (let i = 1; i <= res; i++) {
    fact *= i;
  } console.log(fact);
}
factorial(process.argv[2]);
