def main():
    cooperResult = int(input("Enter Cooper test result (m):\n"))
    bodyWeight = float(input("Enter runner's body weight (kg):\n"))
    longestTime = 12.0
    oxygenConsumption = (0.2 * cooperResult / longestTime) + 3.5

    print(f"Oxygen consumption per  one minute and kilogram is {oxygenConsumption}  ml.")
    print(f"Oxygen consumption for the runner per one minute is {oxygenConsumption * bodyWeight} ml.")

main()
