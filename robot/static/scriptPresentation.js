var moveDataProto = {
    getPosIdle :false,
    getPosRest :false,
    getPosCue :false,
    leftx :0,
    lefty :0,
    rightx :0,
    righty :0,
    getHeadX :0,
    getHeadY :0
}


function fake_sendData (moveData) {
	var dataForm = new FormData();
	dataForm.append("idle", moveData.getPosIdle);
	dataForm.append("rest", moveData.getPosRest);
	dataForm.append("cue", moveData.getPosCue);
	dataForm.append("leftx", moveData.leftx);
	dataForm.append("lefty", moveData.lefty);
	dataForm.append("rightx", moveData.rightx);
	dataForm.append("righty", moveData.righty);
	dataForm.append("yaw", moveData.getHeadX);
	dataForm.append("pitch", moveData.getHeadY);

	
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "/command", true);
	xmlhttp.send(dataForm);
};

function fake_sendTTS (txt) {
	var dataForm = new FormData();
	dataForm.append("message", txt);
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "/say", true);
	xmlhttp.send(dataForm);
}

function say(txt) {
    fake_sendTTS(txt)
}

function run() {
    var timeline = 0; // en ms
    setTimeout(function () {
        say("Bonjour");
    }, timeline);
    timeline += 1500;
    setTimeout(function () {
        say("Depuis la dernière fois, le projet a Gnubiquity a bien avancé. Je vais vous présenter mes nouvelles fonctionnalités !");
        moveDataProto.getHeadX = -100;
        fake_sendData(moveDataProto);
        moveDataProto.getHeadX = 0;
    }, timeline);
    timeline += 6000;
    setTimeout(function () {
        say("Comme vous avez pu le constater, je peux désormais parler pour interragir avec vous, humains");
        moveDataProto.getHeadX = 100;
        fake_sendData(moveDataProto);
        moveDataProto.getHeadX = 0;
        moveDataProto.getHeadX = 100;
        fake_sendData(moveDataProto);
        moveDataProto.getHeadX = 0;
    }, timeline);
    timeline += 4500;
    setTimeout(function () {
        say("Je peux aussi lever le bras pour attirer votre attention");
    }, timeline);
    timeline += 2000;
    setTimeout(function () {
        moveDataProto.getPosCue = true;
        fake_sendData(moveDataProto);
        moveDataProto.getPosCue = false;
    }, timeline);
    timeline += 2500;
    setTimeout(function () {
        moveDataProto.getPosIdle = true;
        fake_sendData(moveDataProto);
        moveDataProto.getPosIdle = false;
    }, timeline);
    timeline += 2000;
    setTimeout(function () {
        say("Je peux marcher et me tourner dans tous les sens. Par exemple je peux avancer pendant 1 secondes et tourner.");
    }, timeline);
    timeline += 5000;
    setTimeout(function () {
        moveDataProto.lefty = 100;
        fake_sendData(moveDataProto);
        setTimeout(function () {
            moveDataProto.lefty = 0;
            fake_sendData(moveDataProto);
        }, 1000);
    }, timeline);
    timeline += 1500;
    setTimeout(function () {
        moveDataProto.rightx = 100;
        fake_sendData(moveDataProto);
        setTimeout(function () {
            moveDataProto.rightx = 0;
            fake_sendData(moveDataProto);
        }, 1000);
    }, timeline);
    timeline += 1500;
    setTimeout(function () {
        say("Et voilà !");
    }, timeline);
}