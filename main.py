from tkinter import * 
import wonderwords
import random
import time

sentence = wonderwords.RandomSentence()

start_time = 0
finish_time = 0
input_text = ""
text_box2 = ""

window = Tk()
window.title("Typing Test Speed")
window.config(background="#2b2b2b")
window.geometry("450x400")
label1 = Label(text="Typing Test Speed", font=("Montserat", 20, "bold"), fg="black",padx=102, bg="#2b2b2b")
label1.pack(expand=True)

sentences_list = []
sentences = ""
size = 0
for n in range(0,5):
    sent = sentence.sentence()
    sentences_list.append(sent)
    sentences += sent
    size += len(sentences_list[n])

    
        
text_box = Text(window,height=9,width=30,)
text_box.pack(expand=True)
text_box.insert('end', sentences)
text_box.config(state="disabled")

def start():
    global start_time, input_text,text_box2

    start_time = time.time()
    text_box2 = Text(window,height=9,width=30,)
    text_box2.pack(expand=True)
    btn1.destroy()
    label1["text"] = "Faaaaast!"
    input_text = text_box2.get('1.0', 'end-1c')


def finisht(e):
    global finish_time, size, input_text, start_time
    input_text = text_box2.get('1.0', 'end-1c')
    finish_time = time.time()
    end =  finish_time - start_time 
    error = 0
    n = 0
    for letter in sentences:
        try:
            if letter == input_text[n]:
                pass
            else:
                error += 1
        except:
            error += 1
        n += 1
    porcentagem = 100 - (error/size)*100
    window.quit()
    palavras = len(sentences.split(" "))
    p_segundo = palavras/end

    print(f"Your typing speed was: {p_segundo:.2f} words/s. You got {porcentagem:.2f}% right")





    

btn1 =Button(window,text='Start!', command=start, pady=30,height=0,width=10)
btn1.pack(expand=True)
window.bind('<Up>', finisht)




window.mainloop()