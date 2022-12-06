#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 1; i <= this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
