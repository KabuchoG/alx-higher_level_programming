#!/usr/bin/node
const list = require('./100-data.js').list;

const nl = list.map((m, idx) => m * idx);
console.log(list);
console.log(nl);
