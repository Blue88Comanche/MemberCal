#this program is not for resale
#Membership Calculator written By Jeffrey Enfinger
print "membership Calculator v2.1.1"
######
#dont change anything in the date field!!
######
#Date Field
######
from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
date = str(current_month) + '/' + str(current_day) + '/' + str(current_year)
next_month = current_month + 1
next_year = current_year
if next_month >= 13:
    next_month = next_month - 12
    next_year = next_year +1
start_billing = str(next_month) + '/' + str(current_day) + '/' + str(next_year)
#######
import os
#Membership Info
#Edit this to change membership rates
#######
single_per = 35
extra_per = 20
startup_1 = 15
startup_extra = 5
tanning = 0
anytime_health = 0
#######
#Discount Field
#Dont change this field
#######
#zero Start up
zero_start = startup_1 - startup_1
zero_start_extra = startup_extra - startup_extra
#10% off monthly
ten_off = single_per * .9
ten_off_extra = extra_per * .9
#City of mobile
city_start = startup_1 * .5
city_per = single_per * .9
#Mobile County
county_start = startup_1 * .5
county_per = single_per * .9
#State of Alabama
state_start = startup_1 * .5
state_per = single_per * .9
#School Teachers
teacher_start = startup_1 * .5
teacher_per = single_per * .9
#AMR (American Medical Responce)
amr_start = startup_1 * .5
amr_per = single_per * .9
#Walmart or Sams Club
wal_or_sam_start = startup_1 * .5
wal_or_sam_per = single_per * .9
wal_or_sam_tan = tanning * .9
#Target Corporation
target_start = startup_1 * .5
target_per = single_per * .9
target_tan = tanning * .9
#Walgreens
walgreens_start = startup_1 * .5
walgreens_per = single_per * .9
#Inner Strength Martial Arts
inner_strength_per = single_per * .9
#ClearWater Christian Church
clearwater_per = single_per * .9
#Military
mil_per = single_per * .9
mil_extra = extra_per * .9
mil_start = startup_1 * .5
mil_extra_start = startup_extra * .5
#silver sneakers
silver = single_per * 0
silver_start = startup_1 * 0
#Home Depot
home_depot_per = single_per * .9
home_depot_start = startup_1 * .5
#Pepsi
pepsi_per = single_per * .9
pepsi_start = startup_1 * .5

