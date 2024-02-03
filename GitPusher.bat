@echo off
title GitPusher by muyeed15

color 1F

echo =============================
echo     GitPusher by muyeed15
echo =============================
echo.

rem Check GitHub connectivity using curl
set githubHost=github.com
set connectivityStatus=False

curl -s -o nul https://%githubHost%
if %errorlevel% equ 0 (
    set connectivityStatus=True
)

echo Connectivity Status: %connectivityStatus%
echo.

if "%connectivityStatus%"=="False" (
    color 4F
    echo GitHub server is not available. Exiting in 5 seconds...
    timeout /nobreak /t 5 >nul
    exit /b
)

rem Do not change this code.
git add .
echo.

set /p commitMessage="Enter commit message: "
git commit -m "%commitMessage%"

color F1

echo.
echo Pulling with automatic conflict resolution --
git pull -X theirs

rem Check if there were conflicts
git diff --quiet --exit-code || (
    color 4F
    echo Conflict resolution failed. Please resolve conflicts manually and run 'git push'.
    echo Press any key to exit...
    pause >nul
    exit /b
)

echo.
echo Pushing --
git push

color 1F

echo.
echo Press any key to exit...
pause >nul
