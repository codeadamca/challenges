<?php

function gcd($p, $q) 
{ 

    // echo 'P: '.$p.' Q: '.$q.'<br>';

    if ($p == 0)  return $q; 
    if ($q == 0) return $p; 
    if ($p == $q) return $p; 
   
    if ($p > $q) return gcd($p - $q, $q);   
    else return gcd($p, $q - $p); 

} 

$p = 98;
$q = 56;
$gcd = gcd($p, $q);

echo 'The largest common denominator between '.$p.' and '.$q.' is '.$gcd.'!';
