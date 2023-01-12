PID=$1
N=$2
outputName=$3

statusParams='VmPeak:\|VmSize:\|VmHWM:\|VmRSS:\|VmPTE:\|VmSwap:\|Threads:' 
meminfoParams='MemFree:\|Buffers:\|Cached:\|SwapCached:\|Active:\|Inactive:\|Dirty:\|Writeback:\|AnonPages:\|Mapped:\|Slab:\|PageTables:\|Committed_AS:\|KernelStack:\|Shmem:\|MemAvailable:\|Unevictable:\|SwapFree:'

for ((i=1;i<=$N;i++))
do
   echo "Iteration $i " $(date '+%Y-%m-%dT%T') >> $outputName
   echo "Iteration $i of $N"
	
   cat /proc/$PID/status | grep -w $statusParams>> $outputName
   cat /proc/meminfo | grep -w $meminfoParams >> $outputName

   echo '-' >> $outputName
   sleep 1
done

python3 txt_to_csv.py $outputName $outputName".csv"

rm -f $outputName

