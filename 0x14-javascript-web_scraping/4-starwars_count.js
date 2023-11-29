#!/usr/bin/node
const request = require('request');
request(process.argv[2], function(err, resp, body) {
	if (err)
		console.log(err);
	else if (resp.statusCode === 200) {
		const results = JSON.parse(body).results;
		console.log(results.reduce((count, movie) => {
			return movie.characters.find((chara) => chara.endsWith('/18/')) ? count + 1 : count;
		}, 0));
	}
});
