# fastapi-task

Project is under developement for testing.

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
