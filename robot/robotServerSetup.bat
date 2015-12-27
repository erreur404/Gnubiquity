@echo off
echo this scrit will attempt to install python 2.7 and the python module Flask on your computer
echo and the python tool for installing packages "pip"
pause
echo installing python...
if not exist "C:\python27"
(
	python27_install.msi
	echo python2.7 installed
)
else
(
	echo python2.7 already installed
)


cp get-pip.py C:\python27
cd C:\python27
echo installing Python install utility
if not exist C:\python27\scripts\pip.exe
(
	python get-pip.py
	echo pip installed
)
else
(
	echo pip already installed
)

echo installing flask
cd scripts
pip install flask

echo installation complete