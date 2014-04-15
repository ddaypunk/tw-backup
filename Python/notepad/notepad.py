import notepad_funcs
import time

notepad = notepad_funcs.Notepad()

choice = 'y'

while str(choice) != 'n' or str(choice) != 'N':

	choice = raw_input("Would you like to enter anoter note? (Y/N): ")

	note = raw_input("Note? => ")

	#time is in format 'Wkd Mth DD HH:mm:ss YYYY'
	notepad.page.append([time.asctime(time.localtime(time.time())),note])

print notepad.page