Sports_shop = {

    "name"          : "SAMRAT SPORTS",
    "rating"        : 4.5,
    "address"       : "NEAR CLOCK TOWER",
    "oppening_time" : "9PM To 10AM",
    "promo_code"    : "SPORTS359",

}

Sports_shop["Phone_Number"] = "95648-5314",

Sports_shop["Items"] = "Football_kit, Cricket_kit",

print(Sports_shop)
print(len(Sports_shop))
print(type(Sports_shop))

Kit1 = {

    "name": "Football",
    "price": "1500",
    "brand": "Spectra",
}

Kit2 = {

    "name": "Cricket",
    "price": "25000",
    "brand": "Adidas",
}

Kit3 = {

    "name": "vollyball",
    "price": "2000",
    "brand": "Spectra",
}
kits = {"kit1", "kit2", "kit3"}
Sports_shop["kits"] = kits

print("sports_shop", Sports_shop)
print(Sports_shop)
print(len(Sports_shop))
