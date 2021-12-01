function getSecondLargest(nums) {
    let greatest = 0;
    let uniq = [...new Set(nums)];
    for(let i = 0; i < uniq.length ; i++){
        if(uniq[i] > greatest){
            greatest = uniq[i];
        }
    }
    let y = uniq.indexOf(greatest);
    if (y > -1){
        t = uniq.splice(y , 1);
    }

    let secGreatest = 0;
    for(let i = 0; i < uniq.length ; i++){
        if(uniq[i] > secGreatest){
            secGreatest = uniq[i];
        }
    }
    
return secGreatest;
}

console.log(getSecondLargest([1,2,3]));