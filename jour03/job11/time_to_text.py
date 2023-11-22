
def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    
    if heures == 1:
        heures_text = "heures"
    else:
        heures_text = "heures"
    
    if minutes_restantes == 1:
        minutes_text = "minute"
    else:
        minutes_text = "minutes"
    
    print(f"{heures} {heures_text} y {minutes_restantes} {minutes_text}")

time_to_text(165)