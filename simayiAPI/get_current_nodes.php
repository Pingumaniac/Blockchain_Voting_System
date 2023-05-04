<?php
//declare(strict_types=1);
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

function get_all_data() {
  $result = yaml_parse_file("backend_configuration.yaml");
  $all_data = array();
  foreach ($result as $key => $value) {
    $link = "http://ransom.isis.vanderbilt.edu:".strval($value["port"]);
    $all_data[] = $link;
  }
	//$all_data = ['http://ransom.isis.vanderbilt.edu:5000'];
  return $all_data;
}

header("Content-Type: application/json");
echo json_encode(get_all_data());
?>
