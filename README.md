# FLASH SHOP

Simple shop site on flask framework

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [flask](http://flask.pocoo.org).

```bash
pip install flask
```

## Usage

1. Change **SERVER_NAME** in conf.py the one you want to use to start the server
    ```python
    class Config():
        DEBUG = False
        # DATABASE_URI='products.sqlite'
    
    
    class DevelopentConfig(Config):
        DEBUG = True
        SERVER_NAME = "127.0.0.1:8082" # <-- Change server name and port
    ```
2. Start server
    ```bash
    python app.py
    ```
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
