@echo off

:: Step 1: Generate a list of installed packages
echo Fetching installed packages...
py -m pip freeze > requirements.txt

:: Step 2: Loop through and update each package
for /F "delims==" %%i in (requirements.txt) do (
    echo Updating package %%i...
    py -m pip install --no-cache-dir --upgrade %%i
)

:: Step 3: Clean up
del requirements.txt

echo All packages have been updated.
pause
