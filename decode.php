<?php

$url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub';

function get_table_from_string($string)
{

    $table_start = strpos($string, '<table');
    $table_end = strpos($string, '</table');

    $table = substr($string, $table_start, $table_end - $table_start + 8);

    return $table;

}

function get_contents($url)
{

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $result = curl_exec($ch);

    return $result;

}

function get_strings_between($string, $start, $end)
{

    $position = 0;
    $data = array();

    echo htmlentities($string);


    while(true)
    {

        $ini = strpos($string, $start, $position);
        if ($ini == 0) break;

        $ini += strlen($start);
        $len = strpos($string, $end, $ini) - $ini;
        $data[] =  substr($string, $ini, $len);

        $position = $ini + $len;
    }

    return $data;

}

function get_message_array($table)
{

    $array = get_strings_between($table, 'c0">', '<');

    return $array;

}

function decode_message($url)
{

    $contents = get_contents($url);
    $table = get_table_from_string($contents);
    $array = get_message_array($table);

    print_r($array);

    echo '<div style="position: relative; border: 1px solid red;">';

    for($i = 3; $i < count($array); $i += 3)
    {

        echo '<div style="
                position: absolute; 
                width: 20px; height: 20px; 
                border: 1px solid green;
                box-sizing: border-box;
                left: '.(20 * $array[$i]).'px;
                top: '.(20 * $array[$i + 2]).'px;">
                    '.$array[$i + 1].'
            </div>';
    }

    echo '</div>';

}




decode_message($url);

