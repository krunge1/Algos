// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

// Examples:

// pushFront([5,7,2,3], 8) => [8,5,7,2,3]
// pushFront([99], 7) => [7,99]

let arr = [5,7,2,3]

function pushFront(arr, value){
    for (i=arr.length; i>0; i--){
        arr[i]=arr[i-1]
    }
    arr[0] = value
    return arr;
}

// console.log(pushFront(arr, 1))

// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!

// Examples:

// popFront([0,5,10,15]) => 0 returned, with [5,10,15] printed in the function
// popFront([4,5,7,9]) => 4 returned, with [5,7,9] printed in the function
function popFront(arr){
    let first = arr[0]
    for (i=0; i<arr.length; i++){
        arr[i]=arr[i+1]
    }
    arr.length= arr.length-1
    console.log(arr)
    return first
}

console.log(popFront(arr))

// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

// Examples:

// insertAt([100,200,5], 2, 311) => [100,200,311,5]
// insertAt([9,33,7], 1, 42) => [9,42,33,7]
function insertAt(arr, location, value) {
    for (i=arr.length; i>location-1; i--){
        arr[i]=arr[i-1]
    }
    arr[location-1] = value
    return arr;
}

// console.log(insertAt(arr, 15, 4))