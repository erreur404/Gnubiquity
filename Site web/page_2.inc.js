<script>

function Say(){
	var ip=document.getElementById("ip").value;
	//alert(ip);
	var message = document.getElementById("message").value;
	//alert(message);
	message = message.replace(/[����]/g, "e").replace(/[�]/g, "c").replace(/[���]/g, "a").replace(/[��]/g, "i").replace(/[���]/g, "u").replace(/[���]/g, "o");;
	//alert(message);	
	send(ip, message);
}

function send(ip, sendingData) {
	var sendingTo = "http://"+ip;


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
</script>