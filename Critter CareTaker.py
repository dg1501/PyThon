import tkinter as tk
from tkinter import messagebox, font

class Critter:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0

    def __str__(self):
        return f"Tên: {self.name} | đói: {self.hunger} | Chán: {self.boredom}"

    def feed(self):
        self.hunger = max(0, self.hunger - 1)

    def play(self):
        self.hunger += 2
        self.boredom = max(0, self.boredom - 1)

    def sleep(self):
        self.hunger += 1
        self.boredom += 1

    def get_mood(self):
        if self.hunger > 5 or self.boredom > 5:
            return "Kiệt sức 😩"
        elif self.hunger > self.boredom:
            return "Mệt mỏi 🥱"
        elif self.boredom > self.hunger:
            return "Tức giận 😠"
        else:
            return "Vui vẻ 😀"

class CritterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRITTER CARETAKER")
        self.root.geometry("460x360")
        self.root.configure(bg="#f0f0f0")

        self.critters = []
        self.current_index = None

        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.label_font = font.Font(family="Arial", size=12)
        self.status_font = font.Font(family="Courier New", size=14, weight="bold")
        self.mood_font = font.Font(family="Arial", size=16, slant="italic", weight="bold")

        tk.Label(root, text="CRITTER CARETAKER", font=self.title_font, bg="#f0f0f0", fg="#333").pack(pady=(15, 10))

        frame_top = tk.Frame(root, bg="#f0f0f0")
        frame_top.pack(pady=(0, 10))

        tk.Label(frame_top, text="Critter's name:", font=self.label_font, bg="#f0f0f0").pack(side='left', padx=(0, 8))

        self.entry = tk.Entry(frame_top, font=self.label_font, width=22)
        self.entry.pack(side='left')

        tk.Button(frame_top, text="Create", command=self.create_critter, width=8, bg="#c9af1d", fg="white", font=self.label_font).pack(side='left', padx=10)

        self.critter_listbox = tk.Listbox(root, font=self.label_font, height=4)
        self.critter_listbox.pack(pady=(0, 10))
        self.critter_listbox.bind('<<ListboxSelect>>', self.select_critter)

        frame_buttons = tk.Frame(root, bg="#f0f0f0")
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Feed", command=self.feed_critter, width=12, bg="#d8171e", fg="white", font=self.label_font).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame_buttons, text="Play", command=self.play_with_critter, width=12, bg="#9ed719", fg="white", font=self.label_font).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame_buttons, text="Sleep", command=self.sleep_critter, width=12, bg="#9e27b0", fg="white", font=self.label_font).grid(row=0, column=2, padx=10, pady=5)

        frame_status = tk.Frame(root, bg="#ffffff", padx=20, pady=15, relief='groove', bd=2)
        frame_status.pack(fill='both', expand=True, padx=20, pady=15)

        self.status_label = tk.Label(frame_status, text="Don't have Critter", font=self.status_font, bg="#ffffff", fg="#3B853E")
        self.status_label.pack(pady=(0,10))

        self.mood_label = tk.Label(frame_status, text="", font=self.mood_font, bg="#ffffff", fg="#d32f2f")
        self.mood_label.pack()

    def create_critter(self):
        name = self.entry.get().strip()
        if name:
            new_critter = Critter(name)
            self.critters.append(new_critter)
            self.critter_listbox.insert(tk.END, name)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập tên cho Critter.")

    def select_critter(self, event):
        selection = self.critter_listbox.curselection()
        if selection:
            self.current_index = selection[0]
            self.display_status()

    def feed_critter(self):
        if self.current_index is not None:
            self.critters[self.current_index].feed()
            self.display_status()
        else:
            messagebox.showwarning("Lỗi", "Hãy chọn một Critter!")

    def play_with_critter(self):
        if self.current_index is not None:
            self.critters[self.current_index].play()
            self.display_status()
        else:
            messagebox.showwarning("Lỗi", "Hãy chọn một Critter!")

    def sleep_critter(self):
        if self.current_index is not None:
            self.critters[self.current_index].sleep()
            self.display_status()
        else:
            messagebox.showwarning("Lỗi", "Hãy chọn một Critter!")

    def display_status(self):
        if self.current_index is not None:
            critter = self.critters[self.current_index]
            self.status_label.config(text=str(critter))
            self.mood_label.config(text=f"Tâm trạng: {critter.get_mood()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CritterApp(root)
    root.mainloop()
