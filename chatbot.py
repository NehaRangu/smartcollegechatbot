
import random

import webbrowser




def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)
print("Hello, I am GrietBOT....\n")
greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup","hii","hello","heyy")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you","heyy"]
continue_dialogue = True
while(continue_dialogue == True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
            print("BOT: Most welcome\nUSER:")
        else:
               if generate_greeting_response(human_text) != None:
                    print("BOT: " + generate_greeting_response(human_text))
                    print("BOT:Are you a parent (or) student (or) faculty?\nUSER:")
               if human_text=='student':
                                       print("BOT:These are the questions students usually ask:\n1.about griet?\n2.timetable?\n3.campus?\n4.student activities?\n5.Gallery\n\n\n But you can ask anything you want though!!!!\nUSER:")
               if human_text=='parent':
                                       print("BOT:These are the questions parents usually ask :\n1.about griet?\n2.hostel facilities\n3.placement details\n4.campus\n5.Gallery\n\n\n But you can ask anything you want though!!!!\nUSER:")
               if human_text=='faculty':
                                        print("BOT:These are the questions faculty usually ask:\n1.about griet?\n2.faculty information\n3.faculty circulars\n4.workshops\n5.schedules\n\n\n But you can ask anything you want though!!!!\nUSER:")
               if 'about griet' in human_text:
                             print("BOT:Damn!it wouldn't be nice if I say that over here,How then I'm afraid?\nGotcha!!!\nEnter yes!!\nUSER:")

               if  human_text=='yes': 
                             webbrowser.open('https://www.griet.ac.in/about.php', new=0) 
               if 'time table' in human_text:
                        print("BOT:OK!let me open it!\n Enter timetable\nUSER:")
               if  human_text=='time table':
                        webbrowser.open('https://www.griet.ac.in/tt.php', new=0)
               if 'campus' in human_text:
                        
                        print("you wanna see how it will be in Griet?\nEnter campus for it!\nUSER:")
                     
               if human_text=='campus':
                        webbrowser.open('https://www.youtube.com/watch?v=Gg0ATMD6zQw', new=0)
               if 'student activities' in human_text:
                   print("do you wanna go through the events at Griet:\nenter events\nUSER:")
               if human_text=='events':
                   webbrowser.open('https://www.youtube.com/watch?v=0CjBdl1P2K0',new=0)
               
               if human_text=='gallery':
                       webbrowser.open('https://in.images.search.yahoo.com/search/images;_ylt=AwrPoWOj_xJlidcU_Q67HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=gokaraju+rangaraju+college+of+engineering+images&fr2=piv-web&type=E210IN105G0&fr=mcafee', new=0)
               if 'facilities' in human_text:
                        print("BOT:hostel\nhealth care\nother aminities\nwhatdo you want to know the details?\nUSER:")
                       
               if human_text=='hostel':
                        webbrowser.open('https://www.kitsw.ac.in/Amenities/Hostels.html', new=0)
               if human_text=='health care':
                        webbrowser.open('https://www.careers360.com/colleges/gokaraju-rangaraju-institute-of-engineering-and-technology-hyderabad/facilities', new=0)
               if human_text=='other aminities':
                        webbrowser.open('https://www.careers360.com/colleges/gokaraju-rangaraju-institute-of-engineering-and-technology-hyderabad/facilities', new=0)
               if 'placement details' in human_text:
                        webbrowser.open('https://www.griet.ac.in/placements.php',new=0)
                        
                        
               if 'holidays' in human_text:
                        print("BOT:Lot of students ask this question!!!hahaha...\n")
                        print("BOT:You wanna see..\ntype holidays\nUSER:")
               if human_text=='holidays':
                        webbrowser.open('https://www.griet.ac.in/academic_calendar.php', new=0)
               if 'faculty information' in human_text:
                        print("BOT:Griet director is \nDo you want to know about it?\n enter fac!\nUSER:")
                        #flag=1
               if human_text=='fac':
                   print('enter any department:')
               if human_text=='CSE':

                   webbrowser.open('http://www.cse.griet.ac.in/',new=0)
               
               if human_text=='EEE':
                   webbrowser.open('http://www.eeedept.griet.ac.in/',new=0)
               if human_text=='ECE':
                   webbrowser.open('http://www.ece.griet.ac.in/',new=0)
               if human_text=='CSDS':
                   webbrowser.open('http://www.ds.griet.ac.in/',new=0)
               if human_text=='IT':
                   webbrowser.open('http://www.it.griet.ac.in/',new=0)
               if human_text=='AIML':
                   webbrowser.open('http://www.aiml.griet.ac.in/',new=0) 
               if human_text=='CSBS':
                   webbrowser.open('http://www.csbs.griet.ac.in/',new=0)
               if human_text=='ME':
                   webbrowser.open('http://www.me.griet.ac.in/',new=0)
               if human_text=='CE':
                   webbrowser.open('http://www.ce.griet.ac.in/',new=0)
             
              
               if 'faculty circulars' in human_text:
                        webbrowser.open('https://www.griet.ac.in/2023/GRIET%20Faculty%20Details-322.pdf',new=0)

               if 'workshops' in human_text:
                        webbrowser.open('https://www.griet.ac.in/fsf.php',new=0)

               if 'schedules' in human_text:
                        webbrowser.open('https://www.griet.ac.in/academic_calendar.php',new=0) 
               
                            
    if human_text== 'bye':
         continue_dialogue = False 
         print("BOT: Good bye and take care of yourself...")
    
    #responses part
def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)














