function dataTypes (data) { // doesn't pass tests yet
	// check for null
	if (data === null) {
		return 'null';

	}
	// check for undefined
	else if (data === undefined) {
		return 'undefined';
	}
	// check for string
	else if (typeof data === 'string') {
		return data.length;
	}
	// check for numbers
	/*
	if (!isNaN(parseFloat(data)) && isFinite(data)) {
		alert(data);
	}
	*/
	else if (!isNaN(data)) {
		switch(true){
			case (data<100): //less than 100
				return 'less than 100';
				break;

			case (data==100): // equal to 100
				return 'equal to 100';
				break;

			case (data>100): // greater than 100
				return 'greater than 100';
				break;

		} // end of switch...case statement
		

	}
	// check for boolean true and false value - not yet sure of how to implement this
	else if(data === true){
		return 'True: ' + data;
	}
	else if(data === false){
		return 'False: ' + data;
	}

	// check for arrays - not recognised as arrays for arrays of length less than 2
	/*
	else if (data instanceof Array) {
		alert(data.length);
	}
	*/
	else if(data.constructor.toString().indexOf("Array") > -1){
		return "An array";
	}
	// check for functions
	else if(data instanceof Function){
		return data(true);
	}

	else {
		return 'I dont know';
	}
}
