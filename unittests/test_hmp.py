import unittest
from importlib import reload
from unittest.mock import patch, MagicMock


# from tracker_dcs_low_voltage.low_voltage.hmp import visa
# with patch('tracker_dcs_low_voltage.low_voltage.hmp.sys.argv', ['hmp.py', 'input_device_name', 'input_mqtt_host']):


class TestHMP(unittest.TestCase):

    def test_HMP(self):
        with patch("tracker_dcs_low_voltage.low_voltage.hmp.visa") as mock_visa:
            from tracker_dcs_low_voltage.low_voltage import hmp

            HMP = hmp.HMP("input_device_name", 5, "/dummy/path", "TCPIP:dummy::SOCKET")

            # print("--------", mock_visa.ResourceManager.assert_called_once_with('/dummy/path'))
            self.assertEqual(
                mock_visa.ResourceManager.assert_called_once_with("/dummy/path"), None
            )

            self.assertEqual(HMP.name, "input_device_name")

            self.assertEqual(HMP.n_channels, 5)

            with self.assertRaises(ValueError):
                HMP.command(topic="dummy_topic", message=1111)

            with self.assertRaises(ValueError):
                HMP.command(topic="/device/cmd/wrong_device_name", message=1111)

            with self.assertRaises(AttributeError):
                # Error: AttributeError: 'int' object has no attribute 'decode'
                HMP.command(topic="/input_device_name/cmd/switch/1", message=1111)

    def test_get_HMP4040(self):
        with patch("tracker_dcs_low_voltage.low_voltage.hmp.visa") as mock_visa:
            from tracker_dcs_low_voltage.low_voltage.hmp import get_HMP4040

            HMP4040 = get_HMP4040("/dummy/path", "TCPIP:dummy::SOCKET")
            # Test visa is called with ResourceManager
            self.assertEqual(
                mock_visa.ResourceManager.assert_called_once_with("/dummy/path"), None
            )

            # Test visa open_resource is called
            self.assertEqual(
                mock_visa.ResourceManager(
                    "/dummy/path"
                ).open_resource.assert_called_once_with("TCPIP:dummy::SOCKET"),
                None,
            )

            # print("----", HMP4040.read_termination=='\n')
            self.assertEqual(HMP4040.read_termination, "\n")
            self.assertEqual(HMP4040.write_termination, "\n")


if __name__ == "__main__":
    unittest.main()
