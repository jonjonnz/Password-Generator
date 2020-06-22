from tkinter import *
from tkinter import messagebox


def gen_passwords():
    """Generate passwords with the provided inputs"""
    if name_entry.get() == '' or 'John' in name_entry.get() or '' in [date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()]:
        return None  # Return None if the entries are empty or basic values
    if len([x for x in name_entry.get().split(' ') if not x.isalpha()]) > 0:
        messagebox.showerror('Incorrect input', 'Please enter a valid name, "{}" not allowed'.format(name_entry.get()))
        name_entry.delete(0, END)
        return None  # Return None if name is not valid
    if not date_entry_day.get().isdigit() or not date_entry_mon.get().isdigit() or not date_entry_year.get().isdigit():
        messagebox.showerror('Incorrect input', 'Please enter a valid numeric date, "{}/{}/{}" not allowed'.format(date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()))
        if not date_entry_day.get().isdigit():
            date_entry_day.delete(0, END)
        if not date_entry_mon.get().isdigit():
            date_entry_mon.delete(0, END)
        if not date_entry_year.get().isdigit():
            date_entry_year.delete(0, END)
        return None  # Return None if date is not valid
    if len(date_entry_day.get()) > 2 or (not date_entry_day.get().startswith('0') and int(date_entry_day.get()) > 31) or int(date_entry_day.get()) == 0:
        messagebox.showerror('Incorrect input', 'Please enter a valid date, "{}/{}/{}" not allowed'.format(date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()))
        date_entry_day.delete(0, END)
        return None  # Return None if day is not valid
    if len(date_entry_mon.get()) > 2 or (not date_entry_mon.get().startswith('0') and int(date_entry_mon.get()) > 12) or int(date_entry_mon.get()) == 0:
        messagebox.showerror('Incorrect input', 'Please enter a valid date, "{}/{}/{}" not allowed'.format(date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()))
        date_entry_mon.delete(0, END)
        return None  # Return None if month is not valid
    if len(date_entry_year.get()) < 4 or int(date_entry_year.get()) == 0:
        messagebox.showerror('Incorrect input', 'Please enter a valid date, "{}/{}/{}" not allowed'.format(date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()))
        date_entry_year.delete(0, END)
        return None  # Return None if year is not valid

    # Basic lists
    symbol_list = ['', '@', '#', '_']
    combined_list_of_names = []
    list_of_corrected_dates = []

    # Append Keywords
    if keywords_entry.get() != '':
        keywords = keywords_entry.get().split(',')
        for key in keywords:
            if key.isalpha():
                combined_list_of_names.append(key)
            elif key.isdigit():
                list_of_corrected_dates.append(key)
            elif key.isalnum():
                pass
            else:
                if key not in symbol_list:
                    symbol_list.append(key)

    # Generate Name Permutations
    name_list = name_entry.get().split(' ')
    normal_case_list = name_permutations(name_list)
    upper_case_list = name_permutations([x.upper() for x in name_list])
    lower_case_list = name_permutations([x.lower() for x in name_list])
    remove_duplicate(normal_case_list, combined_list_of_names)
    remove_duplicate(upper_case_list, combined_list_of_names)
    remove_duplicate(lower_case_list, combined_list_of_names)

    # Generate Date Permutations
    date_list = [date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()]
    list_of_dates = date_permutations(date_list)
    remove_duplicate(list_of_dates, list_of_corrected_dates)

    # Combine Names and Dates together with symbols and without symbols
    combined_list_of_names_and_dates = combine_names_and_dates(combined_list_of_names, list_of_corrected_dates, symbol_list)

    # Get Length
    exact_length = int(length_entry_exact.get()) if length_entry_exact.get() is not None and length_entry_exact.get() != '' else None
    min_length = int(length_entry_min.get() if length_entry_min.get() and length_entry_min.get() != '' else 8)
    max_length = int(length_entry_max.get() if length_entry_max.get() and length_entry_max.get() != '' else 16)

    # Create File with the specific name
    filename = name_list[0] + '_' + date_entry_day.get() + date_entry_mon.get() + date_entry_year.get() + '__' + ((str(min_length) + '_' + str(max_length)) if exact_length is None else str(exact_length)) + '.txt'
    file = open(filename, 'w+')
    file.write('Possible common passwords with the inputs "{}" as name and "{}/{}/{}" as birthday are as follows :\n'.format(name_entry.get(), date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()))
    file.write('NOTE ALL THE PASSWORDS PROVIDED BELOW ARE JUST A RESULT OF MULTIPLE PERMUTATIONS AND COMBINATIONS.\n')
    file.write('Total number of passwords found : {}'.format(len([x for x in combined_list_of_names_and_dates if min_length - 1 < len(x) < max_length + 1]) if exact_length is None else len([x for x in combined_list_of_names_and_dates if len(x) == exact_length])))
    file.write('\n')
    if exact_length is None:
        for i in combined_list_of_names_and_dates:
            if min_length - 1 < len(i) < max_length + 1:
                file.write(i + '\n')  # Write possible options to file
    else:
        for i in combined_list_of_names_and_dates:
            if len(i) == exact_length:
                file.write(i + '\n')
    file.close()  # Closing the file after done


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


