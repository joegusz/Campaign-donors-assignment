# This variable represents the data from the nycdonors-cleanme.csv file as a
# list, with each item representing a string for each row. 
data = open('nycdonors-cleanme.csv', 'r').read().split('\r\n')[1:]

# You'll add your output data here, using the .append() method
output = [data.append('cleaned_data')]

# Hint: Start by looping over the data variable, turn each item into a list,
# and perform the necessary transformations. Once the row has been transformed,
# append it into the output list, like this: output.append(cleaned_row)

########## YOUR CODE GOES HERE ##########

for row in data:
   row = row.split(',')
   row[11] = row[11].upper()
   row[15] = row[15].replace('&nbsp;','')
   row[-1] = float(row[-1])
   row[17] = str(row[17])
   if row[-1] > 5000.0:
       print row
   if row[16] != 'NY':
       print row

