def inch_to_cm(mesure):
    return mesure*2.54
inch=int(input("Enter inch measure: "))
cm=inch_to_cm(inch)
print(f"Centimeters: {cm}")