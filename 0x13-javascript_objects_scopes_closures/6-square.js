#!/usr/bin/node

const Square1 = require('./5-square');

class Squarewithcar extends Square1 {
  charPrint (c) {
    let row = '';
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.width; i++) {
      row += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Squarewithcar;
