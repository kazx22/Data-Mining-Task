def houseCsm(hl):
    houseArea = []
    csm = []
    for i in range(len(hl)):
        total = 0.0
        for k, v in hl[i].items():
            if k != "Price":
                total += v
        houseArea.append(total)
        csm.append(hl[i]["Price"] / total)
        total = 0

    return houseArea, csm


def roomCheck(hl):
    nonExisting = []
    existing = []
    totaLExisting = []
    totalNonExisting = []
    for i in range(len(hl)):
        for k, v in hl[i].items():
            if k != "Price":
                if v == 0:
                    nonExisting.append(k)
                else:
                    existing.append(k)
        totaLExisting.append(existing)
        totalNonExisting.append(nonExisting)
        nonExisting = []
        existing = []
    return totaLExisting, totalNonExisting


def houseAnalysis(hl):
    houseInfo = []

    hc = houseCsm(hl)
    rch = roomCheck(hl)

    for i in range(len(hl)):
        houseData = {
            "Id": i + 1,
            "Total Square Meters": hc[0][i],
            "CPSM": hc[1][i],
            "Empty Rooms": rch[0][i],
        }
        houseInfo.append(houseData)

    return houseInfo


houses = [
    {
        "Price": 185000,
        "Bedroom 1": 9.5,
        "Bedroom 2": 5,
        "Bedroom 3": 0,
        "Living-Room": 8,
        "Kitchen": 5,
        "Bathroom": 1.8,
        "Garage": 12,
    },
    {
        "Price": 201999,
        "Bedroom 1": 12,
        "Bedroom 2": 8,
        "Bedroom 3": 4,
        "Living-Room": 14,
        "Kitchen": 7,
        "Bathroom": 3,
        "Garage": 18,
    },
    {
        "Price": 140000,
        "Bedroom 1": 0,
        "Bedroom 2": 0,
        "Bedroom 3": 0,
        "Living-Room": 55,
        "Kitchen": 0,
        "Bathroom": 0,
        "Garage": 0,
    },
    {
        "Price": 180000,
        "Bedroom 1": 11.5,
        "Bedroom 2": 2,
        "Bedroom 3": 3,
        "Living-Room": 6,
        "Kitchen": 5,
        "Bathroom": 2,
        "Garage": 10,
    },
    {
        "Price": 195000,
        "Bedroom 1": 15.5,
        "Bedroom 2": 3,
        "Bedroom 3": 2,
        "Living-Room": 8,
        "Kitchen": 5,
        "Bathroom": 2.5,
        "Garage": 14,
    },
    {
        "Price": 210000,
        "Bedroom 1": 14.5,
        "Bedroom 2": 6,
        "Bedroom 3": 3,
        "Living-Room": 12,
        "Kitchen": 5,
        "Bathroom": 2,
        "Garage": 14,
    },
    {
        "Price": 210000,
        "Bedroom 1": 21.5,
        "Bedroom 2": 7,
        "Bedroom 3": 4,
        "Living-Room": 11,
        "Kitchen": 5,
        "Bathroom": 2,
        "Garage": 14,
    },
    {
        "Price": 205000,
        "Bedroom 1": 19.5,
        "Bedroom 2": 4,
        "Bedroom 3": 6,
        "Living-Room": 10,
        "Kitchen": 5,
        "Bathroom": 2,
        "Garage": 18,
    },
    {
        "Price": 170000,
        "Bedroom 1": 1.5,
        "Bedroom 2": 8,
        "Bedroom 3": 7,
        "Living-Room": 10,
        "Kitchen": 5,
        "Bathroom": 1.5,
        "Garage": 0,
    },
    {
        "Price": 175000,
        "Bedroom 1": 5.5,
        "Bedroom 2": 10,
        "Bedroom 3": 8,
        "Living-Room": 6,
        "Kitchen": 5,
        "Bathroom": 1.5,
        "Garage": 0,
    },
    {
        "Price": 180000,
        "Bedroom 1": 3.5,
        "Bedroom 2": 12,
        "Bedroom 3": 8,
        "Living-Room": 6,
        "Kitchen": 5,
        "Bathroom": 1.8,
        "Garage": 0,
    },
    {
        "Price": 185000,
        "Bedroom 1": 8.5,
        "Bedroom 2": 1,
        "Bedroom 3": 0,
        "Living-Room": 6,
        "Kitchen": 5,
        "Bathroom": 1.8,
        "Garage": 8,
    },
    {
        "Price": 185000,
        "Bedroom 1": 12.5,
        "Bedroom 2": 4,
        "Bedroom 3": 2,
        "Living-Room": 6,
        "Kitchen": 5,
        "Bathroom": 1.8,
        "Garage": 12,
    },
    {
        "Price": 285000,
        "Bedroom 1": 15.5,
        "Bedroom 2": 15,
        "Bedroom 3": 12,
        "Living-Room": 25,
        "Kitchen": 15,
        "Bathroom": 8,
        "Garage": 14,
    },
]

houseCost = houseCsm(houses)


for i in range(len(houses)):
    print(f"Numebr {i+1} House Total Square Meter {houseCost[0][i]}")

checkCpsm = input("Do You want to Check the CPSM ? (Y/N)")

if checkCpsm == "Y":
    for i in range(len(houses)):
        print(f"Number {i+1} House CPSM {houseCost[1][i]}")
else:
    pass

rc = roomCheck(houses)

for i in range(len(houses)):
    print(f"Number {i+1} NonExisting Rooms {rc[1][i]  or  0} ")


checkRoom = input("Do You want to Check the Existing Room ? (Y/N)")
if checkRoom == "Y":
    for i in range(len(houses)):
        print(f"Number {i+1} House Existing Room {rc[0][i]}")
else:
    pass

print(houseAnalysis(houses))
