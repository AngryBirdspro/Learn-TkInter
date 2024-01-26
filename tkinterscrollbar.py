from tkinter import *
r = Tk()

main_frame= Frame(r)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
canvas.pack(fill=BOTH, side = LEFT, expand=1)

scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

second_frame = Frame(canvas)

canvas.create_window((0,0), window=second_frame, anchor="nw")

for i in range(100):
    Button(second_frame, text = f'Button {i} Yo!').pack(pady=10, padx=10)
mainloop()