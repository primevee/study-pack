#!/usr/bin/node

const num = parseInt(process.argv[2]);
let i = 0;

if (isNaN(num) && process.argv.length > 2) {
  console.log('Missing number of occurrences');
} else if (!isNaN(num) && num > 0) {
  while (i !== num) {
    console.log('C is fun');
    i++;
  }
}
