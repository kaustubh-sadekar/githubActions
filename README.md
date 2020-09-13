# githubActions

This repository contains a small collection of utility functions.

# Installing the library in colab
```shell
!git clone https://github.com/kaustubh-sadekar/dlutils.git
!sudo python3 dlutils/setup.py install
```

# Example code for testing in colab
```python
import sys
sys.path.append("dlutils/")
import kdlutils
input_dim = (1,600,800)
layersList = [{'conv':(1,7,3,1,1,1)},{'mp':(2,2,0,1)},{'conv':(7,14,3,1,1,1)},{'mp':(2,2,0,1)},{'conv':(14,30,3,1,1,1)},{'mp':(2,2,0,1)}]
out = kdlutils.kdlutils.getOutShape(input_dim,layersList)
print(out)
```
Documentation and new codes will be uploaded soon.

### References:

1. The setup.py file and theREADME.rst files are written based on [this blog](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56). It is a great reference for anyone trying to their package 'pip installable'

2. Link to python documentation section [related to packaging](https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi).

3. Link to python documentation section [related to pipy friendly README](https://packaging.python.org/guides/making-a-pypi-friendly-readme/).

4. Link to python documentation section [related to packaging using GiHhubActions](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/#:~:text=Go%20to%20https%3A%2F%2Fpypi,distinguishable%20in%20the%20token%20list.).

5. [Similar link](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/).

6. [link to the PiPy package](https://pypi.org/project/kdlutils/)

### To do
- [ ] Write a tutorial.md file explaining the process
- [x] Share useful links
- [x] Share link of Pipy package
