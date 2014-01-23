print 'Form Finder V1.0.4'
#
import os
#
#This program is used to pull up forms for the gym
#
print 'What Form are you looking for?'
print '1 = Tanning Agreement'
print '2 = Key Usage'
print '3 = Equipment and Facility'
print '4 = Safty Notices'
print
print '5 = Guest Regeister'
print '6 = Guest Pass'
print
print '7 = Cancelation Form'
print '8 = Fax Cover Sheet'
print '9 = General cleaning check list'
print '10 = Deposit Receipt'
print '11 = Payment Envelopes Airport'
print '12 = Payment Envelopes Hillcrest'
print
print '15 = Contract'
print
print '20 = Everything for a new member'

form = input()
if form is 1:
    os.startfile("forms\TANNING AGREEMENT.pdf")
if form is 2:
    os.startfile("forms\Important Notice Regarding Key Usage.pdf")
if form is 3:
    os.startfile("forms\AF Equipment and Facilities Policies.pdf")
if form is 4:
    os.startfile("forms\SAFETY NOTICES.pdf")
if form is 5:
    os.startfile("forms\Guest_Register.pdf")
if form is 6:
    os.startfile("forms\Guest Pass.pdf")
if form is 7:
    os.startfile("forms\Cancelation document.pdf")
if form is 8:
    os.startfile("forms\Fax Cover Sheet.pdf")
if form is 9:
    os.startfile("forms\General cleaning check list.pdf")
if form is 10:
    os.startfile("forms\Deposit Receipt.pdf")
if form is 11:
    os.startfile("forms\Payment Envelopes Airport.pdf")
if form is 12:
    os.startfile("forms\Payment Envelopes Hillcrest.pdf")
if form is 15:
    os.startfile("forms\Contract.pdf")

if form is 20:
    os.startfile("forms\TANNING AGREEMENT.pdf")
    os.startfile("forms\Important Notice Regarding Key Usage.pdf")
    os.startfile("forms\AF Equipment and Facilities Policies.pdf")
    os.startfile("forms\SAFETY NOTICES.pdf")
    
