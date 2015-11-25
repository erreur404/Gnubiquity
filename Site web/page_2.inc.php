<style>
<?php include 'SiteNao.css'; ?>
</style>
<?php
include 'page_2.inc.js';

?>
<div id="contenu0">

    <titre id="titre1">
        Essai
    </titre>

    <div id="contenu10">
		<p>
			<label for="ip"> Ip :</label>
			<input type="text" name="ip" id="ip" placeholder="127.0.0.1" size="30" requiered/>
		</p>
		<p>
			<label for="message"> Message :</label>
			<input type=text name=message id=message placeholder="Hello World" value=""/>
		</p>
		<p>
		<button type=button onclick=Say()>Envoi!</button>
		</p>
    </div>
</div>