## Run the App(local)
#### install  Python environments
```
pip install virtualenv
```
#### Create env 
```
python3 -m venv 
```
#### Activate env 
```
source env/bin/activate
```
#### Use pip to install dependencies from requirements.txt:
```
pip install -r requirements.txt
```


Deployment
----------

deploy using AWS Lambda and zappa.

Install `zappa`:

```
  $ pip install zappa
```

Install `aws-cli` to run cloudformation template:

```
  $ pip install aws-cli
```
