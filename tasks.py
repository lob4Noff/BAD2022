import datetime
import math
import os

while True:
    file_name = input("Enter the name of the file to open (or type 'exit' to exit): ")

    if file_name == "exit":
        print("Closing... Thanks for attention!")
        break
    else:
        try: 
            print(f"[{file_name}] Success! Processing...\n")

            time_start = datetime.datetime.now()

            with open(file_name, "r") as file:
                input_arr = file.readlines()

                for i in range(len(input_arr)):
                    try:
                        input_arr[i] = int(input_arr[i].strip())
                    except AttributeError:
                        pass
                
                max_value = min_value = input_arr[0]
                for elem in input_arr:
                    if max_value < elem:
                        max_value = elem
                    if min_value > elem:
                        min_value = elem
                
                print(f"Max value = {max_value}")
                print(f"Min value = {min_value}")

                sorted_arr = sorted(input_arr)
                #print(f"Max value = {sorted_arr[-1]}")
                #print(f"Min value = {sorted_arr[0]}")

                if len(sorted_arr) % 2 == 1:
                    index = math.floor(len(sorted_arr)/2)
                    print(f"Median = {sorted_arr[index]}")
                else:
                    index_left = int(len(sorted_arr)/2)-1
                    index_right = int(len(sorted_arr)/2)+1
                    print(f"Median = {sum(sorted_arr[index_left : index_right]) / 2}")

            print(f"Average value = {sum(input_arr)/len(input_arr)}")

            max_order = list()
            min_order = list()
            current_order = [input_arr[0]]


            for elem in input_arr:
                if (current_order[-1] < elem) and (len(current_order) == 1):
                    current_order.append(elem)

                elif (current_order[-1] < elem) and (len(current_order) > 1) and (current_order[1] > current_order[0]):
                    current_order.append(elem)

                elif (current_order[-1] > elem):
                    if (len(current_order) > len(max_order)):
                        max_order = current_order.copy()
                    current_order = [elem]

            for elem in input_arr:
                if (current_order[0] > elem) and (len(current_order) == 1):
                    current_order.append(elem)
                elif (current_order[-1] > elem) and (len(current_order) > 1) and (current_order[0] > current_order[1]):
                    current_order.append(elem)
                elif (current_order[-1] < elem) and (len(current_order) > 1):
                    if (len(current_order) > len(min_order)):
                        min_order = current_order.copy()
                    current_order = [elem]

            print(max_order)
            print(min_order)

            print(f"Total time: {datetime.datetime.now() - time_start}")
            print("---------------\n")

        except FileNotFoundError:
            print("Sorry, I can't find this file! Try again, please. Also, I managed to find these files:")
            #print("Maybe, it will help you to find required file:")
            for file in os.listdir():
                if ".txt" in file:
                    print(f"--- {file}")