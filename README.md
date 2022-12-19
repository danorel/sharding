### Instructions

1. `docker-compose up -d`: starts MongoDB database separate shards and the web application using them.
2. `docker-compose stop`: stops Docker containers to work.

### Application

Application web service starts using `localhost:8080` URL:

1. Goto `/` to check whether application is running or not.
2. Goto `/sharding/enable` to enable sharding capabilities for admin database. 
3. Goto `/sharding/info` to receive info about shards size. 
4. Goto `/sharding/load` to load Titanic database into MongoDB collection.