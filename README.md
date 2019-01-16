# python-helloworld

Hello-World Docker Flask-REST Service based on openSUSE

## How to start

Use following command to clone the git repo, build an image and run the container: 
```bash
git clone git@github.com:Luke31/python-helloworld.git &&
cd python-helloworld &&
docker build -t python-hello-world . &&
docker run -it -p 5000:5000 python-hello-world
```

Now you can call the Flask REST-Service in your browser: [localhost:5000](http://localhost:5000) or test in your shell by running: 
```bash
curl localhost:5000
```

This image follow pytest good practices: [https://docs.pytest.org/en/latest/goodpractices.html](https://docs.pytest.org/en/latest/goodpractices.html)
and Flask-RESTful practices: [https://flask-restful.readthedocs.io/en/0.3.5/intermediate-usage.html](https://flask-restful.readthedocs.io/en/0.3.5/intermediate-usage.html)
