@echo off
rem Select source file
	set "source_file=cipher.py"

rem Check if pytube is installed
	pip show pytube >nul 2>&1
	if %errorlevel% equ 0 (
   		echo Pytube is installed
	) else (
    		echo Pytube is not installed. Installing pytube 
  		pip install pytube
	)

REM Get and set location of pytube installation
	for /f "tokens=1,* delims=: " %%i in ('pip show -f pytube ^| findstr Location') do set "PYTUBE_LOCATION=%%j"
	echo Pytube installed at: %PYTUBE_LOCATION%
	set "destination_folder=%PYTUBE_LOCATION%\pytube"
	echo Destination folder: %destination_folder%

pause

rem Fix the pytube problem
	copy %source_file% %destination_folder%
	echo Fixed

pause


