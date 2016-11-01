function fizzBuzz(num){ // this code works fine and passes all tests on andelab
	// divisible by only 3
	if ((num%3 === 0) && (num%5 !== 0)){
		return 'Fizz';
	}
	// divisible by only 5
	else if((num%5 === 0) && (num%3 !== 0)){
		return 'Buzz';
	}
	// divisible by both 3 and 5
	else if((num%5 === 0) && (num%3 === 0)){
		return 'FizzBuzz';
	}
	// divisible by neither 3 nor 5
	else if((num%5 !== 0) && (num%3 !== 0)){
		return num;
	}
}