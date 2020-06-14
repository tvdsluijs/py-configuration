from unittest import TestCase
from readconfig import ReadConfig


class TestReadConfig(TestCase):

    def test_ReadConfig_with_file(self):
        file = "config.yml"
        cf = ReadConfig(file)
        assert cf.file == file

    def test_ReadConfig_with_None(self):
        file = "./config/config.yml"
        cf = ReadConfig(None)
        assert cf.file == file

    def test_read_config_file(self):
        test_data = "Abbracadabra"
        file = "config.yml"
        cf = ReadConfig(file)
        assert cf.config['data']['test'] == test_data

