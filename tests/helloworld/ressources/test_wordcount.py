from src.helloworld.ressources.wordcount import Wordcount


class TestLanguages(object):
    def test_get(self, mocker):
        mocker.patch.object(Wordcount, 'tokenize')
        languages = Wordcount()
        languages.tokenize.return_value = ['hello', 'world']
        assert languages.get('hello world') == {'wordcount': 2}
        languages.tokenize.assert_called_with = 'hello world'
