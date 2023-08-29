#!/usr/bin/node

let num1 = parseInt(process.argv[2]);
let num2 = parseInt(process.argv[3]);
let i = 4;

if (process.argv.length < 4) {
  console.log(0);
} else {
  if (num2 > num1) {
    const temp = num2;
    num2 = num1;
    num1 = temp;
  }

  while (process.argv[i] !== undefined) {
    const temp = parseInt(process.argv[i]);
    if (temp > num1) {
      num2 = num1;
      num1 = temp;
    } else if (temp < num1 && temp > num2) {
      num2 = temp;
    }
    i++;
  }
  console.log(num2);
}
