#/bin/bash
services=(173.194.222.113 87.250.250.242 192.168.0.1)
while :
do
        for j in ${services[@]}
        do
                nc -zvw3 $j 80
		if (($? != 0)); then
			echo $j >> ./error.log
			exit 1
		fi
        done
done
