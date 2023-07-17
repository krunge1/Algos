// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

// Examples:

// pushFront([5,7,2,3], 8) => [8,5,7,2,3]
// pushFront([99], 7) => [7,99]

// let arr = [6,5,7,2,3]

function pushFront(arr, value){
    for (let i=arr.length; i>0; i--){
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
    for (let i=0; i<arr.length; i++){
        arr[i]=arr[i+1]
    }
    arr.length= arr.length-1
    console.log(arr)
    return first
}

// console.log(popFront(arr))

// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

// Examples:

// insertAt([100,200,5], 2, 311) => [100,200,311,5]
// insertAt([9,33,7], 1, 42) => [9,42,33,7]
function insertAt(arr, location, value) {
    for (let i=arr.length; i>location-1; i--){
        arr[i]=arr[i-1]
    }
    arr[location-1] = value
    return arr;
}

// console.log(insertAt([9,33,7], 1, 42))

// BONUS: Remove At
// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).

// Examples:

// removeAt([1000,3,204,77], 1) => 3 returned, with [1000,204,77] printed in the function
// removeAt([8,20,55,44,98], 3) => 44 returned, with [8,20,55,98] printed in the function

function removeAt(arr, location){
    let removedValue = arr[location]
    for (let i=location; i<arr.length; i++){
        arr[i]=arr[i+1]
    }
    console.log(removedValue)
    arr.length = arr.length-1
    return arr;
}

// console.log(removeAt([8,20,55,44,98], 3))

// BONUS: Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.

// Examples:

// insertAt([1,2,3,4]) => [2,1,4,3]
// insertAt(["Brendan",true,42]) => [true,"Brendan",42]

function swapPairs(arr) {
    for (let i=0; i<arr.length-1; i+=2){
        tempValue = arr[i]
        arr[i] = arr[i+1]   
        arr[i+1] = tempValue
    }
    return arr;
}

    // console.log(swapPairs([1,2,3,5,4,6,7]))

// Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!

// Examples:

// removeDupes([-2,-2,3.14,5,5,10]) => [-2,3.14,5,10]
// removeDupes([9,19,19,19,19,19,29]) => [9,19,29]

function removeDups(arr) {
    let newArray = [];
    let previousValue = null;
    for (let i = 0; i < arr.length; i++) {
        
    if (arr[i] !== previousValue) {
        newArray.push(arr[i]);
        previousValue = arr[i];
    }
    }
    
    return newArray;
}
console.log(removeDups([-2,-2,3.14,5,5,10]))
console.log(removeDups([9,19,19,19,19,19,29]))