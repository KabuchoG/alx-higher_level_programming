#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const n of list) {
    if (n === searchElement) {
      i++;
    }
  }
  return i;
};
