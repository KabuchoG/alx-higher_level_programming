#!/usr/bin/node
exports.esrever = function (list) {
  const listn = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listn.push(list[i]);
  }
  return listn;
};
