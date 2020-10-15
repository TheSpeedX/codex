function solution() {

  var nums = [1, 5, 12];

  for(var n = 10, Pn = 22; ; n+= 3, Pn+= n) {

    nums.push(Pn);

    for (var i = 0; i < nums.length; i++) {

      var a = Pn - nums[i];
      var b = nums[i];

      if (isPentagonal(a) && isPentagonal(Math.abs(a - b))) {
        console.log(Math.abs(a-b));
        return;
      }
    }
  }
}
