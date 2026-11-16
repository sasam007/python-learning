import tkinter as tk

KM_TO_MILES = 0.621371


def calculate():
    try:
        km = float(km_entry.get())
    except ValueError:
        result_label["text"] = "?"
        return
    result_label["text"] = f"{km * KM_TO_MILES:.2f}"


window = tk.Tk()
window.title("Kilometer to Mile Converter")
window.config(padx=20, pady=20)

km_entry = tk.Entry(width=10)
km_entry.insert(0, "0")
km_entry.grid(row=0, column=1)

tk.Label(text="km").grid(row=0, column=2)
tk.Label(text="is equal to").grid(row=1, column=0)

result_label = tk.Label(text="0")
result_label.grid(row=1, column=1)

tk.Label(text="Miles").grid(row=1, column=2)

tk.Button(text="Calculate", command=calculate).grid(row=2, column=1)

window.mainloop()
