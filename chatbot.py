from tkinter import *

root = Tk()

def send():
    user_input = e.get()
    text.insert(END, "\nYou: " + user_input)

    if user_input.lower() in ['hi', 'hello', 'hey']:
        text.insert(END, "\nMARVREEN: Hello!")

    elif user_input.lower() in ['how are you?','how are you','how is you', 'how are you doing?']:
        text.insert(END, "\nMARVREEN: I'm fine, thank you. How about you?")

    elif user_input.lower() in ['good', 'fine', "i'm fine", "i'm good"]:
        text.insert(END, "\nMARVREEN: That's great to hear!")

    elif user_input.lower() in ['thank you', 'thanks']:
        text.insert(END, "\nMARVREEN: You're welcome!")

    elif user_input.lower() in ['bye', 'goodbye', 'see you later']:
        text.insert(END, "\nMARVREEN: Goodbye! Have a great day!")

    elif '?' in user_input:
        text.insert(END, "\nMARVREEN: I'm sorry, I don't have the answer to that question at the moment.")

    else:
        text.insert(END, "\nMARVREEN: Sorry, I didn't understand that.")

    # Clear the entry widget
    e.delete(0, END)

text = Text(root, bg='grey', fg='white')
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

send_button = Button(root, text='Send', bg='brown', fg='white', width=20, command=send)
send_button.grid(row=1, column=1)

root.title('MARVREEN CHATBOT')
root.mainloop()
