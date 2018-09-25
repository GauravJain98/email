import sendgrid
import os
from sendgrid.helpers.mail import *

final = {
'SodiCates': 'sanjuk.gbpec@gmail.com', 'Int Elligence': 'khuranasara18@gmail.com', 'BugBusters': 'dhruvbhatnagar10@ieee.org', 'Anonymous': 'Birladeepasha99@gmail.com', 'HackedOnce': 'aashita.arora.2365@gmail.com', 'noobs': 'amaanabbasi99@gmail.com', 'Bellatrix': 'dilsheenkaur98@gmail.com', 'ARIA': 'anant99garg@gmail.com', 'Super Hackers': 'abhishek.shrm.2195@gmail.com', 'supercalifragilisticexpialidocious hackers': 'sakshisrivastava413@gmail.com', 'Marshal Coders': 'meghagupta307@gmail.com', 'InstillCoders': 'aayushtiwari8@gmail.com', '9TH BIT': 'charugoyal180@gmail.com', 'Arjuna': 'harshitaj270@gmail.com', 'harrypotter0': 'cool_akashkandpal@rediffmail.com', 'Dobie': 'damakbajaj98@gmail.com', 'Titans': 'souravmunjal2000@gmail.com', 'Pseudo101': 'ishaanofficial28@gmail.com', 'AA Battery': 'ayushyadav97@gmail.com', 'code in blood': 'harshkashyap307@gmail.com', 'Vandals': 'shivamkalra2017@gmail.com', 'The Brogrammers': 'sarthak0120@gmail.com', 'LHash': 'developer@shikharagnihotri.com', 'Liquid': 'nachiketa.raina98@gmail.com', 'Ninja coders': 'svaish.stp@gmail.com', 'Hash it Out': 'sunnyashish01@gmail.com', 'fortnite': 'icode365@gmail.com', 'NoOne': 'ssshailesh3@gmail.com', 'Lunatic hackers': 'munishgrover98@gmail.com', 'Infinite Loop': 'yk.smb.kkr@gmail.com', 'Reverlash': 'jabhi678@gmail.com', 'Caffeine Cachers': 'jainvatsal1137@gmail.com', 'Fruitchill': 'rathi27ritik@gmail.com', 'Droid_Brothers': 'vashisht.s21295@gmail.com'
}


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("hackatbvp@gmail.com")
for i in final:
	to_email = Email(final[i])
	subject = "Congratulations"
	content = Content("html/css", "<p dir=ltr id=gmail-docs-internal-guid-8fb15a38-7fff-de55-50ff-de2a8e76989c>Hi "+ i +" ,<p dir=ltr>Congrats! Your team has been shortlisted for a 24-hour hackathon “HACK@BVP 2.0” organized by Computer Science Department , Bharati Vidyapeeth’s College of Engineering in collaboration with TASTE = 360 (Title Sponsor) , Coding Blocks (Education Partner) , Monktree (Cloud Partner), SMARTEDGE (Knowledge and Mentoring Partner) and INCUSPAZE (Incubation Partner). HACK@BVP 2.0 is designed to bring developers, technology leaders, and innovators together to explore and discuss new ideas for tools, services, and apps designed to improve value, affordability, and outcomes on the Themes mentioned in our website <a href=http://www.hackbvp.com>www.hackbvp.com</a> .<p dir=ltr>Points to remember:-<ul><li dir=ltr><p dir=ltr>Please bring your college ID-card.<li di ir=ltr><p dir=ltr>You will get your scheduled meals free of cost but apart from that, you can have your own from food stalls in college premises (Day/Night).<li dir=ltr><p dir=ltr>To reboot your brain, we would encourage everyone to take a break every now and then. Arrangements have been made for the same.(Separate for boys/girls).<li dir=ltr><p dir=ltr>College WIFI would be provided to all participants throughout the hackathon but it is advisable to bring your own internet connection and also the extension board.</ul><p dir=ltr>Please join us on [28/09/2018] at 8:00 AM sharp in Library, Bharati Vidyapeeth’s College of Engineering, Paschim Vihar, New Delhi-110063.<p dir=ltr>RSVP to <a href=https://goo.gl/forms/oKqIW8nB8qL69mdH2>https://goo.gl/forms/oKqIW8nB8qL69mdH2 </a>within 3 days if your team would like to attend, otherwise, your invitation will be canceled. This invitation is for the whole team and not a member and is non-transferrable.<p dir=ltr>Sincerely,<p dir=ltr>Hackathon Team")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
