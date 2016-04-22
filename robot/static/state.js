var progress = {
    "state.js":100,
    "soutenance":{
        "demo":50,
        "texte/structure":37,
        "diapo":0
    },
    "video":{
        "capture":25,
        "montage":0,
        "post-prod":0
    },
    "fonctionnalités":{
        "Interface":{
            "contrôle joystick":{
                "tactile":100,
                "souris":100
            },
            "toucher pour voir":100,
            "presser pour montrer":0,
            "position repos":100,
            "position prêt":100,
            "attirer l'attention":100,
            "enregistrer voix":100,
            "envoyer texte":100,
            "lire le son de nao":{
                "lire un mp3":100,
                "envoyer un mp3 multipart":0
            }
        },
        "Nao":{
            "déplacement":{
                "avancer":100,
                "tourner":100
            },
            "lever le bras":100,
            "pointer du doigt":0,
            "tourner la tête":100,
            "position repos":100,
            "position prêt":100,
            "dire texte":100,
            "retour vidéo":{
                "support des définitions":100,
                "selection automatique définition":80
            },
            "enregistrement son":0,
            "convertir wav en mp3":0
        }
        "Pi":{
            "video":100,
            "mouvement":0
        }
    }
}

function divFile(divId) {
    var res = document.createElement("div");
    res.id = divId;
    res.className = "subroot";
    return res;
}

function progressBar(name, prrr) {
    var line = document.createElement("div");
    line.className = "line";
    var desc = document.createElement("span");
    desc.innerText = name+" : ";
    desc.className = "task_name";
    line.appendChild(desc);
    var ext = document.createElement("div");
    ext.className = "progress_bar_ext";
    line.appendChild(ext);
    var ins = document.createElement("div");
    ins.className = "progress_bar_int";
    ins.style.width = prrr+"%";
    ext.appendChild(ins);
    return line;
}

function recursive(root, elem)
{
    var k = Object.keys(elem);
    var val = 0; // sum of values of internal objects
    for (var i=0; i<k.length; i++)
    {
        if (typeof(elem[k[i]]) == "number")
        {
            root.appendChild(progressBar(k[i], elem[k[i]]));
            val += elem[k[i]];
        }
        else if (typeof(elem[k[i]]) == "object")
        {
            var subRoot = divFile(k[i]);
            var subVal = recursive(subRoot, elem[k[i]]);
            val += subVal;
            root.appendChild(progressBar(k[i], subVal));
            root.appendChild(subRoot);
        }
    }
    return val/k.length;
    
}

function main() {
    var root = document.getElementById("progress")
    recursive(root, progress)
}

setTimeout(function () {main();}, 2000);

/*
    CSS classes :
      * line
      * task_name
      * subroot
      * progress_bar_ext
      * progress_bar_int

*/