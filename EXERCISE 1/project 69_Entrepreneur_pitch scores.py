#integer python
scores = [ 64, 80, 75,90,] 

total= sum(scores)
average= total/ len(scores)
minimum = min(scores)
maximum = max(scores)

print(f"Total Score: {total}")  
print(f"Average Score: {average:.2f}") 
print(f"Minimum Score: {minimum}")
print(f"Maximum Score: {maximum}\n")
#strings
report=(
    f"Entrepreneur pitch scores report:\n"
    f"Total of entrepreneur pitch scores:{total}\n"
     f"Average of entrepreneur pitch scores:{average}\n"
)
print(report)
#boolean
average = 75      
threshold = 50    
maximum = 95       

if average > threshold and maximum > 50: 
    print("Above Standard")
else:
    print("Below Standard")
print()
#lists
scores = [85, 92, 78, 90, 88]
scoreslist = scores.copy()
print("Original List:", scoreslist)

scoreslist.append(95)

scoreslist = [s for s in scoreslist if s >= 65]

scoreslist.sort()
print("Modified & Sorted List:", scoreslist, "\n")
#arrays
import array
scores = [85, 92, 78, 90, 88]
arrayscore = array.array('i', scores[:4])  
arraysum = sum(arrayscore)
print("Array Scores:", arrayscore.tolist())
print("Array Sum:", arraysum)
print("List Sum (same subset):", sum(scores[:4]), "\n")
#dictionaries
records = [
    {"id": 1, "name": "Alice", "value": 92},
    {"id": 2, "name": "Anitha", "value": 88},
    {"id": 3, "name": "Ganza", "value": 72},
]

print("Original Records:", records)

for rec in records:
    if rec["name"] == "Alice":
        rec["value"] = 90

records = [rec for rec in records if rec["name"] != "Ganza"]

totalvalues = sum(rec["value"] for rec in records)
print("Updated Records:", records)
print(f"Total of Values after Update/Delete: {totalvalues}")