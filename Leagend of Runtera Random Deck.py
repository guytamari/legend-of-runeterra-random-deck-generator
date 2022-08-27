import random
import xlsxwriter
import time
A = 0
t = 2
regions = ["Bandle City", "Bilgewater", "Demacia", "Freljord", "Ionia", "Noxus", "Piltover & Zaun", "Shadow Isles", "Shurima","Targon"]
def main_program(A):
    global time
    workbook = xlsxwriter.Workbook(f'RandomDeck {A} .xlsx')
    worksheet = workbook.add_worksheet()
    print("Choosing two regions... ")
    region_pick = str(random.sample(regions, 2))
    time.sleep(t)
    print("The regions is: {}".format(region_pick))
    num_shoras = int(input("Enter Number of Columns: "))
    num_tors = int(input("Enter Number of Rows: "))
    print("Ok, The Excel File is now at your folder you currently on...")
    list_shorot = []
    list_tors = []
    for x in range(1, num_shoras + 1):
        list_shorot.append(x)
    for x in range(1, num_tors + 1):
        list_tors.append(x)
    worksheet.write('A1', region_pick)
    worksheet.write('A2', "Row")
    worksheet.write('B2', "Column")
    worksheet.write('C2', "Amount")
    x = 2

    for time in range(40):
        chosen_shora = random.choice(list_shorot)
        chosen_tor = random.choice(list_tors)
        num_of_times = random.randint(1, 3)
        x += 1
        worksheet.write('A' + str(x), chosen_tor)
        worksheet.write('B' + str(x), chosen_shora)
        worksheet.write('C' + str(x), num_of_times)
    workbook.close()
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        main_program(A + 1)
    if restart == "n" or restart == "no":
        print("Bye...")

main_program(A)