@echo off
setlocal
:: Example python url: https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe
:: Step 1: Define URLs and file names
set "DOWNLOAD_URL=https://www.python.org/ftp/python"
set "VERSION_NAME=python-versions.html"

echo Fetching the latest Python version...

:: Step 2: Use curl to download the latest Python version page and extract the latest version number
powershell -Command "Invoke-WebRequest -Uri '%DOWNLOAD_URL%' -OutFile '%VERSION_NAME%'"


:: Step 3: Extract the latest version number from the HTML file
for /F "tokens=1,2 delims=/" %%a in ('findstr /r /c:"[0-9]+\.[0-9]+\.[0-9]+/" python-versions.html') do (
    set "LATEST_VERSION=%%b"
    goto :found
)

:found
echo Latest Python version found: %LATEST_VERSION%

:: Step 4: Download the latest Python installer (64-bit version for Windows)
set "DOWNLOAD_LINK=%DOWNLOAD_URL%/%LATEST_VERSION%/python-%LATEST_VERSION%-amd64.exe"
echo Downloading Python %LATEST_VERSION% from %DOWNLOAD_LINK% ...
curl -o %INSTALLER_NAME% %DOWNLOAD_LINK%

:: Step 5: Install Python silently and add it to PATH
echo Installing Python...
%INSTALLER_NAME% /quiet InstallAllUsers=1 PrependPath=1

:: Step 6: Cleanup installer files
echo Cleaning up...
::del %INSTALLER_NAME%
::del latest_python_page.html

echo Python %LATEST_VERSION% has been installed.
pause