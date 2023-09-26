def houseCsm(hl):
    houseArea = []
    csm = []
    for i in range(len(hl)):
        total = 0.0
        for k, v in hl[i].items():
            if k != "id" and k != "price":
                total += v
        houseArea.append(total)
        csm.append(hl[i]["price"] / total)
        total = 0

    return houseArea, csm


def roomCheck(hl):
    nonExisting = []
    existing = []
    totaLExisting = []
    totalNonExisting = []
    for i in range(len(hl)):
        for k, v in hl[i].items():
            if k != "id" and k != "price":
                if v == 0:
                    print(k)
                    nonExisting.append(k)
                else:
                    existing.append(k)
        totaLExisting.append(existing)
        totalNonExisting.append(nonExisting)
        nonExisting = []
        existing = []
    return totaLExisting, totalNonExisting


def houseAnalysis(hl):
    houselist = []

    hc = houseCsm(hl)
    rch = roomCheck(hl)

    for i in range(len(hc)):
        houseData = {
            "id": i + 1,
            "total": hc[0][i],
            "cpsm": hc[1][i],
            "empty": rch[0][i],
        }
        houselist.append(houseData)

    return houselist


houses = [
    {
        "id": 1,
        "price": 185000,
        "b1": 9.5,
        "b2": 5,
        "b3": 0,
        "lv": 8,
        "kit": 5,
        "bath": 1.8,
        "gar": 12,
    },
    {
        "id": 2,
        "price": 201999,
        "b1": 12,
        "b2": 8,
        "b3": 4,
        "lv": 14,
        "kit": 7,
        "bath": 3,
        "gar": 18,
    },
]

houseCost = houseCsm(houses)
print(houseCost)
print(
    f"First House Total Square Meter {houseCost[0][0]} Second House Total Square {houseCost[0][1]}"
)

checkCspm = input("Do You want to Check the CSPM ? (Y/N)")
if checkCspm == "Y":
    print(f"First House CPSM {houseCost[1][0]}  Second House CPSM {houseCost[1][1]}")
else:
    pass

rc = roomCheck(houses)
print(rc)
print(
    f"First House NonExisting Rooms {rc[1][0]} Second House NonExisting Rooms {rc[1][1]}"
)
checkRoom = input("Do You want to Check the Existing Room ? (Y/N)")
if checkRoom == "Y":
    print(
        f"First House Existing Room {rc[0][0]}  Second House Existing Room {rc[0][1]}"
    )
else:
    pass

print(houseAnalysis(houses))
