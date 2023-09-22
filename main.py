import tkinter as tk
import customtkinter as ctk

win = tk.Tk()
win.title('Todo App')
win.geometry('750x450')
photo = tk.PhotoImage(file='m.png')
win.iconphoto(True, photo)
win.config(bg='#87CEEB')
#win.resizable(True, True)
win["bg"] = "#F1F1F1"

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder=None, font=None):
        super().__init__(master, font=font)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']
            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()

def add_def():
    task = add_todo.get()
    if task.strip():  # Проверяем, что задача не пуста
        listbox.insert(tk.END, task)
        add_todo.delete(0, tk.END)  # Очищаем поле ввода


def edit_def():
    selected_index = listbox.curselection()  # Получаем индексы выбранных элементов
    if selected_index:
        selected_item = listbox.get(selected_index)  # Получаем выбранный элемент
        edit_window = tk.Toplevel(win)
        edit_window.title('Edit Item')

        edit_todo = EntryWithPlaceholder(edit_window, font=('Arial', 10))
        edit_todo.grid(row=0, column=0, sticky="we", padx=5, pady=5)

        # При открытии окна редактирования, заполните поле ввода текущим значением элемента
        edit_todo.insert(tk.END, selected_item)

        def save_edit():
            new_text = edit_todo.get()
            if new_text.strip():
                # Удалите выбранный элемент из listbox
                listbox.delete(selected_index)
                # Добавьте отредактированный элемент обратно в listbox
                listbox.insert(tk.END, new_text)
                edit_window.destroy()

        save_button = ctk.CTkButton(edit_window, text="Save", corner_radius=5, bg_color="white", width=50,
                                    command=save_edit)
        save_button.grid(row=1, column=0, padx=5, pady=10)

def delete_def():
    selected_index = listbox.curselection()  # Получаем индексы выбранных элементов
    if selected_index:
        listbox.delete(selected_index)  # Удаляем выбранные элементы из listbox


tk.Label(win, text=" ", font=('Arial', 5)).grid(row=0, column=0)
tk.Label(win, text="Daily Tasks", font=('Arial', 22)).grid(row=1, column=0, pady=20)

conteyner = tk.Frame(win, bg='#DCDCDC', width=520, height=220)
conteyner.grid(row=2, column=0, sticky="ns", pady=15)

add_todo = EntryWithPlaceholder(conteyner, ' Add todo', font=('Arial', 10))
add_todo.grid(row=0, column=0, sticky="we", padx=5, pady=5)

listbox = tk.Listbox(conteyner, width=85, height=10, border='1', bg="white", xscrollcommand='vertical')
listbox.grid(row=1, column=0, padx=5)
#listbox.configure(state=tk.DISABLED)


scrollbar = tk.Scrollbar(conteyner, orient="vertical", command=listbox.yview)
scrollbar.grid(row=0, rowspan=2, column=1, sticky='ns', ipady=5)

add = ctk.CTkButton(win, text="Add", corner_radius=5, bg_color="white", width=500, command=add_def)
add.grid(row=4, column=0, padx=0, pady=5)

edit = ctk.CTkButton(win, text="Edit", corner_radius=5, bg_color="white", width=500, command=edit_def)
edit.grid(row=5, column=0, padx=0, pady=5)

delete = ctk.CTkButton(win, text="Delete", corner_radius=5, bg_color="white", width=500, command=delete_def)
delete.grid(row=6, column=0, padx=0, pady=5)

win.columnconfigure(0, weight=100)
win.columnconfigure(1, weight=1)

win.mainloop()