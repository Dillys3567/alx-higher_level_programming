#!/usr/bin/node
const l = process.argv.length;
if (l === 2) {
  console.log('Missing number of occurrences');
} else {
  const n = Number(process.argv[2]);
  let i = 0;
  while (i < n) {
    console.log('C is fun');
    i++;
  }
}
