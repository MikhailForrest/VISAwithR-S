# https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_manuals/gb_1/s/sma/SMA100A_OperatingManual_en_14.pdf
# https://www.radiotester.ru/media/pdf/rohdeschwarz_espi3_A38.pdf


from time import sleep
import pyvisa  #https://pypi.org/project/PyVISA/

rm = pyvisa.ResourceManager()
print(rm.list_resources())
sma100A_generator = rm.open_resource('TCPIP::172.10.168.23::INSTR') # in settings of generator
epsi3_analyzer = rm.open_resource('') 

print(sma100A_generator)

sma100A_generator.write('*IDN?')
print(sma100A_generator.read())

sma100A_generator.timeout = 2500 #setting the waiting time

sma100A_generator.write("SOUR:POW:POW -40") #changing the signal level
sma100A_generator.write("SOUR:FREQ:FREQ 1.5 MHz") #frequency tuning
sma100A_generator.write("AM:STAT ON") # enabling AM modulation
sma100A_generator.write("AM:SOUR INT") #Selects the modulation signal source for amplitude modulation
sma100A_generator.write("AM:DEPT 50") #sets a modulation depth of 50 %
sma100A_generator.write("LFO1:FREQ 1.0kHz") #sets frequency LF generator

sma100A_generator.write("OUTP ON") #disabling/enabling the RF signal
sleep(3) #in sec

sma100A_generator.write("OUTP OFF") #disabling/enabling the RF signal
sma100A_generator.write("AM:STAT OFF") #


sma100A_generator.get_visa_attribute





