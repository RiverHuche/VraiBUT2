<?php

for ($i = 0; $i < 10; $i++){
    if($i % 2 == 0){
        echo "paire \n";
    }
    else{
        echo "impaire \n";
    }
}

$liste_langages = array("php"=> "servers", "html"=> "style", "css" => "style", "python" => "servers");

function est_serveur($type) {
    return ($type == "servers");
}

$langages_serveur = array_filter($liste_langages, "est_serveur");

var_dump($langages_serveur);


?>

