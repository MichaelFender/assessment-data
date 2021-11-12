log_file = open("um-server-01.txt") #allows this .py to use the data in the .txt file


def sales_reports(log_file): #passes "log_file" into the new function "sales_reports"
    for line in log_file: #loop over each line in the txt file
        line = line.rstrip() #rstrip removes trailing characters
        day = line[0:3] #selects the line in a particular day
        if day == "Tue": #singles out day if = "Tue"
            print(line) #will print out Monday's reports to the terminal


sales_reports(log_file)#will show the full result from the function
