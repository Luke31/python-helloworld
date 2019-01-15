# python-helloworld

Clone git repo, build and run image: 
```bash
git clone git@github.com:Luke31/python-helloworld.git
cd python-helloworld
docker build -t python-hello-world . &&
docker run -it -p 5000:5000 --name python-helloworldc python-hello-world
```

Call Flask REST-Service in Browser: [localhost:5000](localhost:5000) or test in console: 
```bash
curl localhost:5000
```

