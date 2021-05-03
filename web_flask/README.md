## **web_flask**

### **Resources**
Read:

    What is a Web Framework?
    A Minimal Application<https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application>
    Routing (except “HTTP Methods”)<https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing>
    Rendering Templates<https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates>
    Synopsis<https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis>
    Variables<https://jinja.palletsprojects.com/en/2.9.x/templates/#variables>
    Comments<https://jinja.palletsprojects.com/en/2.9.x/templates/#comments>
    Whitespace Control<https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control>
    List of Control Structures (read up to “Call”)<https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures>
    Flask<https://palletsprojects.com/p/flask/>
    Jinja<https://jinja.palletsprojects.com/en/2.9.x/templates/>


Extra resources used:

    can't connect to Flask web service, connection refused<https://stackoverflow.com/questions/30554702/cant-connect-to-flask-web-service-connection-refused#30554831>
    The Pallets Project: Flask<https://palletsprojects.com/p/flask/>

### **Learning Outcomes**

    What is a Web Framework
    How to build a web framework with Flask
    How to define routes in Flask
    What is a route
    How to handle variables in a route
    What is a template
    How to create a HTML response in Flask by using a template
    How to create a dynamic template (loops, conditions…)
    How to display in HTML data from a MySQL database

### **Tasks**
### **0-hello_route.py, __init__.py**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition

```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
xyz@ubuntu:~$ 
```

### **1-hbnb_route.py**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
xyz@ubuntu:~$ 
```

### **2-c_route.py**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
    You must use the option strict_slashes=False in your route definition
```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
xyz@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
xyz@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
xyz@ubuntu:~$ 
```

### **3-python_route.py**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    You must use the option strict_slashes=False in your route definition

```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
xyz@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
xyz@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
xyz@ubuntu:~$ 
```

### **4-number_route.py**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition
```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
xyz@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
xyz@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
xyz@ubuntu:~$ 
```

### **5-number_template.py, templates/5-number.html**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
    You must use the option strict_slashes=False in your route definition
```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
xyz@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
xyz@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
xyz@ubuntu:~$ 
```

### **6-number_odd_or_even.py, templates/6-number_odd_or_even.html**
script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n is even|odd” inside the tag BODY
    You must use the option strict_slashes=False in your route definition
```
xyz@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

xyz@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
xyz@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
xyz@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
xyz@ubuntu:~$ 
```
