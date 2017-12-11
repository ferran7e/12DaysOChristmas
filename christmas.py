from time import sleep
import os

number_to_text = ['A', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
past_to_text = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth']
items = ['{} Partridge in a Pear Tree', '{} Turtle Doves', '{} French Hens', '{} Calling Birds', '***{} Golden Rings***', '{} Geese a Laying', '{} Swans a Swimming', '{} Maids a Milking', '{} Ladies Dancing', '{} Lords a Leaping', '{} Pipers Piping', '{} Drummers Drumming']


choice = input("Would you like listen to the Twelve Days of Christmas? (Y/N)").lower()

while choice == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    count = 1
    while count < 12:
        for item in number_to_text:
            sleep(2)
            print("On the " + past_to_text[count-1] + " day of Christmas my true love sent to me:")
            sleep(1.25)
            output = items[:count]

            new_list = []
            for o in output:
                new_list.append(o.format(number_to_text[output.index(o)]))

            for i in new_list[::-1]:
                print(i)
                sleep(1.5)
            if count != 12:
                os.system('cls' if os.name == 'nt' else 'clear')
            count+=1

    choice = input("\nWould you like to listen again? (Y/N): ").lower()

if choice in ('y', 'n') != True:
    print('Have a Merry Christmas and a Happy New Year!! :)')





