@echo off
C:\Users\dwive\AppData\Local\Programs\Python\Python36\python.exe main.py %*
title Converting Psuedo Code to Source Code
color 0a
set load=
set/a loadnum=0

:Loading
set load=%load%ÛÛ
cls

echo 	----------------------------------------------------------------------------------------------------------
echo 					PSUEDO CODE TO SOURCE CODE TRANSLATION
echo 	----------------------------------------------------------------------------------------------------------
echo.
echo.
echo 	Translating... Please Wait...
echo 	----------------------------------------
echo 	%load%
echo 	----------------------------------------
ping localhost -n 1 >nul

set/a loadnum=%loadnum% +1
if %loadnum%==20 goto Done

goto Loading
:Done
cls
echo 	----------------------------------------------------------------------------------------------------------
echo 					PSUEDO CODE TO SOURCE CODE TRANSLATION
echo 	----------------------------------------------------------------------------------------------------------
echo.
echo.

echo 	Completed... 
echo 	----------------------------------------
echo 	%load%
echo 	----------------------------------------
echo.
echo.
echo 	Succesfully Generated Source Code File.
start notepad "XMLFile.xml"
start notepad "sourceCode.c"
pause
exit