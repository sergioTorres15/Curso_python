import pickle
import sleep
from tkinter import *
from tkinter import ttk
from contact import Contact





ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]




def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? : ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)

def add_contact(contacts, name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)
    return contact


def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact ["name"]).grid(column=1, row=row)
    ttk.Label(frame_contact_list, text=contact ["email"]).grid(column=2, row=row)
    ttk.Label(frame_contact_list, text=contact ["phone"]).grid(column=3, row=row)





def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "),input("Teléfono: "),input("Email: "))
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    contact_a_deleted = input("busca un contacto :")
    contactos_encontrados = []
    contador = 0
    indices = []
    print("\ncontactos encontrados : \n")
    for contacto in contacts:
        if contacto["name"].find(contact_a_deleted) >= 0:
            contactos_encontrados.append(contacto)
            print("{} -{}".format(contador, contacto["name"]))
            indices.append(contador)
            contador += 1
    indice = 0
    if len(indices) >= 0:
        indice = ask_until_option_expected(indices)
        contacts.pop(indice)
        print("El contacto se ha eliminado correctamente")

    elif len(indices) < 0:
        print("no se ha encontrado ninguno")

    sleep(2)

def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    option = input("Desea buscar por [1] nombre / [2] email : ")

    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if option == "1":
            if contact.name.find(search_term) >= 0:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact.name))
                contact_indexes.append(contact_counter)
                contact_counter += 1
        elif option == "2":
            if contact.email.find(search_term) >= 0:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact.name))
                contact_indexes.append(contact_counter)
                contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        volver = input("\nquieres volver a intentar [si] / volver al menu [no] : ")
        if volver == "si":
            find_contact(contacts)
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index].name))
    contact = found_contacts[contact_index]
    contact.print_data()
    sleep(2)




def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = []




    root = Tk()
    root.title("Agenda de Contactos")
    root.config(bg="pink")



    frame_add_contact = Frame(root, width="50", height=50, bg="pink")
    frame_add_contact.grid()



    frame_contact_list = Frame(root, width="50", height="50", bg="pink")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()



    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1)

    ttk.Entry(frame_add_contact, width=20, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=26, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=phone).grid(column=3, row=2)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=2)
    ttk.Label(frame_contact_list, text="email").grid(column=2, row=2)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=3, row=2)

    ttk.Button(frame_add_contact,
               text="SAVE",
               command=lambda: save_contacts(contacts)
               ).grid(column=4, row=3)


    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda:add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3)
    contact=load_contacts()

    ttk.Button(frame_add_contact,
               text="VIEW",
               command=lambda:contact
               ).grid(column=3, row=4)

    Button(frame_add_contact, text="EXIT", command=root.destroy,bg="red", fg="white").grid(column=4, row=5)

    for date in frame_add_contact.winfo_children():
        date.grid_configure(padx=5, pady=5)

    for campo in frame_contact_list.winfo_children():
            campo.grid_configure(padx=8, pady=8)
    load_contacts()

    root.mainloop()

if __name__ == "__main__":
    main()