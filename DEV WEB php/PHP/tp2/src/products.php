<?php

function getProducts():array|Exception{
    $source = '../data/data.json';
    $content = file_get_contents($source);
    $products = json_decode($content,true);

    if (empty($products)){
        throw new Exception('No product.');
    }

    return $products;
}



function getProductsById(int $id):array|Exception{
    $products = getProducts();

    $id_to_find = $id;

    $products_f  = array_filter(
        $products,

        fn ($p) => $p['id'] === $id_to_find 
    );

    if (count($products_f) != 1){
        throw new Exception(sprintf('None or not only one product for id "%d"', $id_to_find),1); 
    }

    $product = array_shift($products_f); 

    return $product;

 



}

?>