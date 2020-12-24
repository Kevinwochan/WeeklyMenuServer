#sudo docker pull mongo
sudo docker run --rm --name mongo \
    -e MONGO_INITDB_ROOT_USERNAME=$MONGO_USER \
    -e MONGO_INITDB_ROOT_PASSWORD=$MONG_PWD \
    -e MONGO_INITDB_DATABASE=$MONGO_DB_NAME \
    mongo

#sudo docker run -it --rm mongo \
#    mongo \
#    -u $MONGO_USER \
#    -p $MONG_PWD \
#    --authenticationDatabase $MONGO_AUTH_DB_NAME \
#    HelloFresh