from tkinter import *


def gen_passwords():
    """Generate passwords with the provided inputs"""
    if name_entry.get() == '' or 'John' in name_entry.get() or '' in [date_entry_day.get(), date_entry_mon.get(),
                                                                      date_entry_year.get()] or date_entry_day.get() == 'dd' or date_entry_mon.get() == 'mm' or date_entry_year.get() == 'yyyy':
        return None  # Return None if the entries are empty or basic values

    # Generate Name Permutations
    name_list = name_entry.get().split(' ')
    Nlist = name_permutations(name_list)
    Ulist = name_permutations([x.upper() for x in name_list])
    Llist = name_permutations([x.lower() for x in name_list])
    combined_list_of_names = []
    remove_duplicate(Nlist, combined_list_of_names)
    remove_duplicate(Ulist, combined_list_of_names)
    remove_duplicate(Llist, combined_list_of_names)

    # Generate Date Permutations
    date_list = [date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()]
    list_of_dates = date_permutations(date_list)
    list_of_corrected_dates = []
    remove_duplicate(list_of_dates, list_of_corrected_dates)

    # Combine Names and Dates together with symbols and without symbols
    combined_list_of_names_and_dates = combine_names_and_dates(combined_list_of_names, list_of_corrected_dates)

    # Create File with the specific name
    filename = name_list[0] + '.txt'
    file = open(filename, 'w+')
    file.write('Possible common passwords with the inputs "{}" as name and "{}/{}/{}" as birthday are as follows :\n'.format(name_entry.get(),
                                                                                                                             date_entry_day.get(),
                                                                                                                             date_entry_mon.get(),
                                                                                                                             date_entry_year.get()))
    file.write('NOTE ALL THE PASSWORDS PROVIDED BELOW ARE JUST A RESULT OF MULTIPLE PERMUTATIONS AND COMBINATIONS.\n')
    file.write('Total number of passwords found : {}'.format(len([x for x in combined_list_of_names_and_dates if 7 < len(x) < 17])))
    file.write('\n')
    for i in combined_list_of_names_and_dates:
        if 7 < len(i) < 17:
            file.write(i + '\n')  # Write possible options to file
    file.close()  # Closing the file after done

    # Resetting Entries for another input
    name_entry.delete(0, END)
    date_entry_day.delete(0, END)
    date_entry_mon.delete(0, END)
    date_entry_year.delete(0, END)


def name_permutations(name_list):
    """Divide the name into list with space as the splitter and using three for loops for now in terms of Fullname Middlename Lastname and
        also using abbreviations of different combinations """
    list_of_name_perms = []
    for i in name_list:
        list_of_name_perms.append(i)
        list_of_name_perms.append(i[0])
        for j in name_list:
            if i is not j:
                list_of_name_perms.append(i + j)
                list_of_name_perms.append(i + j[0])
                list_of_name_perms.append(i[0] + j)
                list_of_name_perms.append(i[0] + j[0])
                list_of_name_perms.append(i + j[0].upper())
                list_of_name_perms.append(i[0].upper() + j)
                list_of_name_perms.append(i[0].upper() + j[0].upper())
                list_of_name_perms.append(i + j[0].lower())
                list_of_name_perms.append(i[0].lower() + j)
                list_of_name_perms.append(i[0].lower() + j[0].lower())
                list_of_name_perms.append(i[0].lower() + j[0].upper())
                list_of_name_perms.append(i[0].upper() + j[0].lower())
            for k in name_list:
                if i != j and j != k and i != k:
                    list_of_name_perms.append(i + j + k)
                    list_of_name_perms.append(i + j + k[0])
                    list_of_name_perms.append(i + j[0] + k)
                    list_of_name_perms.append(i + j[0] + k[0])
                    list_of_name_perms.append(i[0] + j + k)
                    list_of_name_perms.append(i[0] + j + k[0])
                    list_of_name_perms.append(i[0] + j[0] + k)
                    list_of_name_perms.append(i[0] + j[0] + k[0])
                    list_of_name_perms.append(i + j + k[0].upper())
                    list_of_name_perms.append(i + j[0].upper() + k)
                    list_of_name_perms.append(i + j[0].upper() + k[0].upper())
                    list_of_name_perms.append(i[0].upper() + j + k)
                    list_of_name_perms.append(i[0].upper() + j + k[0].upper())
                    list_of_name_perms.append(i[0].upper() + j[0].upper() + k)
                    list_of_name_perms.append(i[0].upper() + j[0].upper() + k[0].upper())
                    list_of_name_perms.append(i + j + k[0].lower())
                    list_of_name_perms.append(i + j[0].lower() + k)
                    list_of_name_perms.append(i + j[0].lower() + k[0].lower())
                    list_of_name_perms.append(i[0].lower() + j + k)
                    list_of_name_perms.append(i[0].lower() + j + k[0].lower())
                    list_of_name_perms.append(i[0].lower() + j[0].lower() + k)
                    list_of_name_perms.append(i[0].lower() + j[0].lower() + k[0].lower())
                    list_of_name_perms.append(i + j[0].upper() + k[0].lower())
                    list_of_name_perms.append(i[0].upper() + j + k[0].lower())
                    list_of_name_perms.append(i[0].upper() + j[0].lower() + k)
                    list_of_name_perms.append(i + j[0].lower() + k[0].upper())
                    list_of_name_perms.append(i[0].lower() + j + k[0].upper())
                    list_of_name_perms.append(i[0].lower() + j[0].upper() + k)
                    list_of_name_perms.append(i[0].upper() + j[0].upper() + k[0].lower())
                    list_of_name_perms.append(i[0].upper() + j[0].lower() + k[0].upper())
                    list_of_name_perms.append(i[0].upper() + j[0].lower() + k[0].lower())
                    list_of_name_perms.append(i[0].lower() + j[0].upper() + k[0].upper())
                    list_of_name_perms.append(i[0].lower() + j[0].upper() + k[0].lower())
                    list_of_name_perms.append(i[0].lower() + j[0].lower() + k[0].upper())
    return list_of_name_perms


