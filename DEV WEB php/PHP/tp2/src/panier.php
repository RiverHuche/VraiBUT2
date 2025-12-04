<?php
session_start();

require_once 'products.php';

$products = getProducts();

if (!empty($_REQUEST['cart'])){
    $_SESSION['cart'][$_REQUEST['cart']['id']] = $_REQUEST['cart'];
}

var_dump($_SESSION);

?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panier</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php
        echo <<<PANIER
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>QTE</th>
                        <th>Price</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>

        PANIER;
        $total = 0;
        foreach ($_SESSION['cart'] as $key => $value){
            $k = array_search($value['id'],array_column($products,'id'));
            $product = $products[$k];
            $totalline = $product['price']*$value['qte'];
            echo <<<LIGNE
                <tr>
                    <td>{$product['title']}</td>
                    <td>{$value['qte']}</td>
                    <td>{$product['price']}</td>
                    <td>{$totalline}</td>
                </tr>
            LIGNE;

            $total +=$totalline;
            echo <<<LIGNETOT
                <tr colspan="3">
                    <td> Panier : {$total} </td>
                </tr>
            LIGNETOT;
        }


        echo <<<FOOTER
            </tbody>
            </table>
        FOOTER;
    ?>
    
</body>
</html>

