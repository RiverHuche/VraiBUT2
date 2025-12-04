<?php

class myinput{

    public function construct(){

    }

    public function toString() :String{
        return "";
    }
}

interface InputRenderInterface{

    public function render();
}


abstract class GenerirFormElement implements InputRenderInterface{

    protected String $name;

    protected String $id;

    public function construct($name, $id){
        $this->name = $name;
        $this->id = $$id;
    }

    public function toString(): String{
        return $this->id+" "+$this->name;;
    }
}


abstract class Input extends GenericFormElement{

    public function __construct(){

    }

}


class Grandpa
{
    public function __construct()
    {
        
    }

}

$Textinput = new Input("1", "Text");


echo $Textinput;


?>