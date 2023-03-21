@echo off
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

rem Check if Python is installed
	winget show --name Python | findstr /R /C:"Python.*[3-9]\.[1-9][0-9]*"> nul 2>&1
	if %errorlevel% equ 0 (
   		echo Python 3.10+ is installed
	) else (
    		echo Python 3.10+ is not installed. Installing Python 3.10
  		winget install --id=Python.Python.3.10 -e
	)

rem Check if pytube is installed
	pip show pytube >nul 2>&1
	if %errorlevel% equ 0 (
   		echo pytube is installed
	) else (
    		echo pytube is not installed. Installing pytube 
  		pip install pytube
	)

rem Check if ffmpeg-python is installed
	pip show ffmpeg-python > nul 2>&1
	if %errorlevel% equ 0 (
 		echo ffmpeg-python is installed
	) else (
    		echo ffmpeg-python is not installed. Installing pytube 
  		pip install ffmpeg-python
	)

rem Check if ffmpeg is installed
	winget show ffmpeg > nul 2>&1
	if %errorlevel% equ 0 (
		echo ffmpeg is installed
	) else (
    		echo ffmpeg is not installed. Installing ffmpeg 
  		winget install ffmpeg --accept-source-agreements --accept-package-agreements
	)

rem Execute the Python file
	python ./scripts/main.py

exit

