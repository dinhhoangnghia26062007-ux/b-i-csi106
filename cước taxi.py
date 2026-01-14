distance = float(input("Enter distance traveled (in km): "))

if distance <= 0:
    print("Invalid distance")
else:
    if distance <= 1:
        fare = distance * 15000
    elif distance <= 10:
        fare = 15000 + (distance - 1) * 13500
    else:
        fare = 15000 + 9 * 13500 + (distance - 10) * 11000

    if distance > 120:
        fare *= 0.9

    print(f"Total fare: {fare:,.0f} VND".replace(",", "."))
