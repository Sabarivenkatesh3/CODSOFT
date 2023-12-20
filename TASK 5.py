import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")

def view_contact_list():
    if not contacts:
        messagebox.showinfo("Empty List", "Contact list is empty.")
    else:
        contact_list.delete(0, tk.END)
        for idx, contact in enumerate(contacts, start=1):
            contact_list.insert(tk.END, f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    search_term = search_entry.get()
    if not search_term:
        messagebox.showwarning("Warning", "Enter a name or phone number to search.")
        return

    found_contacts = []
    contact_list.delete(0, tk.END)

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            found_contacts.append(contact)

    if not found_contacts:
        messagebox.showinfo("No Match", "No matching contacts found.")
    else:
        for idx, found_contact in enumerate(found_contacts, start=1):
            contact_list.insert(tk.END, f"{idx}. Name: {found_contact['Name']}, Phone: {found_contact['Phone']}")

def update_contact():
    selection = contact_list.curselection()
    if not selection:
        messagebox.showwarning("Warning", "Select a contact to update.")
        return

    index = selection[0]
    contact = contacts[index]

    update_window = tk.Toplevel()
    update_window.title("Update Contact")

    frame = tk.Frame(update_window)
    frame.pack(padx=10, pady=10)

    label_name = tk.Label(frame, text="Name:")
    label_name.grid(row=0, column=0, sticky="w")
    name_entry_update = tk.Entry(frame)
    name_entry_update.grid(row=0, column=1)
    name_entry_update.insert(tk.END, contact['Name'])

    label_phone = tk.Label(frame, text="Phone:")
    label_phone.grid(row=1, column=0, sticky="w")
    phone_entry_update = tk.Entry(frame)
    phone_entry_update.grid(row=1, column=1)
    phone_entry_update.insert(tk.END, contact['Phone'])

    label_email = tk.Label(frame, text="Email:")
    label_email.grid(row=2, column=0, sticky="w")
    email_entry_update = tk.Entry(frame)
    email_entry_update.grid(row=2, column=1)
    email_entry_update.insert(tk.END, contact['Email'])

    label_address = tk.Label(frame, text="Address:")
    label_address.grid(row=3, column=0, sticky="w")
    address_entry_update = tk.Entry(frame)
    address_entry_update.grid(row=3, column=1)
    address_entry_update.insert(tk.END, contact['Address'])

    def update_contact_info():
        contact['Name'] = name_entry_update.get()
        contact['Phone'] = phone_entry_update.get()
        contact['Email'] = email_entry_update.get()
        contact['Address'] = address_entry_update.get()
        messagebox.showinfo("Success", "Contact updated successfully.")
        update_window.destroy()
        view_contact_list()

    update_button = tk.Button(frame, text="Update Contact", command=update_contact_info)
    update_button.grid(row=4, columnspan=2, pady=5)

def delete_contact():
    selection = contact_list.curselection()
    if not selection:
        messagebox.showwarning("Warning", "Select a contact to delete.")
        return

    index = selection[0]
    del contacts[index]
    messagebox.showinfo("Success", "Contact deleted successfully.")
    view_contact_list()

root = tk.Tk()
root.title("Contact Book")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_name = tk.Label(frame, text="Name:")
label_name.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

label_phone = tk.Label(frame, text="Phone:")
label_phone.grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(frame)
phone_entry.grid(row=1, column=1)

label_email = tk.Label(frame, text="Email:")
label_email.grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1)

label_address = tk.Label(frame, text="Address:")
label_address.grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1)

add_button = tk.Button(frame, text="Add Contact", command=add_contact)
add_button.grid(row=4, columnspan=2, pady=5)

search_entry = tk.Entry(frame)
search_entry.grid(row=5, columnspan=2, pady=5)

search_button = tk.Button(frame, text="Search Contact", command=search_contact)
search_button.grid(row=6, columnspan=2, pady=5)

contact_list = tk.Listbox(frame, width=40)
contact_list.grid(row=7, columnspan=2, pady=5)

update_button = tk.Button(frame, text="Update Contact", command=update_contact)
update_button.grid(row=8, columnspan=2, pady=5)

delete_button = tk.Button(frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=9, columnspan=2, pady=5)

root.mainloop()
