# Water state depending on the temperature in Celsius

temp = int(input("Enter the water temperature in Celsius: "))

if temp < 0 :
    print("Water is in SOLID state (ICE)")

elif temp == 0 :
    print ("Water is in MELTING ICE state")

elif 0 < temp < 100 :
    print ("Water is in LIQUID state")

elif temp == 100 :
    print("Water is at BOILING point!")

else :
    print("Water is in GAS state")
    

# Another way of doing the same but shorter and more elegant.
# Water state depending on the temperature in Celsius

temp1 = int(input("Enter the water temperature in Celsius: "))

if temp1 < 0 :
    state = "SOLID state (ICE)"

elif temp1 == 0 :
    state = "MELTING ICE state"

elif 0 < temp1 < 100 :
    state = "LIQUID"

elif temp1 == 100 :
    state = "BOILING point!"

else :
    state = "GAS state"
    
print("At the given temperature", temp1, "degrees Celsius", "the water state is", state)