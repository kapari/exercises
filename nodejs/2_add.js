// Add unknown # of integers
// [node, filename, integer, integer...]
// console.log(process.argv);
var input = process.argv;

function add_any(argv_input) {
    var output = 0;
    for (var i = 2; i < argv_input.length; i++) {
        output += Number(argv_input[i]);
    }
    return output;
}

console.log(add_any(input));