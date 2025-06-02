/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var filtrado=[];
    for(var i=0;i<arr.length;i++){
        if(fn(arr[i],i)){
            filtrado.push(arr[i]);
        }
    }
    return filtrado;
};