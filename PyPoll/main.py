import csv
import os
from collections import Counter

winner_number = "none"
winner = "none"
wc = 0
percentages = "none"
nc = 0
number_of_votes = 0

candidates = []
contenders = []
list_of_votes = []
dict_of_candidates = dict()
second_try = dict()
third_try = dict()

election_data_path = os.path.join("Resources","election_data.csv")

with open(election_data_path,'r',newline ='',encoding="utf-8") as election_data_file:
    election_data_reader = csv.reader(election_data_file, delimiter=',')
    election_data_header = next(election_data_file)

    for rows in election_data_reader:
        number_of_votes = number_of_votes + 1
        candidates.append(rows[2])


    for candidate in candidates:
          dict_of_candidates[candidate] = dict_of_candidates.get(candidate,0)+1

    for candidate,votes in dict_of_candidates.items():
        contenders.append(candidate)
        list_of_votes.append(votes)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {number_of_votes}")
print("-------------------------")

while nc < len(contenders):
    percentages = round(((int(dict_of_candidates[contenders[nc]]) / int(number_of_votes))*100),2)
    print(f"{contenders[nc]}: {percentages}% ({list_of_votes[nc]})")
    nc = nc + 1

for result in list_of_votes:
    if winner_number == "none":
        winner_number = result
        winner = contenders[wc]
    if winner_number < result:
        winner_number = result
        winner = contenders[wc]
    wc = wc + 1

print("-------------------------")
print(f"Winner: {winner} with {winner_number} of the votes.")
print("--------------------------")

results_path = os.path.join("Analysis","Results.txt")

with open(results_path,"w", newline = "", encoding="utf-8") as my_txt_file:
    my_txt_file.write("Election Results\n")
    my_txt_file.write("-------------------------\n")
    my_txt_file.write(f"Total Votes: {number_of_votes}\n")
    my_txt_file.write("-------------------------\n")
    nc = 0
    while nc < len(contenders):
        percentages = round(((int(dict_of_candidates[contenders[nc]]) / int(number_of_votes))*100),2)
        my_txt_file.write(f"{contenders[nc]}: {percentages}% ({list_of_votes[nc]}) \n")
        nc = nc + 1
    my_txt_file.write("-------------------------\n")
    my_txt_file.write(f"Winner: {winner} with {winner_number} of the votes.\n")
