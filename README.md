# FLASH SHOP

Simple shop site on flask framework

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requierement packages.

```bash
pip install -r requirements.txt
```

## Usage
1. Create test database using a special script
    ```python
        python products_creator.py
    ```
2. Change **SERVER_NAME** in conf.py the one you want to use to start the server
    ```python
    class Config():
        DEBUG = False
        # DATABASE_URI='products.sqlite'
    
    
    class DevelopentConfig(Config):
        DEBUG = True
        SERVER_NAME = "127.0.0.1:8082" # <-- Change server name and port
    ```
3. Start server
    ```bash
    python app.py
    ```
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
