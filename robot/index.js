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