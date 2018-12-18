import csv
import pygal

# Show format of file contents.
filename = 'Demographic_Statistics_By_Zip_Code.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Get count of ticipants and juristictions.
filename = 'Demographic_Statistics_By_Zip_Code.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    num_participants = []
    for row in reader:
        num_participants.append(int(row[1]))
    
    juristictions = []
    for row in reader:
        juristictions.append(row[0])
    
# Plot data.
par = pygal.Bar()

par.title = "Participants from Zip Codes."
par.x_labels = juristictions

par.x_title = "Zip Code"
par.y_title = "Number of Participants"

par.add("Number of Participants", num_participants)
par.render_to_file('par_data.svg')



