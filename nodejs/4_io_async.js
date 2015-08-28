//console.log(process.argv);

var fs = require('fs');
var path = process.argv[2];

fs.readFile(path, function countLines(error, fileContents) {
    var list = fileContents.toString().split('\n');
    var lines = list.length - 1;
    console.log(lines);
});