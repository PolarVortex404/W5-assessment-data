log_file = open("um-server-01.txt") #function opens the 'um-server-01.txt' file


def sales_reports(log_file): # the def keyword defines a function, the colon marks the beginning of its body
    for line in log_file: # iterable 
        line = line.rstrip() # creates variable called 'line', sets equal to itself while the rstrip() function removes any trailing characters
        day = line[0:3] #creates variable called 'day', sets equal to 'line' with an index of '[0:3]'
        if day == "Tue": #if the day is equal to the string 'Tue', the following line will execute
            print(line) #prints to the console 

sales_reports(log_file)
