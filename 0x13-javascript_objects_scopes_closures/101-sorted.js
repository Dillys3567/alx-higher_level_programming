#!/usr/bin/node
const dict = require('./101-data').dict;

const list = Object.entries(dict);
const vals = Object.values(dict);
const unique = [...new Set(vals)];
const newD = {};
for (const j in unique) {
  const l = [];
  for (const k in list) {
    if (list[k][1] === unique[j]) {
      l.push(list[k][0]);
    }
  }
  newD[unique[j]] = l;
}
console.log(newD);
