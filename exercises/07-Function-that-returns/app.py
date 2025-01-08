def dollar_to_euro(dollar_value):
    return dollar_value * 0.91

def euro_to_yen(euro_value):
    return euro_value * 161.70

####### ↓ YOUR CODE BELOW ↓ #######
# Convertimos dólares a euros
euros = dollar_to_euro(137)

# Convertimos euros a yenes
yenes = euro_to_yen(euros)

# Imprimimos el resultado final
print(yenes)  # Esto imprimirá el valor en yenes
