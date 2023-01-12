cd C:\Users\itama\Desktop\nbody

SET repetitions=5
SET bodies=50000

for /F %%i in (count.txt) DO set count=%%i

if %count% == 40 exit

for /L %%x in (1, 1, %repetitions%) do (
	nbodySim.exe %bodies% >> .\Osservazioni\output%count%.txt
)

SET /A count=count+1

echo %count% > count.txt 
