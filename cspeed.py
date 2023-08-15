#!/bin/python3
import psutil
import subprocess as sb
import time
while True:
	sb.run("clear")
	var=psutil.cpu_freq(True)
	print(*var,sep='\n')
	time.sleep(0.5)