var sendingData = {
	'citron':3,
	'melon':2,
	'citrouille':1
}

var sendingTo = window.location+"/command/"

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

var createDebugWindow = function () {
	var wind = document.createElement("iframe");
	wind.id = "debugWindow";
	wind.style.position="fixed";
	wind.style.top = "0px";
	wind.style.left = "0px;"
	wind.style.zindex = "9999";
	wind.style.backgroundColor = "rgba(255,255,255,0.5)";
	wind.style.height = "90%";
	document.body.appendChild(wind);
}

var exec_cute = function () {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', sendingTo, true);
	xhr.onloadend = function (err) {
		console.log(err.target.responseText);
		document.getElementById("debugWindow").contentDocument.write(err.target.responseText);
	};
	xhr.send(sendingData.toString());
}

setTimeout(
	function (e) {
		createDebugWindow();
	},
	3000
);