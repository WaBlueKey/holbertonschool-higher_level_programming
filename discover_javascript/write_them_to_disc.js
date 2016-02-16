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
	streamToString(res, writeToDisc);
});

req.end();

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	    chunks.push(chunk);
	});
    stream.on('end', () => {
	    cb(chunks.join(''));
	});
}

var writeToDisc = function(jsonString){
    var fs = require('fs');
    fs.writeFile('/tmp/29', jsonString, function (err) {
      if (err) return console.log(err);
      console.log('The file was saved!');
    });
};

req.on('error', function(e) {
	console.error(e);
    });