##Start of Program## Dont change anything past this point
print "How long is the membership (In months, up to 12 months)"
months = input ()
print "Is this a single membership or family? 1 = Single / 2 = Family"
memberanswer = input ()
if memberanswer is 1:
    print 'Does this member get a discount? 1 = yes / 2 = no'
    discount_ans = input ()
    if discount_ans is 1:
        print 'What company does the member work for?'
        print '0 = City of Mobile'
        print '1 = Mobile County'
        print '2 = State of Alabama'
        print '3 = School Teacher'
        print '4 = AMR'
        print '5 = Walmart or Sam\'s Club'
        print '6 = Target Corporation'
        print '7 = Walgreens'
        print '8 = Inner Strength Martial Arts'
        print '9 = Clearwater Christian Church'
        print '10 =  Military'
        print '11 = Silver Sneakers'
        print '12 = Home Depot'
        print '13 = Pepsi'
        print
        print '30 = Zero Startup fee Special'
        print '31 = 10 percent off monthly'
        print
        print '32 = Not listed'
        discount_plan = input ()
    #Silver Sneakers
        if discount_plan is 11:
            print "Silver Sneakers Discount Plan"
            print
            print 'Silver Sneakers member do not pay'
            print 'anything for their membership'
            print
            print 'All that is required is that they fill'
            print 'out all the paper work, and we get a copy'
            print 'of their drivers license and their Silver'
            print 'sneakers card.'
    #no discount found
        if discount_plan is 32:
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1 
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #Zero Start
        if discount_plan is 30:
            startup_1 = zero_start
            startup_extra = zero_start_extra
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1 
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #10 PERCENT OFF
        if discount_plan is 31:
            single_contract_fee = ten_off * months + startup_1
            single_contract = ten_off * months
            down_pay = ten_off + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (ten_off)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1 
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #City of Mobile
        if discount_plan is 0:
            print "City of Mobile discount plan"
            print
            single_per = city_per
            startup_1 = city_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)    
    #Mobile County		
        if discount_plan is 1:
            print 'Mobile County discount plam'
            print
            single_per = county_per
            startup_1 = county_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)    
    #State of Alabama		
        if discount_plan is 2:
            print 'State of Alabama discount plan'
            single_per = state_per
            startup_1 = state_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #School Teacher        
        if discount_plan is 3:
            print 'Teacher discount plan'
            single_per = teacher_per
            startup_1 = teacher_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #AMR (American Medical Responce)       
        if discount_plan is 4:
            print 'AMR discount plan'
            single_per = amr_per
            startup_1 = amr_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #Walmart or Sam's Club       
        if discount_plan is 5:
            print 'Walmart or Sam\'s Club discount plan'
            single_per = wal_or_sam_per
            startup_1 = wal_or_sam_start
            tanning = wal_or_sam_tan
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Walmart Flyer.pdf")
    #Target Corp       
        if discount_plan is 6:
            print 'Target Corporation discount plan'
            single_per = target_per
            startup_1 = target_start
            tanning = target_tan
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Target.pdf")
    #Walgreens       
        if discount_plan is 7:
            print 'Walgreens discount plan'
            single_per = walgreens_per
            startup_1 = walgreens_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Walgreens.pdf")
    #Inner Strength Martial Arts       
        if discount_plan is 8:
            print 'Inner strength Martial Arts discount plan'
            single_per = inner_strength_per
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay 
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #Clearwater Christian Church        
        if discount_plan is 9:
            print 'Clearwater Christian Church discount plan'
            single_per = clearwater_per
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #Military
        if discount_plan is 10:
            print "Military discount plan"
            print
            single_per = mil_per
            startup_1 = mil_start
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            #Home Depot       
        if discount_plan is 12:
            print 'Home Depot discount plan'
            single_per = home_depot_per
            startup_1 = home_depot_start
            tanning = wal_or_sam_tan
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Home Depot.pdf")
            #pepsi       
        if discount_plan is 13:
            print 'Pepsi discount plan'
            single_per = pepsi_per
            startup_1 = pepsi_start
            tanning = wal_or_sam_tan
            single_contract_fee = single_per * months + startup_1
            single_contract = single_per * months
            down_pay = single_per + startup_1
            bal = single_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (single_per)
            print "plus a %s dollar start up fee" % (startup_1)
            print "Total year Membership cost %s dollars" % (single_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (single_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (startup_1)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (single_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    if discount_ans is 2:
        single_contract_fee = single_per * months + startup_1
        single_contract = single_per * months
        down_pay = single_per + startup_1
        bal = single_contract_fee - down_pay
        fu_month =  current_month + months
        if fu_month < 12:
            date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
        if fu_month > 12:
            new_month = fu_month - 12
            fu_year = current_year + 1
            date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
        print "Does this membership get discount? 1 = yes / 2 = no"
        print
        print "Single membership rate is %s dollars per month" % (single_per)
        print "plus a %s dollar start up fee" % (startup_1)
        print "Total year Membership cost %s dollars" % (single_contract_fee)
        print
        print
    	#Contract fillout cheat sheet
        print "Contract Cheat sheet"
        print
        print "start membership"
        print date
        print "end membership"
        print date_end
        print
        print "Membership --------- %s" % (single_contract)
        print "Tanning ------------ %s" % (tanning)
        print "Processing Fee ----- %s" % (startup_1)
        print "Anytime Health ----- %s" % (anytime_health)
        print "Total -------------- %s" % (single_contract_fee)
        print "Downpaymnt --------- %s" % (down_pay)
        print "Remaining Balance -- %s" % (bal)
        print
        months_bal = months - 1
        print "Payment Plan (membership dues): %s Dollars Per month" % (single_per)
        print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
if memberanswer is 2:
    print 'How many secondary members?'
    secondary = input ()
    membership_per = secondary * extra_per + single_per
    print 'does this member get a discount? 1 = yes / 2 = no'
    discount_ans = input ()
    if discount_ans is 1:
        print 'What company does the member work for?'
        print '0 = City of Mobile'
        print '1 = Mobile County'
        print '2 = State of Alabama'
        print '3 = School Teacher'
        print '4 = AMR'
        print '5 = Walmart or Sam\'s Club'
        print '6 = Target Corporation'
        print '7 = Walgreens'
        print '8 = Inner Strength Martial Arts'
        print '9 = Clearwater Christian Church'
        print '10 = Military'
        print '11 = Silver Sneakers'
        print '12 = Home Depot'
        print '13 = Pepsi'
        print
        print '30 = Zero Startup fee Special'
        print '31 = 10 percent off monthly'
        print
        print '32 = Not listed'
        discount_plan = input ()
    #Silver Sneakers
        if discount_plan is 11:
            print "Silver Sneakers Discount Plan"
            print
            print 'Silver Sneakers member do not pay'
            print 'anything for their membership'
            print
            print 'All that is required is that they fill'
            print 'out all the paper work, and we get a copy'
            print 'of their drivers license and their Silver'
            print 'sneakers card.'
            print
            print "However they can not have paying secondary"
            print 'members.  If the secondary members want to'
            print 'join then they will need to be on their own'
            print 'membership'
    #Zero Start
        if discount_plan is 30:
            multi_fee = secondary * zero_start_extra + zero_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #ten percent off
        if discount_plan is 31:
            membership_per = secondary * ten_off_extra + ten_off
            multi_fee = secondary * startup_extra + startup_1
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
        #no Discount found
        if discount_plan is 32:
            membership_per = secondary * extra_per + single_per
            multi_fee = secondary * startup_extra + startup_1
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Membership rate is %s per month" % (membership_per)
            print "plus a %s start up fee" % (multi_fee)
            print "Total Membership cost %s dollars with %s secondary member(s)" % (multi_contract_fee,secondary)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Fill-out Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #City of Mobile
        if discount_plan is 0:
            print "City of Mobile discount plan"
            print
            membership_per = secondary * extra_per + city_per
            multi_fee = secondary * startup_extra + city_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)    
    #Mobile County		
        if discount_plan is 1:
            print 'Mobile County discount plam'
            print
            membership_per = secondary * extra_per + county_per
            multi_fee = secondary * startup_extra + county_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #State of Alabama		
        if discount_plan is 2:
            print 'State of Alabama discount plan'
            membership_per = secondary * extra_per + state_per
            multi_fee = secondary * startup_extra + state_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #School Teacher        
        if discount_plan is 3:
            print 'Teacher discount plan'
            membership_per = secondary * extra_per + tracher_per
            multi_fee = secondary * startup_extra + teacher_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #AMR (American Medical Responce)       
        if discount_plan is 4:
            print 'AMR discount plan'
            membership_per = secondary * extra_per + amr_per
            multi_fee = secondary * startup_extra + amr_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #Walmart or Sam's Club       
        if discount_plan is 5:
            membership_per = secondary * extra_per + wal_or_sam_per
            multi_fee = secondary * startup_extra + wal_or_sam_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Walmart Flyer.pdf")
    #Target Corp       
        if discount_plan is 6:
            print 'Target Corporation discount plan'
            membership_per = secondary * extra_per + target_per
            multi_fee = secondary * startup_extra + target_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Target.pdf")
    #Walgreens       
        if discount_plan is 7:
            membership_per = secondary * extra_per + walgreens_per
            multi_fee = secondary * startup_extra + walgreens_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Walgreens.pdf")
    #Inner Strength Martial Arts       
        if discount_plan is 8:
            print 'Inner strength Martial Arts discount plan'
            membership_per = secondary * extra_per + inner_strength_per
            multi_fee = secondary * startup_extra + inner_strength_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)   
    #Clearwater Christian Church        
        if discount_plan is 9:
            print 'Clearwater Christian Church discount plan'
            membership_per = secondary * extra_per + clearwater_per
            multi_fee = secondary * startup_extra + clearwater_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #military
        if discount_plan is 10:
            print "Military discount plan"
            print
            membership_per = secondary * mil_extra + mil_per
            multi_fee = secondary * mil_extra_start + mil_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    #home depot       
        if discount_plan is 12:
            membership_per = secondary * extra_per + home_depot_per
            multi_fee = secondary * startup_extra + home_depot_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
            os.startfile("flyers\Home Depot.pdf")
    #pepsi       
        if discount_plan is 13:
            membership_per = secondary * extra_per + pepsi_per
            multi_fee = secondary * startup_extra + pepsi_start
            multi_contract_fee = membership_per * months + multi_fee
            multi_contract = membership_per * months
            down_pay = membership_per + multi_fee
            bal = multi_contract_fee - down_pay
            fu_month =  current_month + months
            if fu_month < 12:
                date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
            if fu_month > 12:
                new_month = fu_month - 12
                fu_year = current_year + 1
                date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
            print
            print "Single membership rate is %s dollars per month" % (membership_per)
            print "Total year Membership cost %s dollars" % (multi_contract_fee)
            print
            print
            #Contract fillout cheat sheet
            print "Contract Cheat sheet"
            print
            print "start membership"
            print date
            print "end membership"
            print date_end
            print
            print "Membership --------- %s" % (multi_contract)
            print "Tanning ------------ %s" % (tanning)
            print "Processing Fee ----- %s" % (multi_fee)
            print "Anytime Health ----- %s" % (anytime_health)
            print "Total -------------- %s" % (multi_contract_fee)
            print "Downpaymnt --------- %s" % (down_pay)
            print "Remaining Balance -- %s" % (bal)
            print
            months_bal = months - 1
            print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
            print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
    if discount_ans is 2:
        membership_per = secondary * extra_per + single_per
        multi_fee = secondary * startup_extra + startup_1
        multi_contract_fee = membership_per * months + multi_fee
        multi_contract = membership_per * months
        down_pay = membership_per + multi_fee
        bal = multi_contract_fee - down_pay
        fu_month =  current_month + months
        if fu_month < 12:
            date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
        if fu_month > 12:
            new_month = fu_month - 12
            fu_year = current_year + 1
            date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)
        print
        print "Membership rate is %s per month" % (membership_per)
        print "plus a %s start up fee" % (multi_fee)
        print "Total Membership cost %s dollars with %s secondary member(s)" % (multi_contract_fee,secondary)
        print
        print
        #Contract fillout cheat sheet
        print "Contract Fill-out Cheat sheet"
        print
        print "start membership"
        print date
        print "end membership"
        print date_end
        print
        print "Membership --------- %s" % (multi_contract)
        print "Tanning ------------ %s" % (tanning)
        print "Processing Fee ----- %s" % (multi_fee)
        print "Anytime Health ----- %s" % (anytime_health)
        print "Total -------------- %s" % (multi_contract_fee)
        print "Downpaymnt --------- %s" % (down_pay)
        print "Remaining Balance -- %s" % (bal)
        print
        months_bal = months - 1
        print "Payment Plan (membership dues): %s Dollars Per month" % (membership_per)
        print "For %s Consecutive Months beginning %s" % (months_bal,start_billing)
raw_input ("press enter to close window")
