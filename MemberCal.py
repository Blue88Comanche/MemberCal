#this program is not for resale
#Membership Calculator written By Jeffrey Enfinger
print "membership Calculator v3.0.1"
print
import os
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
while True:
	##########################################
	## Membership Info                      ##
	## Edit this to change membership rates ##
	##########################################
	# Primary member rate
	single_per = 35
	# Secondary member rate
	extra = 20
	# Primary start up fee
	startup_1 = 15
	# Secondary start up fee
	startup_extra = 5
	# Tanning rate # not used
	tanning = 0
	# Anytume Health fee # not used
	anytime_health = 0
	#######
	#Discount Field
	#Don't change this field
	#######
	#zero Start up
	zero_start = startup_1 - startup_1
	zero_start_extra = startup_extra - startup_extra
	#10% off monthly
	ten_off = single_per * .9
	ten_off_extra = extra * .9
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
	#Wal*mart or Sam's Club
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
	mil_extra = extra * .9
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
	#Student
	student = single_per * .9
	student_fee = startup_1 * .5
	#Coca-Cola
	coca_cola = single_per * .9
	coca_cola_fee = startup_1 * .5
	#Delta
	delta = single_per * .9
	#Kohl's
	kohls = single_per * .9
	kohls_start = startup_1 * .5
	#Unitedhealth Allies
	unitedhealth = single_per * .9
	unitedhealth_start = startup_1 * .5
	###############################################################
	## Start of Program ## Don't change anything past this point ##
	print "How long is the membership? (In months, up to 12)"
	term = input ()
	os.system('CLS')
	if term > 12.1:
		term = 12
	print 'How many members?'
	members = input()
	os.system('CLS')
	if members is 1:
		os.system('CLS')
		contract = single_per * term
		rate = single_per
		fee = startup_1
		total = single_per * term + startup_1
		down_pay = single_per + startup_1
		bal = total - down_pay
	else:
		os.system('CLS')
		#how many members
		members = members - 1
		#rate
		primary = single_per * term
		secondary = extra * members * term
		#startup fee
		extra_fee = startup_extra * members
		#total startup fees
		fee = startup_1 + extra_fee
		#total monthly with fee
		rate = extra * members + single_per
		#
		members = members + 1
		#sent to cheat sheet
		contract = primary + secondary
		fee = fee
		total = contract + fee
		down_pay = rate + fee
		bal = total - down_pay
	#date stuff
	fu_month =	current_month + term
	if fu_month <= 12:
		date_end = str(fu_month) + '/' + str(current_day) + '/' + str(current_year)
	if fu_month >= 13:
		new_month = fu_month - 12
		fu_year = current_year + 1
		date_end = str(new_month) + '/' + str(current_day) + '/' + str(fu_year)	
	##############
	## Read out ##
	print "Single membership rate is %s dollars per month" % (rate)
	print "plus a %s dollar start up fee" % (fee)
	print "Total year Membership cost %s dollars" % (total)
	print
	#Contract fillout cheat sheet
	print "Contract Cheat Sheet:"
	print
	print "start membership"
	print date
	print "end membership"
	print date_end
	print
	print "Membership --------- %s" % (contract)
	print "Tanning ------------ %s" % (tanning)
	print "Processing Fee ----- %s" % (fee)
	print "Anytime Health ----- %s" % (anytime_health)
	print "Total -------------- %s" % (total)
	print "Downpaymnt --------- %s" % (down_pay)
	print "Remaining Balance -- %s" % (bal)
	print
	term_bal = term - 1
	print "Payment Plan (membership dues): %s Dollars Per month" % (rate)
	print "For %s Consecutive term beginning %s" % (term_bal,start_billing)
	##############################
	## Apply Discount if listed ##
	print
	print 'Does this membership apply for a discount?'
	print '1 = yes / 2 = no'
	ans = input()
	os.system('CLS')
	if ans is 1:
		print 'What company does the member work for?'
		print '0 = City of Mobile'
		print '1 = Mobile County'
		print '2 = State of Alabama'
		print '3 = Mobile County Public School System'
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
		print '14 = Student'
		print '15 = Coca-Cola'
		print '16 = Delta'
		print '17 = Kohl\'s'
		print '18 = Unitedhealth Allies'
		print
		print '31 = 10% off'
		#print
		#print '32 = Anytime Fitness Special'
		print
		print '35 = Not listed'	
		discount_plan = input()	
		#########################
		##Discounts start here ##
		#City of Mobile
		if discount_plan is 0:
			single_per = city_per
			startup_1 = city_start
			os.startfile("flyers\City of Mobile.pdf")
		#Mobile County		
		if discount_plan is 1:
			single_per = county_per
			startup_1 = county_start
			os.startfile("flyers\Mobile County.pdf")
		#State of Alabama		
		if discount_plan is 2:
			single_per = state_per
			startup_1 = state_start
			os.startfile("flyers\State of Alabama.pdf")
		#School Teacher		   
		if discount_plan is 3:
			single_per = teacher_per
			startup_1 = teacher_start
			os.startfile("flyers\Mobile County Public School System.pdf")
		#AMR (American Medical Response)	   
		if discount_plan is 4:
			single_per = amr_per
			startup_1 = amr_start
			os.startfile("flyers\AMR.pdf")
		#Walmart or Sam's Club		 
		if discount_plan is 5:
			single_per = wal_or_sam_per
			startup_1 = wal_or_sam_start
			tanning = wal_or_sam_tan
			os.startfile("flyers\Walmart Flyer.pdf")
		#Target Corp	   
		if discount_plan is 6:
			single_per = target_per
			startup_1 = target_start
			tanning = target_tan
			os.startfile("flyers\Target.pdf")
		#Walgreens		 
		if discount_plan is 7:
			single_per = walgreens_per
			startup_1 = walgreens_start
			os.startfile("flyers\Walgreens.pdf")
		#Inner Strength Martial Arts	   
		if discount_plan is 8:
			single_per = inner_strength_per
			os.startfile("flyers\Inner Strength Martial Arts.pdf")
		#Clearwater Christian Church		
		if discount_plan is 9:
			single_per = clearwater_per
			os.startfile("flyers\Clearwater Christian Church.pdf")
		#military
		if discount_plan is 10:
			single_per = mil_per
			startup_1 = mil_start
			extra = mil_extra
			startup_extra = mil_extra_start
			os.startfile("flyers\Military.pdf")
		#Silver Sneakers
		if discount_plan is 11:
			single_per = silver
			startup_1 = silver_start
		#home depot		  
		if discount_plan is 12:
			single_per = home_depot_per
			startup_1 = home_depot_start
			os.startfile("flyers\Home Depot.pdf")			
		#pepsi		 
		if discount_plan is 13:
			single_per = pepsi_per
			startup_1 = pepsi_start
			os.startfile("flyers\Pepsi.pdf")
		#Student	 
		if discount_plan is 14:
			single_per = student
			startup_1 = student_fee
		#coca-cola		 
		if discount_plan is 15:
			single_per = coca_cola
			startup_1 = coca_cola_fee
		#Delta
		if discount_plan is 16:
			single_per = delta
		#Kohl's
		if discount_plan is 17:
			single_per = kohls
			startup_1 = kohls_start
		#Unitedhealth Allies
		if discount_plan is 18:
			print "Unitedhealth Allies discount plan"
			print
			single_per = unitedhealth
			startup_1 = unitedhealth_start
			print
			print 'Unitedhealth Allies requires all members to have direct draft'
			print 'from their checking account'
			print
			print 'Enter as a new contract in Club Hub'
			print
			print 'Enter their information to the Healthy Contributions\' webpage'
			print 'DO NOT put this membership into ABC'
			print
			raw_input('press any key to continue to membership rates')		
		#ten percent off
		if discount_plan is 31:
			single_per = ten_off
			extra = ten_off_extra	
		###################
		## End Discounts ##	
		if members is 1:
			os.system('CLS')
			contract = single_per * term
			rate = single_per
			fee = startup_1
			total = single_per * term + startup_1
			down_pay = single_per + startup_1
			bal = total - down_pay
		else:
			os.system('CLS')
			#how many members
			members = members - 1
			#rate
			primary = single_per * term
			secondary = extra * members * term
			#startup fee
			extra_fee = startup_extra * members
			#total startup fees
			fee = startup_1 + extra_fee
			#total monthly with fee
			rate = extra * members + single_per
			#
			members = members + 1
			#sent to cheat sheet
			contract = primary + secondary
			fee = fee
			total = contract + fee
			down_pay = rate + fee
			bal = total - down_pay
		#Read out
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
			print 'members.	 If the secondary members want to'
			print 'join then they will need to be on their own'
			print 'membership'
		else:
			print "Single membership rate is %s dollars per month" % (rate)
			print "plus a %s dollar start up fee" % (fee)
			print "Total year Membership cost %s dollars" % (total)
			print
			#Contract fillout cheat sheet
			print "Contract Cheat Sheet:"
			print
			print "start membership"
			print date
			print "end membership"
			print date_end
			print
			print "Membership --------- %s" % (contract)
			print "Tanning ------------ %s" % (tanning)
			print "Processing Fee ----- %s" % (fee)
			print "Anytime Health ----- %s" % (anytime_health)
			print "Total -------------- %s" % (total)
			print "Downpaymnt --------- %s" % (down_pay)
			print "Remaining Balance -- %s" % (bal)
			print
		raw_input ("press enter to restart")
		os.system('CLS')
	else:
		os.system('CLS')		
	##### end #####
