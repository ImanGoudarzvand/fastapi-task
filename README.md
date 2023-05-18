# fastapi-task


1- clone the project
```
git clone https://github.com/ImanGoudarzvand/fastapi-task.git
cd fastapi-task

```

2- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements.txt
```

4- create your env
```
cp .env.example .env
```

5- run the services with docker
```
docker compose up -d
```


6 - run the app
```
uvicorn app.main:app --reload --port 8000
```

7 - run the tests
```
pytest
```

### Possible Improvements:
1- add more tests ( full coverage)
2- using Factory functions and more fixtures in Testing
3- docker build the api app and put it next to other services in docker compose
4- put testing in a seperate service in compose file
5- add password validation for users when registering
...
