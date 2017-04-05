"""Installation script for netnotify."""
# pylint: disable=wrong-import-position
import sys
from setuptools import setup, find_packages, Command

with open('README.rst', 'r') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='netnotify',
    description='send notifications over the Internet',
    long_description=LONG_DESCRIPTION,
    author='nihlaeth',
    author_email='info@nihlaeth.nl',
    url='https://github.com/nihlaeth/netnotify',
    license='GPLv3',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',
    scripts=['netnotify.py'],
    install_requires=[
        'dbus-python', 'notify2', 'user_config>=1.0a9', 'daemonocle'],
    entry_points={
        'console_scripts': [
            'netnotify = netnotify:send',
            'netnotifyd = netnotify:daemon_controller']},
    )
