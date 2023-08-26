import time
import sys
import os

class TrafficLightSimulator:
    def __init__(self):
        self.colors = ["RED", "YELLOW", "GREEN"]
        self.color_times = {}
        self.default_time = 3

    def set_color_time(self, color, time_input):
        self.color_times[color] = time_input

    def show_art(self, color):
        with open(f'ascii_art/{color}', "r") as file:
            content = file.read()
            print(content)

    def change_color(self, color):
        os.system("clear")
        print("Press Ctrl+C to exit the program. ")
        self.show_art(color)

    def run(self):
        self.colors.append("YELLOW")
        while True:
            try:
                for color in self.colors:
                    self.change_color(color)
                    time.sleep(self.color_times[color])
            except KeyboardInterrupt:
                print("Exiting Traffic Light Simulator")
                sys.exit()

def main():
    traffic_light = TrafficLightSimulator()

    for color in traffic_light.colors:
        try:
            time_input = float(input(f"Enter time for {color} light (seconds): "))
            if time_input <= 0:
                print("Only positive numbers allowed")
                print(f"Setting default time for {color}: {traffic_light.default_time} seconds")
                traffic_light.set_color_time(color, traffic_light.default_time)
            else:
                traffic_light.set_color_time(color, time_input)
        except ValueError:
            print("Only positive numbers allowed as input. Exiting...")
            sys.exit()

    traffic_light.run()

if __name__ == "__main__":
    main()
