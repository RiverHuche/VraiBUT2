<?php

require_once 'products.php';
$data = getProducts(); 
$brand = $_GET['brand'] ?? null;
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des Produits</title>
    <link rel="stylesheet" href="style.css"> 
</head>
<body>
    <?php  
        include "../templates/filter.php";
    ?>
    <h1> Mes Produits</h1>
    <main>
        <form action="index.php" method="GET" class="search-form">
        <input type="text" name="search" placeholder="Rechercher un produit (nom, marque...)" value="<?= htmlspecialchars($_GET['search'] ?? '') ?>">
        <button type="submit">Rechercher</button>
        <?php if(!empty($_GET['search'])): ?>
            <a href="index.php" class="reset-btn">Effacer</a>
        <?php endif; ?>
        </form>
        <?php
        if (!empty($data)): 
            foreach ($data as $product): 
                if ($brand && strtolower($product['brand']) !== strtolower($brand)) continue;
                echo '<div class="product">';
                    echo '<h3>' . htmlspecialchars($product['title']) . '</h3>';
                    echo '<p>Marque: ' . htmlspecialchars($product['brand']) . '</p>';
                    echo '<p>Description: ' . htmlspecialchars($product['description']) . '</p>';
                    echo '<p>Prix: ' . htmlspecialchars(number_format($product['price'], 2, ',', ' ') . ' €') . '</p>';
                    echo '<p><a href="detail.php?id=' . htmlspecialchars($product['id']) . '">Voir le détail</a></p>';
                echo '</div>';
            endforeach; 
        else: 
            echo '<p>Aucun produit trouvé.</p>';
        endif; ?>
    </main>

</body>
</html>