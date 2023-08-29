#!/usr/bin/node

const num = parseInt(process.argv[2]);
let row = '';

if (isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    row += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(row);
  }
}
