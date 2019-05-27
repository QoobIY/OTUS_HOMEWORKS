# WRITING FIRST APP

#### 1. Create 3 files in root folder:
* views.py
* urls.py 
* main.py

**views.py** contains logic that is responsible for processing the user's request and for returning the response :
```python
from web_framework.response import response

def index(request):
    return response('index')
```

**urls.py** contains a list of comparable URL and pattern :
```python
import views

url_pattern = {
    '/': views.index,
}
```

**main.py** used to configure and start the server
```python
from urls import url_pattern
from web_framework.app import run_server

port = 8000
run_server(port, url_pattern)
```

#### 2. Create `template` file **index.html** in template folder

**template/index.html**
```html
<!doctype html>
<html>
<head>
    <title>File</title>
</head>
<body>
   <p>Hello World!</p>
</body>
</html>
```

#### 3. Run server

To start the server write in bash console
```bash
python main.py <PORT>
```
For Example, this is how server start with port 8082
```bash
python main.py
>>Serving on port 8000...
>>192.168.1.1 - - [20/May/2019 12:33:34] "GET / HTTP/1.1" 200 510
>>192.168.1.1 - - [20/May/2019 12:33:34] "GET /favicon.ico HTTP/1.1" 200 30
```

**In browser**

![alt-текст](/docs/files/browser.png)