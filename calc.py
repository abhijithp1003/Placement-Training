# import tkinter

# def cal_bmi():
#     h = float(ht_val.get())
#     w = float(wt_val.get())
#     h1 = h/100
#     bmi = w/(h1**2)
#     bmi = round(bmi, 2)
#     if bmi <18.5:
#         status = "Underweight"
#     elif bmi >=18.5 and bmi <24.5:
#         status = "Normal"
#     elif bmi >=24.5 and bmi <30:
#         status = "Overweight"
#     else:
#         status = "Obisity"
#     res.config(text=f"BMI IS {bmi:.2f} ({status})", bg="#4CAF50")

# root = tkinter.Tk()
# root.title("BMI Calculator")
# root.geometry("500x500")
# head = tkinter.Label(root, text="BMI CALCULATOR", font=("Arial", 20, "bold"), bg="#5E81AC")
# head.pack(pady=20)

# fr = tkinter.Frame(root, bg="#5E81AC")
# fr.pack(pady=10)


# ht = tkinter.Label(fr, text="HEIGHT (in cm)", font=("Arial", 15), bg="#5E81AC")
# ht.grid(row=0, column=0, padx=5, pady=5)
# ht_val = tkinter.Entry(fr)
# ht_val.grid(row=0, column=1, padx=5, pady=5)


# wt = tkinter.Label(fr, text="WEIGHT (in kg)", font=("Arial", 15), bg="#5E81AC")
# wt.grid(row=1, column=0, padx=5, pady=5)
# wt_val = tkinter.Entry(fr)
# wt_val.grid(row=1, column=1, padx=5, pady=5)


# bt = tkinter.Button(root, text="Calculate", font=("Arial", 20, "bold"), fg="white", bg="#5E81AC", command=cal_bmi)
# bt.pack(pady=20)


# res = tkinter.Label(root, text="", font=("Arial", 20, "bold"), bg="#ECEFF4")
# res.pack(pady=20)
# root.mainloop()

from collections import Counter

a = [2,3,4,5]
b= [2,3,10,11]

c=Counter(b)
for i in a&b:
    for j in range(c[11]):
        print("hai", end=" ")