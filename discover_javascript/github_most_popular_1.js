var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 1e4494c05723340138ecb8ec379d6c1988e39ced'
    }
};

var req = https.request(options, function(res) {
	res.on('data', function(d) {
		process.stdout.write(d);
	    });
    });
req.end();

req.on('error', function(e) {
	console.error(e);
    });