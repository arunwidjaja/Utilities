@echo off
setlocal EnableDelayedExpansion

:: Directory list and log file
set DIRS_FILE=%~dp0bd.txt
set LOG_FILE=%~dp0backup.LOG

:: Check if the directories file exists
if not exist "%DIRS_FILE%" (
    echo ERROR: The directories file does not exist. Please make sure it is located at: %DIRS_FILE%. Each line should contain the source path and the target path separated by a comma, like so:
	echo.
	echo # This is a sample directory file
	echo SOURCEPATH1,TARGETPATH1
	echo SOURCEPATH2,TARGETPATH2
	echo # Lines preceded by "#" are ignored
	echo.
    pause
    exit /b 1
)
:: Clear previous log file
if exist "%LOG_FILE%" (
	del "%LOG_FILE%"
)
echo -----------
echo START HERE:
echo -----------
echo Make sure you have a .txt file in the same directory as this file called 'bd.txt'.
echo Each line should contain your source directory and your target directory separated by a comma.
echo Here's an example of a 'bd.txt' file that would back up my Videos and Documents to another drive:
echo ----------------------------------------------------------------------------------
echo.
echo C:\Users\Arun Widjaja\Documents,D:\Backups\Documents
echo C:\Users\Arun Widjaja\Videos,D:\Backups\Videos
echo.
echo -----------------------------------------------------------------------------------
echo That would backup my Documents and Videos from my C: to D: Drive.
echo ====================
echo STARTING ROBOCOPY...
echo ====================
(
	echo This backup was performed on: %date%
	echo.
) >> "!LOG_FILE!"

for /f "usebackq tokens=1,2 delims=, eol=#" %%A in ("%DIRS_FILE%") do (
    :: Skip lines that are empty
    if "%%A"=="" (
        echo Skipping empty line.
    ) else (
        set "SRC=%%A"
        set "DST=%%B"
        
        :: Check if directories exist
        if not exist "!SRC!" (
            echo ERROR: Source directory "!SRC!" does not exist.
			exit /b 1
        )
		if not exist "!DST!" (
			mkdir "!DST!"
		)
		:: Perform robocopy and log output
		echo Backing Up: "!SRC!" ---^> "!DST!"
		echo "!SRC!" ---^> "!DST!" >> "!LOG_FILE!"
		robocopy "!SRC!" "!DST!" /e /log+:"!LOG_FILE!" /NDL /NJS /NJH> nul
	)
)
echo.
echo Robocopy has completed.
echo Check the log file at:
echo.
echo %LOG_FILE%.
echo.
echo Do you want to open the log file? type "y" or "Y" and press enter to do so.
echo If not, hit any other key.
set /p userInput=
REM Check if user input is 'y' or 'Y'
if /i "%userInput%"=="y" (
    start notepad.exe !LOG_FILE!
) else (
		echo Exiting...
		pause
		exit
)
pause
endlocal
