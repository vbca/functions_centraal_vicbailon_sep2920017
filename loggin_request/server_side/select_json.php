<?php
header("Access-Control-Allow-Origin: *");
include_once 'codes.php';

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
        HTTPStatus(406);
        echo json_encode(array(
            'status' => 406,
            'message' => 'Check your request, no empty fields',
        ));
    } else {
        $m1 = new MongoClient("mongodb://ds017432.mlab.com:17432");
        $db = $m1->centraal;
        $db->authenticate("centraal_user", "aca123demy");
        $collection = new MongoCollection($db, 'user');

        $user = array(email => $_POST['username'], password => $_POST['password']);
        $get = array(name => 1);
        
        $owner = array(owner => $_POST['username']);
        
        $cursor = $collection->find($user);
        
         //INSERTAMOS UN NUEVO REGISTRO a otra coleccion
        $collection_contact = new MongoCollection($db, 'contact');
        $cursor2 = $collection_contact->find($owner);
        $results= array();  
        $con=0;
        
        $eso=$cursor->count();
        if ($eso == 1) {
            while ($cursor->hasNext()) {

                 while ($cursor2->hasNext()) {
                 $info2 = $cursor2->getNext();
                        $results[$con]->id=$info2['_id'].id;
                        $results[$con]->name=$info2['name'];
                        $results[$con]->number=$info2['number'];
                        $con++;
                 }
                
                $final=json_encode($results);
                
                HTTPStatus(200);
                echo json_encode(array(
                    'status' => 200,
                    'message' => 'List',
                    'content' => $final
                ));
                break;
            }
        } else {
            HTTPStatus(203);
            echo json_encode(array(
                'status' => 203,
                'message' => 'Deny access, please check user and password',
            ));
        }
    }
}
?>

