<?php
/*
EXERCISE:
Using your language, explore the concept of regular expressions,
creating one that is capable of finding and extracting all numbers
from a text.
*/

function get_all_numbers($str)
{
    $pattern = '/\d/';
    $matches = [];
    preg_match_all($pattern, $str, $matches);
    return implode('', $matches[0]);
}

echo get_all_numbers("Holaque2tal") . "\n"; // Output: 2


/*
EXTRA DIFFICULTY (optional):
Create 3 regular expressions (at your discretion) capable of:
Validating an email.
Validating a phone number.
Validating a URL.
*/

function validate_email($email)
{
    $pattern = '/^[\w\.-]+@[\w\.-]+\.\w{2,}$/';
    // [\w\.-]+ matches the part before and after @
    // \w{2,} matches the top-level domain (min 2 letters)
    return preg_match($pattern, $email) > 0;
}

var_dump(validate_email("cuchara"));
var_dump(validate_email("cuch@ra.da"));

function validate_phone($number)
{
    $pattern = '/^(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$/';
    // (\+?\d{1,3}[\s-]?)? - Matches an optional country code.
    // $$? - Matches an optional opening parenthesis.
    // [\s-]? - Matches an optional space or hyphen.
    // \d{3} - Matches exactly 3 digits (prefix).
    // [\s-]? - Matches an optional space or hyphen.
    // \d{4} - Matches exactly 4 digits (line number).
    return preg_match($pattern, $number) > 0;
}

var_dump(validate_phone("12"));
var_dump(validate_phone("+41 4588748965"));

function validate_url($url)
{
    $pattern = '/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*/';
    // ([\da-z\.-]+) matches the subdomain or domain name. It allows any combination of digits (\d), lowercase letters (a-z), periods (.), and hyphens (-).
    // ([a-z\.]{2,6}) matches the top-level domain (TLD) with a length between 2 and 6 characters, allowing letters and periods.
    // ([\/\w \.-]*)* matches the path, query string, and fragment identifier optionally. It allows any combination of forward slashes (/), word characters (\w), spaces, periods, and hyphens.
    return preg_match($pattern, $url) > 0;
}

var_dump(validate_url("http://.com"));
var_dump(validate_url("https://www.gabrielcmoris.com"));
