# Categorizer web server

## Usage

1. Copy models you intend to use to './models'
1. sudo `pip install -r requirements.txt`
1. `python server.py 8080`

That starts loads the models and starts the server. To test the service run:

```
curl -X POST localhost:8080/categorize -d '{"body": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."}'
```
