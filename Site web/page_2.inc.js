<script>

var sendingData = "";
var sendingTo = "";

function Say(){
	ip=document.getElementById("ip").value;
	sendingTo="http://"+ip;
	alert(sendingTo);
	message = document.getElementById("message").value;
	//alert(message);
	sendingData = message.replace(/[����]/g, "e").replace(/[�]/g, "c").replace(/[���]/g, "a").replace(/[��]/g, "i").replace(/[���]/g, "u").replace(/[���]/g, "o");
	//alert(sendingData);	
	execute();
}

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

var exec_cute = function () {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', sendingTo, true);
	xhr.onloadend = function (err) {console.log(err);};
	xhr.send();
}

</script>