import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Moonveil Calculator")
        self.root.geometry("420x560")
        self.root.resizable(False, False)

        self.expression = tk.StringVar()
        self.display = tk.Entry(
            root,
            textvariable=self.expression,
            font=("Segoe UI", 24),
            justify="right",
            bd=8,
            relief="sunken"
        )
        self.display.pack(fill="x", padx=12, pady=12, ipady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(expand=True, fill="both", padx=12, pady=8)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("(", 3, 2), (")", 3, 3),
            ("C", 4, 0), ("⌫", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for text, row, col in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Segoe UI", 16),
                command=lambda value=text: self.press(value)
            )
            btn.grid(
                row=row,
                column=col,
                padx=5,
                pady=5,
                sticky="nsew"
            )

        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)

        self.root.bind("<Return>", lambda _: self.calculate())
        self.root.bind("<Escape>", lambda _: self.clear())

    def press(self, value):
        if value == "=":
            self.calculate()
        elif value == "C":
            self.clear()
        elif value == "⌫":
            current = self.expression.get()
            self.expression.set(current[:-1])
        else:
            self.expression.set(self.expression.get() + value)

    def calculate(self):
        expression = self.expression.get().strip()

        if not expression:
            return

        try:
            # Restricted evaluation environment.
            result = eval(
                expression,
                {"__builtins__": {}},
                {}
            )

            self.expression.set(str(result))

        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
        except Exception:
            messagebox.showerror("Error", "Invalid expression.")

    def clear(self):
        self.expression.set("")


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()