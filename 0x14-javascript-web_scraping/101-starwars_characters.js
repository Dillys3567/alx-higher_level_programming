#!/usr/bin/node
const requests = require('request');
const path = "https://swapi-api.alx-tools.com/api/films/";
const id = process.argv[2];
requests.get(path + id, function(err, resp, body) {
	if (err)
		console.log(err);
	else if (resp.statusCode === 200) {
		const jsonBody = JSON.parse(body);
		characters = jsonBody["characters"];
		printChars(characters, 0);
	}
});

function printChars(chars, index) {
	requests(chars[index], function(err, resp, body) {
		if (!err) {
			console.log(JSON.parse(body).name);
			if (index + 1 < chars.length) {
				printChars(chars, index + 1);
			}
		}
	});
}
