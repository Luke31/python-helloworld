from src.helloworld import app

if __name__ == '__main__':
    app.srv.run(host='0.0.0.0', debug=True)
    print("started")
