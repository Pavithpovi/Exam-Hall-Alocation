import tkinter as tk
import random

class ExamHallAllocator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exam Hall Allocation System")
        self.geometry("800x600")
        self.configure(bg="white")

        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.circles = []
        self.create_animation()

        self.form_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window(400, 150, window=self.form_frame)

        tk.Label(self.form_frame, text="Total Students:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.form_frame, text="Number of Halls:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.form_frame, text="Capacity per Hall:", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=5, pady=5)

        self.entry_students = tk.Entry(self.form_frame, font=("Arial", 12))
        self.entry_halls = tk.Entry(self.form_frame, font=("Arial", 12))
        self.entry_capacity = tk.Entry(self.form_frame, font=("Arial", 12))

        self.entry_students.grid(row=0, column=1, padx=5, pady=5)
        self.entry_halls.grid(row=1, column=1, padx=5, pady=5)
        self.entry_capacity.grid(row=2, column=1, padx=5, pady=5)

        self.allocate_btn = tk.Button(self.form_frame, text="Allocate", font=("Arial", 12), command=self.allocate)
        self.allocate_btn.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(self.canvas, height=15, width=80, font=("Courier", 10))
        self.canvas.create_window(400, 400, window=self.result_text)

        self.animate()

    def allocate(self):
        self.result_text.delete("1.0", tk.END)
        try:
            students = int(self.entry_students.get())
            halls = int(self.entry_halls.get())
            capacity = int(self.entry_capacity.get())

            if students > halls * capacity:
                self.result_text.insert(tk.END, "Error: Not enough hall capacity for all students.\n")
                return

            allocation = {}
            student_id = 1
            for hall_id in range(1, halls + 1):
                allocation[hall_id] = []
                for _ in range(capacity):
                    if student_id > students:
                        break
                    allocation[hall_id].append(student_id)
                    student_id += 1

            for hall, students_list in allocation.items():
                self.result_text.insert(tk.END, f"Hall {hall}: {students_list}\n")

        except ValueError:
            self.result_text.insert(tk.END, "Error: Please enter valid integers.\n")

    def create_animation(self):
        for _ in range(30):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            r = random.randint(10, 30)
            dx = random.choice([-1, 1]) * random.random()
            dy = random.choice([-1, 1]) * random.random()
            circle = {
                "id": self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(["#d1e8ff", "#a7d8ff", "#e0f7ff"]), outline=""),
                "x": x,
                "y": y,
                "r": r,
                "dx": dx,
                "dy": dy
            }
            self.circles.append(circle)

    def animate(self):
        for circle in self.circles:
            circle["x"] += circle["dx"]
            circle["y"] += circle["dy"]
            x = circle["x"]
            y = circle["y"]
            r = circle["r"]

            if x - r < 0 or x + r > 800:
                circle["dx"] *= -1
            if y - r < 0 or y + r > 600:
                circle["dy"] *= -1

            self.canvas.coords(circle["id"], x - r, y - r, x + r, y + r)

        self.after(30, self.animate)


if __name__ == "__main__":
    app = ExamHallAllocator()
    app.mainloop()
