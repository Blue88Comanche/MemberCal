print 'Form Finder V1'
#
import os
#
#This program is used to pull up forms for the gym
#
print 'What Form are you looking for?'
print '1 = Tanning Agreement'
print '2 = Key Usage'
print '3 = Equipment and Facility'
print '4 = Guest Regeister'
print '5 = Guest Pass'
print '6 = Cancelation Form'
form = input()
if form is 1:
    os.startfile("forms\TANNING AGREEMENT.docx")
if form is 2:
    os.startfile("forms\Important Notice Regarding Key Usage.doc")
if form is 3:
    os.startfile("forms\AF Equipment and Facilities Policies.pdf")
if form is 4:
    os.startfile("forms\Guest_Register.pdf")
if form is 5:
    os.startfile("forms\Guest Pass.docx")
if form is 6:
    os.startfile("forms\Cancelation document.docx")
