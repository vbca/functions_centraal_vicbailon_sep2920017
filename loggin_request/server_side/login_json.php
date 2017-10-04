<?php
header("Access-Control-Allow-Origin: *");
include_once 'codes.php';
//return HTTPStatus(400);
$data = json_decode(file_get_contents('php://input'), true);
$_POST=$data;

if (!isset($_POST['username']) || !isset($_POST['password'])) {
     HTTPStatus(400);
    echo json_encode(array(
         'status' => 400,
         'message' => 'Check your request, user and password',
    ));
} else {
    if ($_POST['username'] == '' || $_POST['password'] == '') {
        HTTPStatus(500);
        echo json_encode(array(
            'status' => 500,
            'message' => 'Check your request, no empty fields',
        ));
    } else {
        $m1 = new MongoClient("mongodb://ds017432.mlab.com:17432");
        $db = $m1->centraal;
        $db->authenticate("centraal_user", "aca123demy");
        $collection = new MongoCollection($db, 'user');

        $user = array(email => $_POST['username'], password => $_POST['password']);
        $get = array(name => 1);

        $cursor = $collection->find($user); 
        $eso=$cursor->count();
        if ($eso == 1) {
            while ($cursor->hasNext()) {
                $info = $cursor->getNext();
                //print_r($info['name']);

                HTTPStatus(200);
                echo json_encode(array(
                    'status' => 200,
                    'message' => 'Login success',
                    'name' => $info['name']
                ));
                break;
            }
        } else {
            HTTPStatus(406);
            echo json_encode(array(
                'status' => 406,
                'message' => 'Deny access, please check user and password',
            ));
        }
    }
}
?>

