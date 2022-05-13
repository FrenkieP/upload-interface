<?php 

use Google\Cloud\Storage\StorageClient;

function upload_object($bucketName, $objectName, $source)
{
    // $bucketName = 'my-bucket';
    // $objectName = 'my-object';
    // $source = '/path/to/your/file';

    $storage = new StorageClient();
    $file = fopen($source, 'r');
    $bucket = $storage->bucket($bucketName);
    $object = $bucket->upload($file, [
        'name' => $objectName
    ]);
    printf('Uploaded %s to gs://%s/%s' . PHP_EOL, basename($source), $bucketName, $objectName);
}
upload_object('keygen1_bucket','file10',$_POST['file'])
?>