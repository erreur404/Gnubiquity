
	  var audio_context;
	  var recorder;
	  function startUserMedia(stream) {
		var input = audio_context.createMediaStreamSource(stream);
	
		
		input.connect(audio_context.destination);
		
		recorder = new Recorder(input);

	  }
	  
	  function toggleRecording( e ) {
		if (e.classList.contains("recording")) {
			// stop recording
			recorder && recorder.stop();
			console.log("toggle class");
			e.classList.remove("recording");
			recorder && recorder.stop();

		
			// create WAV download link using audio data blob
			createDownloadLink();
		
			recorder && recorder.clear();
		
		} else {
			// start recording
			if (!recorder)
				console.log("je passe ici à chaques fois !");
				//return;
			e.classList.add("recording");
			recorder && recorder.record();

		}
	   }
	  function createDownloadLink() {
		recorder && recorder.exportWAV(function(blob) {
		  var url = URL.createObjectURL(blob);
		  var oReq = new XMLHttpRequest();
		  oReq.open("POST", "/son", true);
		  oReq.onload = function (oEvent) {
			// Uploaded.
		  };

		  oReq.send(blob);
		});
	  }
	  window.onload = function init() {
		try {
		  // moz shim
		  window.AudioContext = window.AudioContext || window.mozAudioContext || window.webkitAudioContext;
		  navigator.getUserMedia = navigator.getUserMedia || navigator.mediaDevices.getUserMedia || navigator.webkitGetUserMedia;
		  window.URL = window.URL || window.mozURL || window.webkitURL;
		  
		  audio_context = new AudioContext;
	
		} catch (e) {
		  alert('No web audio support in this browser!');
		}
		
		navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
		
		});
		};