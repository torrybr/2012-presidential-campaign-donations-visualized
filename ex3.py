import matplotlib
matplotlib.use('Agg')
from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime
import numpy as np

reader = csv.DictReader(open(sys.argv[1], 'r'))
obamadonations = defaultdict(lambda:0)
mccainDonations = defaultdict(lambda:0)
total_amount = float(0)

for row in reader:
 name = row['cand_nm'] 
 attrib = row['receipt_desc']
 datestr = row['contb_receipt_dt'] 
 amount = float(row['contb_receipt_amt']) 
 date = datetime.datetime.strptime(datestr, '%d-%b-%y') 

 if 'Obama' in name and 'REATTRIBUTION' in attrib: 
    obamadonations[date] += amount

 elif 'McCain' in name and 'FROM SPOUSE' in attrib:
	 mccainDonations[date] += amount


sorted_by_date = sorted(obamadonations.items(), key=lambda (key,val): key)
sorted_by_date1 = sorted(mccainDonations.items(), key = lambda (key,val): key)
xs,ys = zip(*sorted_by_date)
xs1,ys1 = zip(*sorted_by_date1)
fig = plt.figure(figsize=(10,5))
fig.suptitle('Reattribution to Spouse', fontsize=20)
plt.xlabel('Date/Year',fontsize=18)
plt.ylabel('Millions of Dollar\'s', fontsize=16)
plt.plot(xs, np.cumsum(ys), label='Obama''s Donations')
plt.plot(xs1,np.cumsum(ys1),label='McCain Donations',color='#FF0000')

plt.legend(loc='upper center', ncol = 4)
plt.savefig('ex3py.png', format='png')
