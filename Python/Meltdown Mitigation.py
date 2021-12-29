def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = (((voltage*current)/theoretical_max_power)*100)
    if efficiency >= 80:
        return "green"
    elif efficiency < 80 and efficiency >= 60:
        return "orange"
    elif efficiency < 60 and efficiency >= 30:
        return "red"
    elif efficiency < 30:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = (temperature * neutrons_produced_per_second)
    if product < (threshold * 0.9):
        return "LOW"
    elif product > (threshold * 0.9) and product < (threshold * 1.1):
        return "NORMAL"
    else:
        return "DANGER"