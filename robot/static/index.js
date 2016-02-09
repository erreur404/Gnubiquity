var HMI = new Hmi();
var LEFT_JOY = [0, 0];
var RIGHT_JOY = [0, 0];
var JOY_DELAY = 300; // every 300ms the joystick values are sent (at least)

// class HMI
function Hmi () {
	this.getForward = function () {
		return LEFT_JOY[1];
	};
	this.getTurn = function () {
		return RIGHT_JOY[0];
	};
	////////////////////////////
	this.getMessage = function () {
		message=document.getElementById("text").value;
		document.getElementById("text").value = "";
		return message.replace(/[éèêë]/g, "e").replace(/[ç]/g, "c").replace(/[àâä]/g, "a").replace(/[ïì]/g, "i").replace(/[ùûü]/g, "u").replace(/[ôöò]/g, "o");
	}
	////////////////////////////
	this.getPosRest = function () {
		var valt = this._posRestToggle;
		this._posRestToggle = false;
		return valt;
	}
	this._posRestToggle = false;
	this._posRestPressedHandle = function (e) {
		this._posRestToggle = true;
		actionButtonClick ();
	};
	///////////////////////////
	this.getPosIdle = function () {
		var vali = this._posIdleToggle;
		this._posIdleToggle = false;
		return vali;
	};
	this._posIdleToggle = false;
	this._posIdlePressedHandle = function (e) {
		this._posIdleToggle = true;
		actionButtonClick ();
	};
	////////////////////////////
	this.getPosCue = function () {
		var valc = this._posCueToggle;
		this._posCueToggle = false;
		return valc;
	};
	this._posCueToggle = false;
	this._posCuePressedHandle = function (e) {
		this._posCueToggle = true;
		actionButtonClick ();
	};
	
}



function actionButtonClick () {
	sendData();
};

function sendData () {
	var dataForm = new FormData();
	dataForm.append("avancer", HMI.getForward());
	dataForm.append("idle", HMI.getPosIdle());
	dataForm.append("rest", HMI.getPosRest());
	dataForm.append("cue", HMI.getPosCue());
	dataForm.append("tourner", HMI.getTurn());
	
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "/command", true);
	xmlhttp.send(dataForm);
};

function sendTTS () {
	var dataForm = new FormData();
	dataForm.append("message", HMI.getMessage());
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "/say", true);
	xmlhttp.send(dataForm);
}

setInterval(function(){
	if (joyDPressed = true || joyGPressed = true)
	{
		actionButtonClick();
	}
}, JOY_DELAY);