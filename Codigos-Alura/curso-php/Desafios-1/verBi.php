<?php
$ano = $argv[1] ?? 2025;

$caso1 = ($ano % 4) == 0 && ($ano % 100) != 0;
$caso2= ($ano % 4) == 0 && ($ano % 100) == 0 && ($ano % 400) == 0;
if($caso1){
    echo "$ano e bissesto";
}else if($caso2){
    echo "$ano e bissesto";
}else{
    echo "$ano nao e bissesto";
}
