import sys

index=0
#0 read preamble
#1 read packet number H
#2 read packet number M
#3 read packet number L
#4 read throttle value H
#5 read throttle value L
#6 read output PWM H
#7 read output PWM L
#8 read output RPM H
#9 read output RPM L

f = open(sys.argv[1], "rb")
last_pn=0

byte = 1
try:
	while True:
		byte = [1]
		while byte[0] != 0x9b:
			byte = f.read(1)
			if len(byte)<1:
				break

		byte = f.read(9)
		if len(byte)<9:
			break

		pn=(byte[0]<<16)+(byte[1]<<8)+(byte[2])
		thr=(byte[3]<<8)+byte[4]
		pwm=(byte[5]<<8)+byte[6]
		rpm=(byte[7]<<8)+byte[8]
		
		#if pn == (last_pn+1)&0xffffff:
		print(pn,thr,pwm,rpm,sep=',')
		last_pn = pn
finally:
	f.close()
