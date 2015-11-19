// For hackerrank.com

// Part 1
function processData(input) {
    var len = input.split('\n')[0];
    var arrayString = input.split('\n')[1];
    var array = arrayString.split(" ");
    var newElt = Number(array[len-1]);
    for (var i = len-1; i >= 0; i--) {
        if (newElt > Number(array[i-1]) || i === 0) {
            array[i] = newElt;
            console.log(array.join(" "));
            break;
        } else {
            array[i] = array[i-1];
            console.log(array.join(" "));
        }
    }
}

// Part 2
function processData2(input) {
    var len = input.split('\n')[0];
    var array = input.split('\n')[1].split(' ');
    var i, j;
    for (i = 0; i < len; i++) {
        current = Number(array[i]);
        for (j = i-1; j >= 0 && Number(array[j]) > current; j--) {
            array[j+1] = array[j];
        }
        array[j+1] = current;
        if (i > 0) {
            console.log(array.join(' '));
        }
    }
} 
