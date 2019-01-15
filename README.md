# python-helloworld

Hello-World Docker Flask-REST Service based on openSUSE

## How to start

Use following command to clone git repo, build image and run container: 
```bash
git clone git@github.com:Luke31/python-helloworld.git &&
cd python-helloworld &&
docker build -t python-hello-world . &&
docker run -it -p 5000:5000 python-hello-world
```

Now you can call the Flask REST-Service in Browser: [localhost:5000](localhost:5000) or test in console: 
```bash
curl localhost:5000
```

