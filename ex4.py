import matplotlib
matplotlib.use('Agg')
from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime
import numpy as np

reader = csv.DictReader(open(sys.argv[1], 'r'))
obamadonations = defaultdict(lambda:0)
obamadonationsAttrib = defaultdict(int)
mccainDonations = defaultdict(int)
mccainDonationsAttrib = defaultdict(int)
total_amount = float(0)

for row in reader:
 name = row['cand_nm'] 
 attrib = row['receipt_desc']
 datestr = row['contb_receipt_dt'] 
 amount = float(row['contb_receipt_amt']) 
 date = datetime.datetime.strptime(datestr, '%d-%b-%y') 

 if 'Obama' in name: 
    obamadonations[date] += amount
    if 'REATTRIBUTION' in attrib:
		obamadonationsAttrib[date] +=amount

 elif 'McCain' in name:
	 mccainDonations[date] += amount
	 if 'TO SPOUSE' in attrib:
		 mccainDonationsAttrib[date] +=amount


sorted_by_date = sorted(obamadonations.items(), key=lambda (key,val): key)
sorted_by_date1 = sorted(mccainDonations.items(), key = lambda (key,val): key)
xs,ys = zip(*sorted_by_date)
xs1,ys1 = zip(*sorted_by_date1)

sorted_by_date2 = sorted(mccainDonationsAttrib.items(), key = lambda (key,val): key)
sorted_by_date3 = sorted(obamadonationsAttrib.items(), key = lambda (key,val): key)
xs2,ys2 = zip(*sorted_by_date2)
xs3,ys3 = zip(*sorted_by_date3)


fig = plt.figure(figsize=(10,5))
fig.suptitle('Ratio of Obama Vs McCain Donations to Reattribution to Spouse', fontsize=14)
plt.xlabel('Date/Year',fontsize=18)
plt.ylabel('Millions of Dollar\'s', fontsize=16)
plt.plot(xs, np.cumsum(ys), label='Obama''s Total Donations')
plt.plot(xs1,np.cumsum(ys1),label='McCain Total Donations',color='#FF0000')




plt.legend(loc='upper center', ncol = 4)
plt.savefig('ex4py.png', format='png')
