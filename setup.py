
import os
from setuptools import setup
from distutils.extension import Extension

def find_source(bases):
    ret = []
    for base in bases:
        for file in os.listdir(base):
            if os.path.splitext(file)[1] in (".cpp", ".c"):
                ret.append(os.path.join(base, file))
            
    print("find_source: " + str(ret))
    return ret

setup(
  name = "bfm_core",
  packages=['bfm_core'],
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("bfm_core provides core libraries and scripts to support BFMS"),
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "CocoTB", "Python"],
  url = "https://github.com/sv-bfms/bfm_core",
  entry_points={
    'console_scripts': [
      'vlsim = vlsim.__main__:main'
    ]
  },
  setup_requires=[
    'setuptools_scm',
  ],
  ext_modules=[
      Extension("pybfms.hdl_sim", 
        find_source(["ext/common", "ext/hdl_sim"]))]
)

