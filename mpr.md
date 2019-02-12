lm_hg202 - National Daily Direct Hogs (morning)
lm_hg203 - National Daily Direct Hogs (afternoon)

Date: Date
Type: PurchaseType
Volume: Integer
Price: Real
Low: Real
High: Real

lm_pk602 - National Daily Pork (afternoon)

Date: Date
Cut_Loads: Real
Trimming_Loads: Real
Carcass: Real
Loin: Real
Butt: Real
Picnic: Real
Rib: Real
Ham: Real
Belly: Real

lm_hg200 - National Daily Direct Hog Prior Day - Purchased Swine (0800C)

Date: Date
Type: PurchaseType
Volume: Integer
Price: Real
Low: Real
High: Real

lm_hg201 - National Daily Direct Hog Prior Day - Slaughtered Swine (1000C)

Date: Date
Type: PurchaseType
Volume: Integer
Base Price: Real
Net Price: Real
Average Live Weight: Real
Average Carcass Weight: Real

lm_hg214 - Weekly National Direct Swine Report
https://www.ams.usda.gov/mnreports/lm_hg214.txt

Daily estimated hog slaughter

Estimate:
Current cash index
Future cash index
Current cutout index
Future cutout index
Total slaughter
Total supply

CME CASH INDEX VIEW
http://s3.amazonaws.com/zanran_storage/www.cmegroup.com/ContentPages/2541882828.pdf

Negotiated Head Count * Negotiated Average Carcass Weight = Negotiated Total Weight
Market Formula Head Count * Market Formula Average Carcass Weight = Market Formula Total Weight
Negotiated Formula Head Count * Negotiated Formula Market Weight = Negotiated Formula Total Weight

Negotiated Total Weight * Negotiated Average Net Price = Negotiated Total Value
Market Formula Total Weight * Market Formula Average Net Price = Market Formula Total Value
Negotiated Formula Total Weight * Negotiated Formula Average Net Price = Negotiated Formula Total Value

Negotiated Total Value + Market Formula Total Value + Negotiated Formula Total Value = Current Day Total Value

2 Day Total Value / 2 Day Total Weight = CME Cash Index

CME CUTOUT INDEX VIEW
https://www.cmegroup.com/trading/agricultural/livestock/pork-cutout-index.html

Sum(previous 5 days of carcass value * carcass loads) / Sum(previous 5 days of carcass loads)


sj_ls711 : actual slaughter numbers
nw_ls255 : national direct delivered feeder pig
