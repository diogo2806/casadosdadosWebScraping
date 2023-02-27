import tkinter as tk
import scraping

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Consulta CNPJ")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.cnj_label = tk.Label(self, text="Consulta CNPJ")
        self.cnj_label.pack()

        self.cnae_label = tk.Label(self, text="Atividade Principal (CNAE)")
        self.cnae_label.pack()
        self.cnae_entry = tk.Entry(self)
        self.cnae_entry.pack()

        self.natureza_label = tk.Label(self, text="Natureza Jurídica")
        self.natureza_label.pack()
        self.natureza_entry = tk.Entry(self)
        self.natureza_entry.pack()

        self.uf_label = tk.Label(self, text="Estado (UF)")
        self.uf_label.pack()
        self.uf_entry = tk.Entry(self)
        self.uf_entry.pack()

        self.search_button = tk.Button(self, text="Buscar", command=self.search_cnpj)
        self.search_button.pack()

    def search_cnpj(self):
        cnae = self.cnae_entry.get()
        natureza = self.natureza_entry.get()
        uf = self.uf_entry.get()

        scraping.scrape(cnae, natureza, uf)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
