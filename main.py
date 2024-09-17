import sensor
import motor
import time

DESIRED_DISTANCE = 20  # Ønsket afstand til væggen i cm
BASE_SPEED_LEFT = 35   # Grundlæggende hastighed for venstre motor (%)
BASE_SPEED_RIGHT = 35  # Grundlæggende hastighed for højre motor (%)
MIN_DISTANCE = 15      # Minimumsafstand før robotten bakker
MAX_DISTANCE = 25      # Maksimumafstand før robotten justerer mod væggen

def backup_to_distance():
    """Robotten bakker, indtil den er ved den ønskede afstand fra væggen."""
    print("For tæt på væggen! Bakker tilbage til ønsket afstand.")

    while True:
        distance = sensor.read_distance_cm()
        if distance is not None:
            print(f"Bakning - Aktuel afstand: {distance:.2f} cm")
            if distance >= DESIRED_DISTANCE:
                break
        else:
            print("Kunne ikke læse afstand under bakning.")
        motor.move_backward(30, 30)  # Bakker med samme hastighed
        time.sleep(0.1)

    motor.stop()
    time.sleep(0.5)  # Kort pause

    # Kør fremad med venstre motor 5% hurtigere i 2 sekunder
    print("Kører fremad med venstre motor 5% hurtigere i 2 sekunder.")
    motor.move_forward(BASE_SPEED_LEFT + 5, BASE_SPEED_RIGHT)
    time.sleep(2)

    # Kør fremad med samme hastighed på begge motorer
    print("Kører fremad med samme hastighed på begge motorer.")
    motor.move_forward(BASE_SPEED_LEFT, BASE_SPEED_RIGHT)

while True:
    distance = sensor.read_distance_cm()

    if distance is not None:
        print(f"Aflæst afstand: {distance:.2f} cm")

        if distance < MIN_DISTANCE:
            # Robotten er for tæt på væggen, bakker tilbage
            backup_to_distance()

        elif distance > MAX_DISTANCE:
            # Øg venstre motors hastighed for at dreje mod væggen
            print(f"Afstand: {distance:.2f} cm | Justerer mod væggen (drejer mod højre).")
            motor.move_forward(BASE_SPEED_LEFT + 5, BASE_SPEED_RIGHT)
        else:
            # Fortsæt fremad med grundlæggende hastigheder
            print(f"Afstand: {distance:.2f} cm | Følger væggen.")
            motor.move_forward(BASE_SPEED_LEFT, BASE_SPEED_RIGHT)
    else:
        print("Ingen afstandsmåling modtaget. Stopper motorerne.")
        motor.stop()

    time.sleep(0.05)
