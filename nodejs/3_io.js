var fs = require('fs');
var path = process.argv[2];
var file = fs.readFileSync(path);
var file_string = file.toString();

var list = file_string.split('\n');
var newlines = (list.length - 1);
console.log(newlines);