<style>
<?php include 'SiteNao.css'; ?>
</style>

<div id="contenu0">

    <titre id="titre1">
        Connexion
    </titre>

    <div id="contenu10">
        <p id="titre1"> Adresse du robot</p>
		<form method="post" action="./traitement/traitement_page_3.php">
			<p>
				<label for="ip"> Ip :</label>
				<input type="text" name="ip" id="ip" placeholder="127.0.0.1" size="30" requiered/>
			</p>
			<p>
				<label for="code"> Code :</label>
				<input type="password" name="code" id="code" placeholder="123456789" size="30" requiered/>
			</p>
			<input id= "btn1" type="submit" value="Submit"/>
		</form>
    </div>
</div>