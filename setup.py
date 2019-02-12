from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for comp30830",
      url="",
      author="Alan Treanor",
      author_email="alan.treanor@ucdconnect.ie",
      license="GPL3",
      packages=['systeminfo'],
      entry_points={'console_scripts':['comp30830_systeminfo=systeminfo.main:main']
                    }
      )