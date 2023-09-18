# cognixus_assessment

This repo is soley for completing the home assessment provided by Cognixus Technologies Sdn Bhd as part of the interview process.

# Steps
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



## Starting Container
1. Start docker desktop
2. ```docker ps -a```
3. ```docker start [CONTAINER_ID]```



```docker network create --driver=bridge --subnet=182.1.0.1/16 cognixus_network```

```docker build -t cognixus-mysql -f Dockerfile-mysql .```
```docker run -itd --name=cognixus-db2 --net=cognixus_network --ip 182.1.0.10 -p 3306:3306 cognixus-mysql```

```docker build -t cognixus-app -f Dockerfile-app .```
```docker run -itd --name=cognixus-app2 --net=cognixus_network --ip 182.1.0.11 -p 3000:3000 cognixus-app```


## Interactive Web Documentation
- http://127.0.0.1:3000/docs#/

## API JSON Schema
- http://127.0.0.1:3000/openapi.json





# Others
- ```mysql -h 182.1.0.2 -u root -p'rootpassword123#'```





# Restart Service Command (required after updating table or source file)
1. ```bash serve_gunicorn.sh stop```
2. ```bash serve_gunicorn.sh start```
3. ```ps aux | grep apws_main``` (to check if service started)
