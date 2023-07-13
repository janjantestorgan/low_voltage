import pytest
from fixtures import env
from ..tracker_dcs_low_voltage import mqtt as connect_to_mqtt


@pytest.fixture
def mqtt(env):
    return connect_to_mqtt.connect_to_mqtt()


def test_connect(mqtt):
    assert mqtt is not None
