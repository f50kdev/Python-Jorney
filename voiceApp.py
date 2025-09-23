from gtts import gTTS, lang, tts
import gtts;
import os  ;
import math ;

texto = "Welcome Faustino";
Information = " Hello sweet Girl , you sre so sexy"; 
English = "en";
portuguese = "en"
franch = "fr";

tts = gTTS(texto , lang=lingua );
sweet = gTTS(honey , lang=language);


tts.save("audio.mp3");
sweet.save("SweetGirls, i love u so much"); 

os.system('ffplay -autoexit -nodisp SweetGirls')

#soma de valor 
firstValue  =  2 ;
secondValue =  4 ;

total  = secondValue + firstValue ;
math.sqrt(total)

test = f"The some of two values s ,{total}";

voice = gTTS( test ,lang=lingua )
voice.save("soma.mp3");

os.system('ffplay -autoexit -nodisp soma.mp3');