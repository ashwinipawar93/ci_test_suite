import pytest
import os

from ..psu_ea import PsuEA, ExceptionPSU


def get_devices():
    ports = [None]
    for p in os.listdir("/dev"):
        if p.startswith("ea"):
            ports.append(p)
            ports.append(os.path.join("/dev", p))
    for p in os.listdir("/dev/serial/by-id"):
        if p.startswith("usb-EA"):
            ports.append(p)
            ports.append(os.path.join("/dev/serial/by-id", p))
    return ports


@pytest.fixture(scope="function")
def psu():
    psu = PsuEA()
    yield psu
    psu.close()


class TestPSU:

    @pytest.mark.parametrize("port", get_devices())
    def test_real_port_names(self, port):
        psu = PsuEA(comport=port)
        psu.close()

    @pytest.mark.parametrize("port", ["foobar", "/dev/foobar"])
    def test_fake_port_names(self, port):
        with pytest.raises(ExceptionPSU):
            psu = PsuEA(comport=port)
            psu.close()

    def test_output(self, psu):
        psu.output_on()
        psu.output_off()

        if psu.get_device_description()['controllable_outputs'] > 1:
            psu.output_on(1)
            psu.output_off(1)

    def test_voltage(self, psu):
        psu.set_voltage(24)

        if psu.get_device_description()['controllable_outputs'] > 1:
            psu.set_voltage(24, 1)
