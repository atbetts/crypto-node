#!/bin/bash
echo "Started Signing of Smartcash" > /home/linaro/SmartCash.log
date >> /home/linaro/SmartCash.log
i=20
j=1
while [ $i -gt 0 ]
do
	if [ -d /media/linaro/EB40-B1B7 ] && [ $i -lt 15 ]; then
		echo "found drive" >> /home/linaro/SmartCash.log
		break
	fi
	echo $i
	i=$(($i-$j))
	sleep 1
done
for file in /media/linaro/EB40-B1B7/*.txn
do
	
	cat $file | sudo -u linaro ./electrum-smart signtransaction - > "$file"".signed"
	echo "Signed ""$file" >> /home/linaro/SmartCash.log
done
