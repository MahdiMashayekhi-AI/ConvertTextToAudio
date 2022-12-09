'''
Created by Mahdi Mashayekhi
Email : MahdiMashayekhi.ai@gmail.com
Github : https://github.com/MahdiMashayekhi-AI
Site : http://mahdimashayekhi.gigfa.com
YouTube : https://youtube.com/@MahdiMashayekhi
Twitter : https://twitter.com/Mashayekhi_AI
LinkedIn : https://www.linkedin.com/in/mahdimashayekhi/

'''
# install library: pip install pyttsx3
# import library
import pyttsx3

main = pyttsx3.init()  # initialized

text = "Hello. I am Mahdi Mashayekhi and welcome. I love programming! What about you?"
main.say(text)
main.runAndWait()
main.save_to_file('Mahdi Mashayekhi', 'Mahdi Mashayekhi')
