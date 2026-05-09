<?php   

echo "Bem-vindo(a) ao screen match!\n";
$nomeFilme = "Top Gun - Maverick";
$anoLancamento = $argv[1] ?? 2022;
$somaDasNotas = 9 + 6 + 8 + 7.5 + 5;
$notaFilme = $somaDasNotas/5;
$planoPrime = true;
$incluidoNoPlano= $planoPrime || $anolancamento <2020;

echo "Nome do Filme: " . $nomeFilme . "\n";
echo "Nota do Filme: $notaFilme\n";
echo "Ano de lancamento: $anoLancamento\n";