import pyttsx3
import PyPDF2


# book = open('resume.pdf' , 'rb')
# reader = PyPDF2.PdfReader(book)
# length = len(reader.pages)
# print(length)
# for id in range(0,length):
#     page = reader.pages[id]
#     Text = page.extract_text()
#     print(Text)



Text = " System Calls Remember Britney in the previous lesson? Let's say we want to see her and get some drinks together, how do we get from standing outside in the crowds of people to inside her innermost circle? We would use system calls. System calls are like the VIP passes that get you to a secret side door that leads directly to Britney.System calls (syscall) provide user space processes a way to request the kernel to do something for us. The kernel makes certain services available through the system call API. These services allow us to read or write to a file, modify memory usage, modify our network, etc. The amount of services are fixed, so you can't be adding system calls nilly willy, your system already has a table of what system calls exist and each system call has a unique ID"
speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
speaker.setProperty("voice",voices[1].id)
speaker.setProperty("rate",150)
speaker.setProperty('pitch', 1) 
speaker.save_to_file(Text,"output2.mp3")
# speaker.say(Text)
speaker.runAndWait()
print('done')
speaker.stop()
