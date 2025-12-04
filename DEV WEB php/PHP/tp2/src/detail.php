<?php

require_once 'products.php' ;

$product = null;

if (!empty ($_GET['id'])){
    try {
        $product = getProductsById((int)$_GET['id']);
    } catch (\Exception $e) {
        
    }
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css"> 
</head>
<body>
    <h1>Detail du produit</h1>
    <?php if ($product): ?>
        <?php
        echo '<h2>' . htmlspecialchars($product['title']).'</h2';
        echo '<p>Marque: '.htmlspecialchars($product['brand']). '</p>';
        echo '<p>Description: '.htmlspecialchars($product['description']). '</p>';
        echo '<p>Prix: '.number_format($product['price'],2,'.').'euros'.'</p>';

        echo '<ul>';
        foreach ($product['images'] as $src){
            echo '<li><img src ="'.htmlspecialchars($src).'" alt="image"></li>';
        }
        echo '</ul>';

        echo '<h2>Toutes les informations:</h2>';
        echo '<ul>';
        $informations=[];
        foreach ($product as $key =>$value){
            if (is_array($value)){
                continue;
            }
            echo '<li><strong>'. htmlspecialchars($key). '</strong>:' .htmlspecialchars($value). '</li>';
        }
        echo '</ul>';

        echo <<<FORM
            <form action="/panier.php" method="post">
            <label for"qte">QTE: </label> <input type="number" name="cart[qte]" id="qte" value="1" />
            <input type="hidden" name="cart[id]" value="{$product['id']}" />
            <input type="submit" value="Ajouter"/>
            </form>
        FORM;

        ?>
    <?php else: ?>
        <p>Produit non trouvé ou ID manquant.</p>
    <?php endif; ?>

    <p><a href="index.php"> retour</a></p>
</body>
</html>