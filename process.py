log_file = open("um-server-01.txt") #allows this .py to use the data in the .txt file


# def sales_reports(log_file): #passes "log_file" into the new function "sales_reports"
#     for line in log_file: #loop over each line in the txt file
#         line = line.rstrip() #rstrip removes trailing characters
#         day = line[0:3] #portion of row
#         if day == "Mon": #singles out day if = "Mon"
#             print(line) #will print out Monday's reports to the terminal

# sales_reports(log_file)#will show the full result from the function

def over_ten(log_file):
    for line in log_file:
        line = line.rstrip()
        orders = line[16:18]
        if orders >= '10': #  == '10' gives me all orders that delivered 10 melons - <= gives all orders 
            print (line)
over_ten(log_file)
