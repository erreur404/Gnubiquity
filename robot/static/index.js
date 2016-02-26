var HMI = new Hmi();
var LEFT_JOY = new Joystick();
var RIGHT_JOY = new Joystick();
var JOY_DELAY = 300; // every 300ms the joystick values are sent (at least)

var old_data = {
	'leftx':0,
	'lefty':0,
	'rightx':0,
	'righty':0
};

function posImage (event) {
	var imPos = event.target.getClientRects()[0];
	// [-100;100] values normalization
	xim = Math.round(100*(-(event.clientX - imPos.left) + imPos.width/2)/(imPos.width/2));
	yim = Math.round(100*(-(event.clientY - imPos.top) + imPos.height/2)/(imPos.height/2));
	//console.log(xim + " -- " + yim);
	actionButtonClick ();
}

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
		this.html.ontouchstart = this.activate.bind(this);
		this.html.ontouchmove = this.onTouchMoveHandle.bind(this);
		this.html.ontouchend = this.inhibate.bind(this);
	};
	
	this.activate = function () {
		//console.log("joystick active")
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
		this.x = Math.max(-100, Math.min(100, Math.round(100*(-(event.clientX - joyPos.left) + joyPos.width/2)/(joyPos.width/2))));
		this.y = Math.max(-100, Math.min(100, Math.round(100*(-(event.clientY - joyPos.top) + joyPos.height/2)/(joyPos.height/2))));
		//console.log(this.x + " -- " + this.y);
	};
	
	this.onTouchMoveHandle = function (event) {
		// to prevent the page to scroll when the user touches the joysticks
		event.preventDefault();
		var deb = document.getElementById("DEBUG");
		//deb.innerText = event.touches.length;
		//deb.innerText = "Touched !";
		/*
		for (var key in object)
		{
			res += ";" + key + "=" + object[key];
		}
		*/
		for (var finger=0; finger<event.touches.length; finger++)
		{
			var touch = event.touches[finger];
			// to check if the point of the touch event is the one targetting the joystick bounded to 'this'
			if (touch.target == this.html) {
				var joyPos = event.target.getClientRects()[0];
				// [-100;100] values normalization
				this.x = Math.max(-100, Math.min(100, Math.round(100*(-(touch.clientX - joyPos.left) + joyPos.width/2)/(joyPos.width/2))));
				this.y = Math.max(-100, Math.min(100, Math.round(100*(-(touch.clientY - joyPos.top) + joyPos.height/2)/(joyPos.height/2))));
				//console.log(this.x + " -- " + this.y);
				//deb.innerText = this.x + " -- " + this.y;
			}
		}
	};
}

// class HMI
function Hmi () {
	this.getJoystickChannel = function () {
		var res = {
			'leftx':LEFT_JOY.getX(),
			'lefty':LEFT_JOY.getY(),
			'rightx':RIGHT_JOY.getX(),
			'righty':RIGHT_JOY.getY()
		}
		return res;
	}
	
	this.getHeadX= function(){
		return xim;
	};
	this.getHeadY= function(){
		return yim;
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
	xim=0;
	yim=0;
};

function sendData () {
	var dataForm = new FormData();
	dataForm.append("idle", HMI.getPosIdle());
	dataForm.append("rest", HMI.getPosRest());
	dataForm.append("cue", HMI.getPosCue());
	dataForm.append("leftx", HMI.getJoystickChannel().leftx);
	dataForm.append("lefty", HMI.getJoystickChannel().lefty);
	dataForm.append("rightx", HMI.getJoystickChannel().rightx);
	dataForm.append("righty", HMI.getJoystickChannel().righty);
	
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
	if (old_data.leftx != HMI.getJoystickChannel().leftx ||
		old_data.lefty != HMI.getJoystickChannel().lefty ||
		old_data.rightx != HMI.getJoystickChannel().rightx ||
		old_data.righty != HMI.getJoystickChannel().righty)
	{
		actionButtonClick();
		old_data.leftx = HMI.getJoystickChannel().leftx;
		old_data.lefty = HMI.getJoystickChannel().lefty;
		old_data.rightx = HMI.getJoystickChannel().rightx;
		old_data.righty = HMI.getJoystickChannel().righty;
	}
}, JOY_DELAY);