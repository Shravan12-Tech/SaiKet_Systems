import customtkinter as ctk
from api_handler import get_joke

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window
app = ctk.CTk()
app.title("API Data Fetcher Dashboard")
app.geometry("900x600")

# Header
title = ctk.CTkLabel(
    app,
    text="🌐 API Data Fetcher Dashboard",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

# Description
desc = ctk.CTkLabel(
    app,
    text="Fetch live data from Public APIs",
    font=("Arial", 16)
)
desc.pack()

# Result Box
result_box = ctk.CTkTextbox(
    app,
    width=700,
    height=250,
    font=("Arial", 16)
)
result_box.pack(pady=30)

# Function
def fetch_data():
    joke = get_joke()

    result_box.delete("1.0", "end")
    result_box.insert("end", joke)

# Button
fetch_btn = ctk.CTkButton(
    app,
    text="Fetch Joke",
    command=fetch_data,
    width=220,
    height=50,
    font=("Arial", 18)
)

fetch_btn.pack()

# Footer
footer = ctk.CTkLabel(
    app,
    text="Python GUI Application using API",
    font=("Arial", 12)
)
footer.pack(side="bottom", pady=15)

app.mainloop()