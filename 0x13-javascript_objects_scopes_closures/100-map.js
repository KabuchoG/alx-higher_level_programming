#!/usr/bin/node
const list = require('./100-data.js').list;

const nl = list.map((m) => m * list.indexOf(m));
console.log(list);
console.log(nl);