def combine_names_and_dates(combined_list_of_names, list_of_corrected_dates, list_of_symbols):
    """Using the final lists of names and dates and further combining them together with symbols and also without them to form all possible
        outputs """
    combined_list_of_both = []
    for i in combined_list_of_names:
        combined_list_of_both.append(i)
        for j in list_of_corrected_dates:
            for k in list_of_symbols:
                combined_list_of_both.append(i + k + j)
                combined_list_of_both.append(j + k + i)

    return combined_list_of_both


def clear_entries():
    clear_nd()
    clear_kl()


def clear_kl():
    keywords_entry.delete(0, END)
    length_entry_exact.delete(0, END)
    length_entry_min.delete(0, END)
    length_entry_max.delete(0, END)


def clear_nd():
    name_entry.delete(0, END)
    date_entry_day.delete(0, END)
    date_entry_mon.delete(0, END)
    date_entry_year.delete(0, END)


# Creating a main window for the program
window = Tk()

window.title('Password Generator')

# Defaults
small_entry_box_width = 4
large_entry_box_width = 25
button_width = 7

# Frames
frame_1 = Frame(window)

# Creating Labels
name_label = Label(frame_1, text='*Name :')
name_label_top = Label(frame_1, text='Enter Full name')
date_label = Label(frame_1, text='    *Birthday :')
date_label_day = Label(frame_1, text='DD', width=small_entry_box_width)
date_label_mon = Label(frame_1, text='|   MM   |', width=small_entry_box_width + 2)
date_label_year = Label(frame_1, text='YYYY', width=small_entry_box_width)
keywords_label = Label(frame_1, text='Keywords :')
keywords_label_top = Label(frame_1, text='Enter Keywords(use comma)')
length_label = Label(frame_1, text='Length :')
length_label_exact = Label(frame_1, text='Exact')
length_label_min = Label(frame_1, text='Min')
length_label_max = Label(frame_1, text='Max')

# Creating Entry boxes
name_entry = Entry(frame_1, width=large_entry_box_width)
date_entry_day = Entry(frame_1, width=small_entry_box_width)
date_entry_mon = Entry(frame_1, width=small_entry_box_width)
date_entry_year = Entry(frame_1, width=small_entry_box_width + 1)
keywords_entry = Entry(frame_1, width=large_entry_box_width)
length_entry_exact = Entry(frame_1, width=small_entry_box_width)
length_entry_min = Entry(frame_1, width=small_entry_box_width)
length_entry_max = Entry(frame_1, width=small_entry_box_width)

# Creating Button to call the generate function
gen_button = Button(frame_1, text='Generate', width=button_width, command=gen_passwords)
clear_all = Button(frame_1, text='Clear All', width=button_width, command=clear_entries)
clear_name_date = Button(frame_1, text='Clear', width=button_width, command=clear_nd)
clear_keyword_length = Button(frame_1, text='Clear', width=button_width, command=clear_kl)

# Create Grid
name_label_top.grid(row=0, column=1, sticky=W), date_label_day.grid(row=0, column=3), date_label_mon.grid(row=0, column=4), date_label_year.grid(row=0, column=5)
name_label.grid(row=1, column=0, sticky=E), name_entry.grid(row=1, column=1), date_label.grid(row=1, column=2, sticky=E), date_entry_day.grid(row=1, column=3), date_entry_mon.grid(row=1, column=4), date_entry_year.grid(row=1, column=5), clear_name_date.grid(row=1, column=6)
keywords_label_top.grid(row=2, column=1, sticky=W), length_label_exact.grid(row=2, column=3), length_label_min.grid(row=2, column=4), length_label_max.grid(row=2, column=5)
keywords_label.grid(row=3, column=0), keywords_entry.grid(row=3, column=1), length_label.grid(row=3, column=2, sticky=E), length_entry_exact.grid(row=3, column=3), length_entry_min.grid(row=3, column=4), length_entry_max.grid(row=3, column=5), clear_keyword_length.grid(row=3, column=6)
gen_button.grid(row=4, column=1, sticky=W), clear_all.grid(row=4, column=6)

# Create packing
frame_1.pack(side=TOP, padx=15, pady=15)

window.mainloop()
