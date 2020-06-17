from tkinter import *


def gen_passwords():
    """Generate passwords with the provided inputs"""
    if name_entry.get() == '' or 'John' in name_entry.get() or '' in [date_entry_day.get(), date_entry_mon.get(), date_entry_year.get()]:
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


# # Placeholder class for entries
# class PlaceHolderEntry(Entry):
#     def __init__(self, container, placeholder, *args, **kwargs):
#         super(PlaceHolderEntry, self).__init__(container, *args, **kwargs)
#         self.placeholder = placeholder
#         self.insert(1, self.placeholder)
#         self.bind("<FocusIn>", self._clear_placeholder)
#         self.bind("<FocusOut>", self._add_placeholder)
#
#     def _clear_placeholder(self, e):
#         self.delete(0, "end")
#
#
#     def _add_placeholder(self, e):
#         if not self.get():
#             self.insert(0, self.placeholder)


# Creating a main window for the program
window = Tk()

window.title('Password Generator')
window.geometry('500x150+400+150')

# Defaults
small_box_width = 5
large_box_width = 25
button_width = 7
row_set_1 = 0
row_set_2 = 1
row_set_3 = 2
row_set_4 = 3
row_set_5 = 4

# Creating Labels
name_label = Label(window, text='*Name :')
name_label_top = Label(window, text='Enter Full name')
date_label = Label(window, text='    *Birthday :')
date_label_day = Label(window, text='DD', width=small_box_width)
date_label_mon = Label(window, text='|   MM  |', width=small_box_width)
date_label_year = Label(window, text='YYYY', width=small_box_width)
keywords_label = Label(window, text='Keywords :')
keywords_label_top = Label(window, text='Enter Keywords(use comma)')
length_label = Label(window, text='Length :')
length_label_exact = Label(window, text='Exact')
length_label_min = Label(window, text='Min')
length_label_max = Label(window, text='Max')

# Creating Entry boxes
name_entry = Entry(window, width=large_box_width)
date_entry_day = Entry(window, width=small_box_width)
date_entry_mon = Entry(window, width=small_box_width)
date_entry_year = Entry(window, width=small_box_width)
keywords_entry = Entry(window, width=large_box_width)
length_entry_exact = Entry(window, width=small_box_width)
length_entry_min = Entry(window, width=small_box_width)
length_entry_max = Entry(window, width=small_box_width)

# Creating Button to call the generate function
gen_button = Button(window, text='Generate', width=button_width, command=gen_passwords)
clear_name_date = Button(window, text='Clear', width=button_width, command=clear_nd)
clear_keyword_length = Button(window, text='Clear', width=button_width, command=clear_kl)
clear_all = Button(window, text='Clear', width=button_width, command=clear_entries)

# Create Grid
name_label_top.grid(row=row_set_1, column=1), date_label_day.grid(row=row_set_1, column=3), date_label_mon.grid(row=row_set_1, column=4), date_label_year.grid(row=row_set_1, column=5)
name_label.grid(row=row_set_2, column=0, sticky=E), name_entry.grid(row=row_set_2, column=1), date_label.grid(row=row_set_2, column=2, sticky=E), date_entry_day.grid(row=row_set_2, column=3), date_entry_mon.grid(row=row_set_2, column=4), date_entry_year.grid(row=row_set_2, column=5), clear_name_date.grid(row=row_set_2, column=6)
keywords_label_top.grid(row=row_set_3, column=1), length_label_exact.grid(row=row_set_3, column=3), length_label_min.grid(row=row_set_3, column=4), length_label_max.grid(row=row_set_3, column=5)
keywords_label.grid(row=row_set_4, column=0), keywords_entry.grid(row=row_set_4, column=1), length_label.grid(row=row_set_4, column=2, sticky=E), length_entry_exact.grid(row=row_set_4, column=3), length_entry_min.grid(row=row_set_4, column=4), length_entry_max.grid(row=row_set_4, column=5), clear_keyword_length.grid(row=row_set_4, column=6)
gen_button.grid(row=row_set_5, column=2,sticky=E), clear_all.grid(row=row_set_5, column=6)

window.mainloop()
