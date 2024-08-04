import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import pickle


def predict():
    try:
        exp = float(ent_exp.get())
        with open('sal.pkl', 'rb') as file:
            model = pickle.load(file)
        sal = model.predict([[exp]])
        msg = "Salary = " + str(round(sal[0], 2)) + "K"
        showinfo("Message", msg)
    except ValueError:
        showerror("Error", "Please enter a valid number for experience")
        ent_exp.delete(0, tk.END)
        ent_exp.focus()
    except FileNotFoundError:
        showerror("Error", "'sal.pkl' file not found. Please make sure the file exists.")

root = tk.Tk()
root.title("Salary Predictor ")

f = ("Century", 30, "bold")

lab_title = tk.Label(root, text="Salary Predictor", font=f)
lab_exp = tk.Label(root, text="Enter experience", font=f)
ent_exp = tk.Entry(root, font=f)
btn_predict = tk.Button(root, text="Predict Salary", font=f, command=predict)

lab_title.pack(pady=5)
lab_exp.pack(pady=5)
ent_exp.pack(pady=5)
btn_predict.pack(pady=5)

root.mainloop()

