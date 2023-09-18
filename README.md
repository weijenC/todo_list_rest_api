# cognixus_assessment
This repo is soley for completing the home assessment provided by Cognixus Technologies Sdn Bhd as part of the interview process.


# Pending item to work on
1. Solve network issue where local host machine can't access docker container bridge network.
    > Solve this to access web documentation at http://127.0.0.1:3000/docs and API schema in JSON format at http://127.0.0.1:3000/openapi.json
2. Publish docker images to dockerhub.
3. Sign in to the API using gmail or github.
4. Database indexing on frequently accessed fields.


# To bring up container
## Build image if image not available in dockerhub
- ```docker build -t cognixus-mysql -f Dockerfile-mysql .```
- ```docker build -t cognixus-app -f Dockerfile-app .```

## Docker Compose to start all containers and sevices
- ```docker-compose up```

## Check if containers are running, there should have 2 containers named cognixus-app-container and cognixus-mysql-container
- ```docker ps```

## Get into cognixus-app-container container and execute curl command to call web service
- ```docker exec -it cognixus-app-container /bin/bash```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/add-item --data '{"request_id": "commit1", "user": "weijen", "item": "service car"}'```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/list-all-item --data '{"request_id": "commit1", "user": "weijen"}'```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/mark-item --data '{"request_id": "commit1", "user": "weijen", "item": "service car"}'```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/delete-item --data '{"request_id": "commit1", "user": "weijen", "item": "service car"}'```

## Run unit test
- ```docker exec -it cognixus-app-container /bin/bash```
- ```cd unittest/```
- ```python3 -m pytest -s test_returncode_additem.py -vv```
- ```python3 -m pytest -s test_returncode_listitem.py -vv```
- ```python3 -m pytest -s test_returncode_markitem.py -vv```
- ```python3 -m pytest -s test_returncode_deleteitem.py -vv```


# Others
## To access database
- ```mysql -h 182.1.0.10 -u root -p'rootpassword123#' -D cognixus```

## To access Interactive Web Documentation
- http://127.0.0.1:3000/docs#/

## To extract API JSON Schema
- http://127.0.0.1:3000/openapi.json






# Development Note
## CREATE Docker Network
- ```docker network create --driver=bridge --subnet=182.1.0.1/16 cognixus_network```

## CREATE Docker DB Volume
- ```docker volume create cognixus_db_data```

## CREATE Docker MySQL Container
- ```docker run -itd -v cognixus_db_data:/data -e MYSQL_ROOT_PASSWORD=rootpassword123# --name=cognixus-db --net=cognixus_network -p 3306:3306 mysql```

## ACCESS Docker MySQL Container
- ```docker exec -it cognixus-db /bin/bash```
- ```mysql -h localhost -u root -p'rootpassword123#'```

## CREATE table
- ```create database cognixus;```
- ```use cognixus;```
- 
```
create table todolist (
    id int NOT NULL AUTO_INCREMENT,
    item varchar(255) NOT NULL,
    status tinyint(1) DEFAULT 0 NOT NULL,
    owner varchar(255) NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (id)
);
```

## CREATE Docker App Volume
- ```docker volume create cognixus_app_data```

## CREATE Docker App Container
- ```docker run -itd --mount type=bind,source=/opt/program/cognixus-app,target=/opt/program/cognixus-app --name=cognixus-app --net=cognixus_network -p 3000:3000 ubuntu```

## ACCESS Docker App Container
- ```docker exec -it cognixus_app /bin/bash```
- ```apt-get update```
- ```apt-get install iputils-ping```
- ```apt-get install telnet```
- ```apt-get install curl```
- ```apt-get install mysql-client```
- ```apt-get install vim```
- ```apt-get install python3```
- ```apt-get install python3-pip```
- ```python3 -m pip install pip --upgrade```
- ```python3 -m pip install setuptools --upgrade```
- ```python3 -m pip install -r /opt/program/cognixus-app/requirements.txt```

## RUN Program (in app container)
- ```cd /opt/program/cognixus-app/```
- ```bash serve_gunicorn.sh start```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/add-item --data '{"request_id": "commit1", "user": "weijen", "item": "service car"}'```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/list-all-item --data '{"request_id": "commit1", "user": "weijen"}'```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/mark-item --data '{"request_id": "commit1", "user": "weijen", "item": "service car"}'```
- ```curl -X POST -H 'Content-Type: application/json' http://localhost:3000/delete-item --data '{"request_id": "commit1", "user": "weijen", "item": "service car"}'```

## RUN Unit Test
- ```cd /opt/program/cognixus-app/unittest/```
- ```python3 -m pytest -s test_returncode_additem.py -vv```
- ```python3 -m pytest -s test_returncode_listitem.py -vv```
- ```python3 -m pytest -s test_returncode_markitem.py -vv```
- ```python3 -m pytest -s test_returncode_deleteitem.py -vv```
