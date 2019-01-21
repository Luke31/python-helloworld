from src.helloworld.app import app


class TestApp(object):
    def test_app_movies(self):
        app.testing = True
        with app.test_client() as c:
            resp = c.get('/movies')
            assert resp.status == "200 OK"
            assert resp.data

    def test_app_wordcount(self):
        app.testing = True
        with app.test_client() as c:
            resp = c.get('/wordcount/hello%20world')
            assert resp.status == "200 OK"
            assert resp.get_json()['wordcount'] == 2

    def test_app_noroute(self):
        app.testing = True
        with app.test_client() as c:
            resp = c.get('/notvalidroute')
            assert resp.status == "404 NOT FOUND"
            assert resp.data

