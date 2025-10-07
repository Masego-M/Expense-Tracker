import csv
import datetime

file_name = r"C:\Users\maseg\OneDrive - belgiumcampus.ac.za\Documents\Projects\expenses.csv"

def file():
    with open(file_name) as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Expense Date", "Category", "Expense Amount"])
        pass

def add_expense():
    date = input('Enter expense date (YYYY-MM-DD) or leave blank for today:  ')
    if not date:
        date = datetime.date.today().strftime("%Y-%m-%d")

    category = input('Enter expense category: ').strip()
    amount = float(input('Enter expense amount: '))

    with open(file_name, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([date, category, amount])
        print('Expense was successfully added.')

def view_expense():
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            print(f"{row[0]} - {row[1]} - {row[2]}")
            


print('=========Expense Tracker=========')
print('1. Add expenses')
print('2. Monthly Summaries')
print('3. Weekly Summaries')
print('4. Show total per category')

print('Enter your choice: ')
choice = int(input())





