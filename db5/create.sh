curl -XPUT 'http://localhost:9200/_snapshot/netology_backup' -H 'Content-Type: application/json' -d '{
    "type": "fs",
    "settings": {
        "location": "snapshot repository",
        "compress": true
    }
}'