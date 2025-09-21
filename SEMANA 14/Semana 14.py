# Tarea: Creación de una Aplicación de Agenda Personal

import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime


class SimpleDatePicker:

    def __init__(self, parent, target_entry, year=None, month=None):
        self.parent = parent
        self.target_entry = target_entry
        now = datetime.now()
        self.year = year or now.year
        self.month = month or now.month
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.title('Seleccionar fecha')
        self.top.resizable(False, False)
        self.build()

    def build(self):
        header = ttk.Frame(self.top)
        header.pack(padx=6, pady=6)

        prev_btn = ttk.Button(header, text='<', width=3, command=self.prev_month)
        prev_btn.grid(row=0, column=0)
        self.lbl_month = ttk.Label(header, text=self._month_year_text(), width=18, anchor='center')
        self.lbl_month.grid(row=0, column=1, padx=6)
        next_btn = ttk.Button(header, text='>', width=3, command=self.next_month)
        next_btn.grid(row=0, column=2)

        cal_frame = ttk.Frame(self.top)
        cal_frame.pack(padx=6, pady=(0,6))

        days = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
        for c, d in enumerate(days):
            ttk.Label(cal_frame, text=d, width=4, anchor='center').grid(row=0, column=c)

        self.day_btns = []
        month_matrix = calendar.Calendar(firstweekday=0).monthdayscalendar(self.year, self.month)
        for r, week in enumerate(month_matrix, start=1):
            row_buttons = []
            for c, day in enumerate(week):
                if day == 0:
                    btn = ttk.Label(cal_frame, text='', width=4)
                    btn.grid(row=r, column=c, padx=1, pady=1)
                    row_buttons.append(btn)
                else:
                    btn = ttk.Button(cal_frame, text=str(day), width=4,
                                     command=lambda d=day: self.select_day(d))
                    btn.grid(row=r, column=c, padx=1, pady=1)
                    row_buttons.append(btn)
            self.day_btns.append(row_buttons)

    def _month_year_text(self):
        return f"{calendar.month_name[self.month]} {self.year}"

    def refresh_calendar(self):
        for w in self.top.winfo_children():
            w.destroy()
        self.build()

    def prev_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.lbl_month.config(text=self._month_year_text())
        self.refresh_calendar()

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.lbl_month.config(text=self._month_year_text())
        self.refresh_calendar()

    def select_day(self, day):
        try:
            dt = datetime(self.year, self.month, day)
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, dt.strftime('%Y-%m-%d'))
        finally:
            self.top.destroy()


class AgendaApp:
    def __init__(self, root):
        self.root = root
        root.title('Agenda Personal de Carlos Asencio')
        root.geometry('700x420')
        root.minsize(600, 380)

        self.frame_list = ttk.Frame(root, padding=8)
        self.frame_list.pack(fill='both', expand=True)

        self.frame_entry = ttk.Frame(root, padding=8)
        self.frame_entry.pack(fill='x')

        self.frame_actions = ttk.Frame(root, padding=8)
        self.frame_actions.pack(fill='x')

        self._build_list_frame()
        self._build_entry_frame()
        self._build_actions_frame()

        self.events = []

    def _build_list_frame(self):
        lbl = ttk.Label(self.frame_list, text='Eventos programados', font=('Segoe UI', 12, 'bold'))
        lbl.pack(anchor='w')

        columns = ('fecha', 'hora', 'descripcion')
        self.tree = ttk.Treeview(self.frame_list, columns=columns, show='headings', selectmode='browse')
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')
        self.tree.column('fecha', width=100, anchor='center')
        self.tree.column('hora', width=80, anchor='center')
        self.tree.column('descripcion', width=420, anchor='w')

        scrollbar = ttk.Scrollbar(self.frame_list, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

    def _build_entry_frame(self):
        lbl_date = ttk.Label(self.frame_entry, text='Fecha (YYYY-MM-DD):')
        lbl_date.grid(row=0, column=0, padx=4, pady=4, sticky='e')
        self.entry_date = ttk.Entry(self.frame_entry, width=14)
        self.entry_date.grid(row=0, column=1, padx=(0,4), pady=4, sticky='w')
        btn_date = ttk.Button(self.frame_entry, text='📅', width=3, command=self.open_datepicker)
        btn_date.grid(row=0, column=2, padx=(0,12), pady=4, sticky='w')

        lbl_time = ttk.Label(self.frame_entry, text='Hora (HH:MM):')
        lbl_time.grid(row=0, column=3, padx=4, pady=4, sticky='e')
        self.entry_time = ttk.Entry(self.frame_entry, width=8)
        self.entry_time.grid(row=0, column=4, padx=(0,12), pady=4, sticky='w')

        lbl_desc = ttk.Label(self.frame_entry, text='Descripción:')
        lbl_desc.grid(row=1, column=0, padx=4, pady=4, sticky='ne')
        self.entry_desc = ttk.Entry(self.frame_entry, width=60)
        self.entry_desc.grid(row=1, column=1, columnspan=4, padx=4, pady=4, sticky='w')

    def _build_actions_frame(self):
        btn_add = ttk.Button(self.frame_actions, text='Agregar Evento', command=self.add_event)
        btn_add.pack(side='left', padx=6, pady=6)

        btn_del = ttk.Button(self.frame_actions, text='Eliminar Evento Seleccionado', command=self.delete_selected)
        btn_del.pack(side='left', padx=6, pady=6)

        btn_exit = ttk.Button(self.frame_actions, text='Salir', command=self.root.quit)
        btn_exit.pack(side='right', padx=6, pady=6)

    def open_datepicker(self):
        SimpleDatePicker(self.root, self.entry_date)

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except Exception:
            return False

    def validate_time(self, time_text):
        try:
            datetime.strptime(time_text, '%H:%M')
            return True
        except Exception:
            return False

    def add_event(self):
        fecha = self.entry_date.get().strip()
        hora = self.entry_time.get().strip()
        desc = self.entry_desc.get().strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning('Campos incompletos', 'Por favor complete fecha, hora y descripción.')
            return
        if not self.validate_date(fecha):
            messagebox.showerror('Fecha inválida', 'La fecha debe tener el formato YYYY-MM-DD (ej. 2025-09-16).')
            return
        if not self.validate_time(hora):
            messagebox.showerror('Hora inválida', 'La hora debe tener el formato HH:MM en formato 24 horas (ej. 14:30).')
            return

        event = {'fecha': fecha, 'hora': hora, 'descripcion': desc}
        self.events.append(event)
        self._insert_into_tree(event)

        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def _insert_into_tree(self, event):
        self.tree.insert('', tk.END, values=(event['fecha'], event['hora'], event['descripcion']))

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo('Seleccionar evento', 'Por favor seleccione un evento para eliminar.')
            return
        item = sel[0]
        vals = self.tree.item(item, 'values')
        confirmed = messagebox.askyesno('Confirmar eliminación', f"¿Eliminar el evento:\n{vals[0]} {vals[1]} - {vals[2]}?")
        if not confirmed:
            return
        self.tree.delete(item)
        for i, e in enumerate(self.events):
            if (e['fecha'], e['hora'], e['descripcion']) == vals:
                del self.events[i]
                break


if __name__ == '__main__':
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
