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
		for (const i in characters) {
			requests.get(characters[i], function(err, resp, body) {
				if (err)
					console.log(err);
				else if (resp.statusCode === 200) {
					const cha = JSON.parse(body);
					console.log(cha.name);
				}
		})
	}
	}});
