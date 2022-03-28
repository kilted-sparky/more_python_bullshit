# Theatre Exercise

costAdult = 10.50
costChild = 7.30
costConcession = 8.40


def freeAdult(children):
    if children > 9:
        # discount adults
        return int(children / 10)
    else:
        return 0


def discountAdult(adult):
    subtotal = adult + costAdult
    return subtotal


def discountTenPercent(adult, children, concession):
    subtotalAdults = adult + costAdult
    subtotalChildren = children + costChild
    subtotalConcession = concession + costConcession
    Totalsubtotal = subtotalAdults + subtotalChildren + subtotalConcession
    if Totalsubtotal > 100.00:
        return Totalsubtotal * 0.1
    else:
        return 0


strGroup = input("How many in your group: ")
try:
    intGroup = int(strGroup)
except:
    print("Number no entered")

strAdult = input("How many adults in your group: ")
try:
    intAdult = int(strAdult)
except:
    print("Number not entered")

strConcession = input("How many concessions in your group: ")
try:
    intConcession = int(strConcession)
except:
    print("Number not entered")

intChildren = intGroup - intAdult - intConcession

if intChildren > 0 and intAdult == 0:
    print("Children must be accompanied by an adult.")
    exit()
if intChildren > 0 and intConcession == 0:
    print("Children must be accompanied by an adult.")
    exit()

print("")
print("Total: {0}".format(intGroup, intChildren))

chargeAdult = 0
if intAdult > 0:
    chargeAdult = intAdult * costAdult
    strAdult = "%.2f" % chargeAdult
    print("Adults:\t\t\t{0}\t£{1}".format(intAdult, strAdult))

chargeChild = 0
if intChildren > 0:
    chargeChild = intChildren * costChild
    strchild = "%.2f" % chargeChild
    print("Children: \t\t{0}\t£{1}".format(intChildren, strchild))

chargeConcession = 0
if intConcession > 0:
    chargeConcession = intConcession * costConcession
    strConcession = "%.2f" % chargeConcession
    print("Concession: \t{0}\t£{1}".format(intConcession, strConcession))

# discount, every 10 children = 1 free adult
intAdultfreebe = freeAdult(intChildren)
Adultdiscount = discountAdult(intAdultfreebe)
if intAdultfreebe > 0:
    strFreeAdult = "-%.2f" % Adultdiscount
    print("Free adult disocunt:\t{0}\t£{1}".format(intAdultfreebe, strFreeAdult))
# 10% discount
TenPercentDiscount =discountTenPercent(intAdult - intAdultfreebe, intChildren, intConcession)
if TenPercentDiscount > 0:
    strTenPerc = "-%.2f" % discountTenPercent
    print("Multi-buy discount:\t\t£{0}".format(strTenPerc))
# Final total
Total = chargeAdult + chargeChild + chargeConcession - Adultdiscount - TenPercentDiscount
strTotal = "%.2f" % Total
print("Total\t\t\t\t£{0}".format(strTotal))
