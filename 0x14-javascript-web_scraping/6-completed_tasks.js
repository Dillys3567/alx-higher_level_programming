#!/usr/bin/node
const request = require('request');
request(process.argv[2], function(err, resp, body) {
	if (err)
		console.log(err);
	else if (resp.statusCode === 200) {
		const completed = {}
		const jsonBody = JSON.parse(body);
		for (const i in jsonBody) {
			todo = jsonBody[i];
			if (todo.completed === true)
				if (completed[todo.userId] === undefined)
					completed[todo.userId] = 1;
			else
				completed[todo.userId]++;
		}
		console.log(completed);
	}
	else {
		console.log(resp.statusCode);
	}
});
