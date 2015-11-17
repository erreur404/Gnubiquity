

    <!DOCTYPE html>
    <html>
        <head>
		<title>App RS</title>
        <meta content="info">
        <meta charset="UTF-8">
		<link rel="stylesheet" href="SiteNao.css" />
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
						$encours = array("1", "0", " ",);

						if (!isset($_GET["page"])) {
							$page = 0;
						} else {
							$page = $_GET["page"];
						}
						$encours[$page] = "encours";

						echo "<li><a class=\"btn_menu $encours[0]\"href=\"?page=0\">Accueil</a></li>\n";
						echo "<li><a class=\"btn_menu $encours[1]\"href=\"?page=1\">Connexion</a></li>\n";
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

