#udacity_CS_101_Notes 2

#Different ways to write biggest

#using nested ifs

def biggest (a,b,c):
	if a>b:
		if a>c:
			return a
		else:
			return c
	else:
		if b>c:
			return b
		else:
			return c

#not using nested ifs, but using a previous built procedure

def biggest (a,b,c):
	if bigger (a,b) == bigger (a,c):
		return a
	if bigger (a,b) == bigger (b,c):
		return b
	else:
		return c

#the way the prof did it

#def biggest (a,b,c)
#   return bigger (bigger (a,b), c)



def bigger (d,e):
	if d>e:
		return d
	else:
		return e
#end of procedure

#--------------#

#multiple in a for loop

def total_enrollment(p):
	total1 = 0
	total2 = 0
	for name,students,price in p: #notice the list of variables where normally we see e
		total1 = total1 + students
		total2 = total2 + students*price


#----------------#

def convert_seconds(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds / 60)%60)
    seconds = seconds %60
    
    hours_string = " hours, "
    minutes_string = " minutes, "
    seconds_string = " second"

    return str(hours) + (" hour, ", " hours, ")[hours != 1] + str(minutes) + (" minute, ", " minutes, ")[minutes != 1] + str(seconds) + (" second", " seconds")[seconds != 1]

def download_time(fileSize, fileUnits, bandSize, bandUnits):
    #Convert file size to lowest level
    if fileUnits == "kb":
		fileSizeFinal = fileSize * (2 ** 10)
    
    elif fileUnits == "kB":
        fileSizeFinal = fileSize * (2 ** 10 * 8)
        
    elif fileUnits == "Mb":
        fileSizeFinal = fileSize * (2 ** 20)
    
    elif fileUnits == "MB":
        fileSizeFinal = fileSize * (2 ** 20 * 8)
	
    elif fileUnits == "Gb":
		fileSizeFinal = fileSize * (2 ** 30)
        
    elif fileUnits == "GB":
		fileSizeFinal = fileSize * (2 ** 30 * 8)
        
    elif fileUnits == "Tb":
		fileSizeFinal = fileSize * (2 ** 40)
        
    else:
		fileSizeFinal = fileSize * (2 ** 40 * 8)
#Convert Bandwidth to lowest level

    if bandUnits == "kb":
		bandSizeFinal = bandSize * (2 ** 10)
        
    elif bandUnits == "kB":
		bandSizeFinal = bandSize * (2 ** 10 * 8)
        
    elif bandUnits == "Mb":
		bandSizeFinal = bandSize * (2 ** 20)
        
    elif bandUnits == "MB":
		bandSizeFinal = bandSize * (2 ** 20 * 8)
        
    elif bandUnits == "Gb":
		bandSizeFinal = bandSize * (2 ** 30)
        
    elif bandUnits == "GB":
		bandSizeFinal = bandSize * (2 ** 30 * 8)
        
    elif bandUnits == "Tb":
		bandSizeFinal = bandSize * (2 ** 40)
        
    else:
		bandSizeFinal = bandSize * (2 ** 40 * 8)
# format return string
    finalSeconds = float(fileSizeFinal)/bandSizeFinal
    return  convert_seconds(finalSeconds)
