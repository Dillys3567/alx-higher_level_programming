#!/usr/bin/node
//display status of get
const request = require('request');
request.get(process.argv[2]).on('response', function(resp) {
	console.log('code: ', resp.statusCode);
});
