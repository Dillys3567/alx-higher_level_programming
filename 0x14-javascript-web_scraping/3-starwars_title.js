#!/usr/bin/node
const request = require('request');
const epi = process.argv[2];
const path = "https://swapi-api.alx-tools.com/api/films/";
request(path + epi, function(err, resp, body) {
	if (err)
		console.log(err);
	else if (resp.statusCode === 200) {
		const respJson = JSON.parse(body);
		console.log(respJson.title);
	}
	else {
		console.log(response.statusCode);
	}
});
