
import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Lista donde almacenaremos las tareas
        self.tareas = []

        # Campo de entrada
        self.entry_tarea = tk.Entry(self.root, width=35)
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea)  # CORREGIDO: <Return>

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack()

        btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=0, padx=5)

        btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista para mostrar tareas
        self.listbox_tareas = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox_tareas.pack(pady=10)
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada)  # Doble clic = Completar

    def agregar_tarea(self, event=None):
        """Añade una tarea a la lista y la muestra en el listbox."""
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea antes de añadir.")

    def marcar_completada(self, event=None):
        """Marca la tarea seleccionada como completada (visual = con ✔)."""
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]  # CORREGIDO
            self.actualizar_lista()
        else:
            messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para marcarla.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para eliminar.")

    def actualizar_lista(self):
        """Actualiza el contenido visual del listbox."""
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = f"✔ {texto}"  # Añadir un check para indicar completada
            self.listbox_tareas.insert(tk.END, texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()

