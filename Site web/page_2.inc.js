<script>

function Say(){
	var ip=document.getElementById("ip").value;
	//alert(ip);
	var message = document.getElementById("message").value;
	//alert(message);
	message = message.replace(/[ийкл]/g, "e").replace(/[з]/g, "c").replace(/[авд]/g, "a").replace(/[по]/g, "i").replace(/[ыщь]/g, "u").replace(/[фцу]/g, "o");;
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