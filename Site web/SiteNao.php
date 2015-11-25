

    <!DOCTYPE html>
    <html>
        <head>
		<title>App RS</title>
        <meta content="info">
        <meta charset="ASCII">
		<link rel="stylesheet" href="SiteNao.css" />
		<script src="jquery-1.11.3.min.js" type="text/javascript"></script>
		</head>
        <body>
            <div id="fond">
                <div id="titre">
                    <span>

                    App RS

                    </span>
                </div>
				<div id="menu">
					<ul id="lemenu">
						<?php
						$encours = array("", "", "");

						if (!isset($_GET["page"])) {
							$page = 0;
						} else {
							$page = $_GET["page"];
						}
						$encours[$page] = "encours";

						echo "<li><a class=\"btn_menu $encours[0]\"href=\"?page=0\">Accueil</a></li>\n";
						echo "<li><a class=\"btn_menu $encours[1]\"href=\"?page=1\">Connexion</a></li>\n";
						echo "<li><a class=\"btn_menu $encours[2]\"href=\"?page=2\">Essai</a></li>\n";
						?> 
					</ul>
				</div>

            <div id="contenu">
                <?php
                if (file_exists("page_" . $page . ".inc.php")) {
                    include("page_" . $page . ".inc.php");
                }
                ?>
            </div>
                <div id="pied">
				<span>Polytech Annecy-Chambéry - APP RS 2017</span>
				</div>
            </div>
        </body>
    </html>

