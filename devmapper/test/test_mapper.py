
import os
import unittest

from devmapper.mapper import DevMapper, DevMapperError


class DevMapperTest(unittest.TestCase):

    def setUp(self):
        devname = 'ttyS0'
        devpath = ''
        for root, dirs, files in os.walk('/sys/devices'):
            for dn in dirs:
                if dn == devname:
                    devpath = '/'.join(os.path.join(root, dn).split('/')[:-1])
                    break
        self.devname = '/dev/'+devname
        self.devpath = devpath

    def test_search_ttyS0_case_1(self):
        # Use: /sys/devices/pnp0/00:08/tty
        devname = DevMapper.serial(self.devpath)
        self.assertEqual(self.devname, devname)

    def test_search_ttyS0_case_2(self):
        # Use: /sys/devices/pnp0/00:08/tty/
        devname = DevMapper.serial(self.devpath+'/')
        self.assertEqual(self.devname, devname)

    def test_search_dev_file(self):
        # Use: /dev/ttyS0
        devname = DevMapper.serial(self.devname)
        self.assertEqual(self.devname, devname)

    def test_search_invalid_path(self):
        try:
            devname = DevMapper.serial('/sys/devices/my/device/path')
        except DevMapperError:
            pass
