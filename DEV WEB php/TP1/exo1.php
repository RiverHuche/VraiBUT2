

Hugo de olivette
<?php

$nb = 1;
var_dump($nb);

echo "Voici la valeur de ma variable :".$nb.PHP_EOL;

var_dump($argv);
?>

Fin du php.


<?php
$x = 10;
$y = 5;



echo $y == $y ? 'true' : 'false' ; echo PHP_EOL;
$is_equal = $x == $y;
$is_not_equal = $x != $y;
$is_greater = $x > $y;
$is_less = $x < $y;
$is_greater_or_equal = $x >= $y;
$is_less_or_equal = $x <= $y;

if ($a != $b) {
    echo "Le test est VRAI\n";
} else {
    echo "Le test est FAUX\n";
}
?>




<?php
    $myVAr = 'Prepare variables.'; // simple

    // From Superglobals vars
    $whatTimeIsIt = $_SERVER['TIME_EXEC'] ;
    $request = $_GET['who'] ?? null;
?>

<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Titre de la page</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
    <ul>
        <li>variable myVAr est <?php echo $myVAr ?></li>
        <li>variable whateTimeIsIt est <?php echo $whatTimeIsIt ?></li>
        <li>variable request est <?php echo $request ?></li>
    </ul>
</body>
</html>
