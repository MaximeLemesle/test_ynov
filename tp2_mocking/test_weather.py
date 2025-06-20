import unittest
from unittest.mock import patch, Mock, mock_open
from weather_service import get_temperature, save_weather_report
import requests  # type: ignore


class TestWeather(unittest.TestCase):
    def setUp(self):
        """Fixture : prépare les données avant chaque test"""
        self.sample_weather_data = {"main": {"temp": 25.5}}
        self.test_city = "Paris"

    def test_get_temperature_paris(self):
        """Test basique qui va poser problème (dépend de l'API réelle)"""
        # temp = get_temperature("Paris")
        # self.assertIsNotNone(temp)  # Test très faible
        pass

    @patch("weather_service.requests.get")
    def test_get_temperature_success(self, mock_get):
        """Premier test avec mock - succès"""
        fake_response = Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = self.sample_weather_data
        mock_get.return_value = fake_response
        result = get_temperature(self.test_city)
        self.assertEqual(result, 25.5)
        mock_get.assert_called_once_with(
            "http://api.openweathermap.org/data/2.5/weather",
            params={"q": self.test_city, "appid": "fake_api_key", "units": "metric"},
        )

    @patch("weather_service.requests.get")
    def test_get_temperature_city_not_found(self, mock_get):
        """Test quand la ville n'existe pas (404)"""
        fake_response = Mock()
        fake_response.status_code = 404
        mock_get.return_value = fake_response
        result = get_temperature("VilleInexistante")
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch("weather_service.requests.get")
    def test_get_temperature_network_error(self, mock_get):
        """Test quand il y a une erreur réseau"""
        mock_get.side_effect = requests.exceptions.RequestException()
        result = get_temperature("Paris")
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch("weather_service.requests.get")
    def test_multiple_cities(self, mock_get):
        """Test plusieurs villes avec une seule méthode (paramétré)"""
        cities_and_temps = [("Paris", 25.0), ("Londres", 18.5), ("Tokyo", 30.2)]
        for city, expected_temp in cities_and_temps:
            fake_response = Mock()
            fake_response.status_code = 200
            fake_response.json.return_value = {"main": {"temp": expected_temp}}
            mock_get.return_value = fake_response
            with self.subTest(city=city):
                result = get_temperature(city)
                self.assertEqual(result, expected_temp)


class TestWeatherReport(unittest.TestCase):
    def setUp(self):
        self.city = "Paris"
        self.temp = 20.5
        self.timestamp = "2024-01-01T12:00:00"

    @patch("weather_service.datetime")
    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("weather_service.get_temperature")
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        """Test sauvegarde rapport météo - succès"""
        mock_get_temp.return_value = self.temp
        mock_datetime.now.return_value.isoformat.return_value = self.timestamp
        result = save_weather_report(self.city)
        self.assertTrue(result)
        mock_get_temp.assert_called_once_with(self.city)
        mock_file.assert_any_call("weather_log.json", "r")
        mock_file.assert_any_call("weather_log.json", "w")


if __name__ == "__main__":
    unittest.main()
