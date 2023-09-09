#!/bin/python3
import psutil
import subprocess as sb
import time
while True:
	sb.run("clear")
	var=psutil.cpu_freq(True)
	i=1
	for freq in var:
		print("CORE "+str(i)+ "	{ Cur: "+str(freq.current)+"	,Min: "+str(freq.min)+"	,Max: "+str(freq.max)+" }")
		i+=1
	time.sleep(0.5)