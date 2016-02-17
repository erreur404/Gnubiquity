var HMI = new Hmi();
var LEFT_JOY = new Joystick();
var RIGHT_JOY = LEFT_JOY;
var JOY_DELAY = 300; // every 300ms the joystick values are sent (at least)

var old_data = {
	'x':0,
	'y':0
};

function Joystick () {
	this.html = {};
	this.activation = false;
	this.x = 0;
	this.y = 0;
	this.html.onmousedown = function () {};
	this.html.onmousemove = function () {};
	this.html.onmouseleave = function () {};

	this.bind = function (htmlObj) {
		this.html = htmlObj;
		this.activation = false;
		this.x = 0;
		this.y = 0;
		// .bind(this)  : 'this' in the the methods will refer to 
		// this <-- object not the event target
		this.html.onmousedown = this.activate.bind(this);
		this.html.onmousemove = this.onMoveHandle.bind(this);
		this.html.onmouseleave = this.inhibate.bind(this);
	};
	
	this.activate = function () {
		console.log("joystick active")
		this.activation = true;
	};
	
	this.inhibate = function () {
		this.activation = false;
		this.x = 0;
		this.y = 0;
	};
	
	this.getActivation = function () {
		return this.activation;
	}
	
	this.getX = function () {
		return this.x;
	}
	
	this.getY = function () {
		return this.y;
	}
	
	this.onMoveHandle = function (event) {
		var joyPos = event.target.getClientRects()[0];
		// [-100;100] values normalization
		this.x = Math.round(100*(-(event.clientX - joyPos.left) + joyPos.width/2)/(joyPos.width/2));
		this.y = Math.round(100*(-(event.clientY - joyPos.top) + joyPos.height/2)/(joyPos.height/2));
		//console.log(this.x + " -- " + this.y);
	};
}

// class HMI
function Hmi () {
	this.getForward = function () {
		return LEFT_JOY.getY();
	};
	this.getTurn = function () {
		return RIGHT_JOY.getX();
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
	if (old_data.x != HMI.getForward() || old_data.y != HMI.getTurn())
	{
		actionButtonClick();
		old_data.x = HMI.getForward();
		old_data.y = HMI.getTurn();
	}
}, JOY_DELAY);