import tkinter as tk
from tkinter import messagebox
from emi_calculator import EMICalculator


class LoanEMIApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Loan EMI Calculator")
        self.root.geometry("500x500")
        self.root.configure(bg="#f5f5f5")

        heading = tk.Label(
            root,
            text="Loan EMI Calculator",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5"
        )
        heading.pack(pady=20)

        tk.Label(
            root,
            text="Loan Amount (₹)",
            bg="#f5f5f5"
        ).pack()

        self.principal = tk.Entry(root, width=30)
        self.principal.pack(pady=5)

        tk.Label(
            root,
            text="Interest Rate (%)",
            bg="#f5f5f5"
        ).pack()

        self.rate = tk.Entry(root, width=30)
        self.rate.pack(pady=5)

        tk.Label(
            root,
            text="Loan Tenure (Months)",
            bg="#f5f5f5"
        ).pack()

        self.months = tk.Entry(root, width=30)
        self.months.pack(pady=5)

        tk.Button(
            root,
            text="Calculate EMI",
            command=self.calculate,
            bg="green",
            fg="white"
        ).pack(pady=15)

        tk.Button(
            root,
            text="Clear",
            command=self.clear,
            bg="red",
            fg="white"
        ).pack()

        self.result = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f5f5f5"
        )
        self.result.pack(pady=20)

    def calculate(self):
        try:
            principal = float(self.principal.get())
            rate = float(self.rate.get())
            months = int(self.months.get())

            emi_obj = EMICalculator(
                principal,
                rate,
                months
            )

            emi = emi_obj.calculate_emi()

            self.result.config(
                text=f"Monthly EMI: ₹ {emi}"
            )

        except:
            messagebox.showerror(
                "Error",
                "Please enter valid values."
            )

    def clear(self):
        self.principal.delete(0, tk.END)
        self.rate.delete(0, tk.END)
        self.months.delete(0, tk.END)
        self.result.config(text="")


root = tk.Tk()
app = LoanEMIApp(root)
root.mainloop()