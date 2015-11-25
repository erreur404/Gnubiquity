var sendingData = {
	'citron':3,
	'melon':2,
	'citrouille':1
}

var sendingTo = "http://127.0.0.1:9999"

var execute = function () {
	var loading = $.ajax(
		{
			'url': sendingTo,
			'data': sendingData,
			'dataType': "json",
			'method': "POST",
			'Access-Control-Allow-Origin': *,
			'error': function() {
				console.log(loading);
			},
			'complete': function () {
				//alert("sucess !");
				console.log(loading);
			}
		}
	);
}

var exec_cute = function () {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', sendingTo, true);
	xhr.onloadend = function (err) {console.log(err);};
	xhr.send();
}