def date_permutations(date_list):
    """Using the date list and creating different ways in which a date can be used"""
    list_of_birthday_perms = []
    for i in date_list:
        if len(i) < 4:
            list_of_birthday_perms.append(i)
            if '0' in i:
                list_of_birthday_perms.append(i.strip('0'))
            for j in date_list:
                if len(j) < 4 and (i != j or int(i) < 13):
                    list_of_birthday_perms.append(i + j)
                    if '0' in i and '0' in j:
                        list_of_birthday_perms.append(i.strip('0') + j.strip('0'))
                        list_of_birthday_perms.append(i.strip('0') + j)
                        list_of_birthday_perms.append(i + j.strip('0'))
                    elif '0' in i:
                        list_of_birthday_perms.append(i.strip('0') + j)
                    elif '0' in j:
                        list_of_birthday_perms.append(i + j.strip('0'))
                    for k in date_list:
                        if len(k) > 2:
                            list_of_birthday_perms.append(k)
                            list_of_birthday_perms.append(i + j + k)
                            if '0' in i and '0' in j:
                                list_of_birthday_perms.append(i.strip('0') + j.strip('0') + k)
                                list_of_birthday_perms.append(i.strip('0') + j + k)
                                list_of_birthday_perms.append(i + j.strip('0') + k)
                            elif '0' in i:
                                list_of_birthday_perms.append(i.strip('0') + j + k)
                            elif '0' in j:
                                list_of_birthday_perms.append(i + j.strip('0') + k)
                            list_of_birthday_perms.append(k + i + j)
                            if '0' in i and '0' in j:
                                list_of_birthday_perms.append(k + i.strip('0') + j.strip('0'))
                                list_of_birthday_perms.append(k + i.strip('0') + j)
                                list_of_birthday_perms.append(k + i + j.strip('0'))
                            elif '0' in i:
                                list_of_birthday_perms.append(k + i.strip('0') + j)
                            elif '0' in j:
                                list_of_birthday_perms.append(k + i + j.strip('0'))
                            list_of_birthday_perms.append(k[2:])
                            list_of_birthday_perms.append(i + j + k[2:])
                            if '0' in i and '0' in j:
                                list_of_birthday_perms.append(i.strip('0') + j.strip('0') + k[2:])
                                list_of_birthday_perms.append(i.strip('0') + j + k[2:])
                                list_of_birthday_perms.append(i + j.strip('0') + k[2:])
                            elif '0' in i:
                                list_of_birthday_perms.append(i.strip('0') + j + k[2:])
                            elif '0' in j:
                                list_of_birthday_perms.append(i + j.strip('0') + k[2:])
                            list_of_birthday_perms.append(k[2:] + i + j)
                            if '0' in i and '0' in j:
                                list_of_birthday_perms.append(k[2:] + i.strip('0') + j.strip('0'))
                                list_of_birthday_perms.append(k[2:] + i.strip('0') + j)
                                list_of_birthday_perms.append(k[2:] + i + j.strip('0'))
                            elif '0' in i:
                                list_of_birthday_perms.append(k[2:] + i.strip('0') + j)
                            elif '0' in j:
                                list_of_birthday_perms.append(k[2:] + i + j.strip('0'))
    return list_of_birthday_perms


def remove_duplicate(curr_list, combined_list):
    """Remove Duplicate elements from the created lists"""
    count = 0
    for curr in curr_list:
        if curr not in combined_list:
            combined_list.append(curr)
        else:
            count += 1
    return count


def combine_names_and_dates(combined_list_of_names, list_of_corrected_dates):
    """Using the final lists of names and dates and further combining them together with symbols and also without them to form all possible
        outputs """
    combined_list_of_both = []
    for i in combined_list_of_names:
        combined_list_of_both.append(i)
        for j in list_of_corrected_dates:
            for k in ['', '@', '#', '_']:
                combined_list_of_both.append(i + k + j)
                combined_list_of_both.append(j + k + i)

    return combined_list_of_both


# Creating a main window for the program
window = Tk()
window.title('Password Generator')
window.geometry('300x100')

# Creating Labels
name_label = Label(window, text='Enter Full Name :')
date_label = Label(window, text='Birthday :')

# Creating Entry boxes
name_entry = Entry(window, width='17')
name_entry.insert(0, 'John')
date_entry_day = Entry(window, width='5')
date_entry_day.insert(0, 'dd')
date_entry_mon = Entry(window, width='5')
date_entry_mon.insert(0, 'mm')
date_entry_year = Entry(window, width='5')
date_entry_year.insert(0, 'yyyy')

# Creating Button to call the generate function
gen_button = Button(window, text='Generate', command=gen_passwords, width='14')

# Creating grid for all the widgets
name_label.grid(row=0, sticky=E)
date_label.grid(row=1, sticky=E)
name_entry.grid(row=0, column=1, columnspan=3)
date_entry_day.grid(row=1, column=1)
date_entry_mon.grid(row=1, column=2)
date_entry_year.grid(row=1, column=3)
gen_button.grid(row=2, column=1, columnspan=3)
window.mainloop()
