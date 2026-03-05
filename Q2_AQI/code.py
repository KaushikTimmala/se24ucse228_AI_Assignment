"""
Simple Reflex Agent for AQI Detection
-------------------------------------

This program simulates a simple reflex agent that reads environmental
parameters from a sensor data file and determines the Air Quality Index (AQI)
category of the region.

Author: Your Name
"""

class AQIAgent:

    def __init__(self, sensor_file):
        self.sensor_file = sensor_file
        self.data = {}

    # SENSOR: Read environmental parameters from file
    def read_sensor_data(self):
        try:
            with open(self.sensor_file, 'r') as file:
                for line in file:
                    key, value = line.strip().split(":")
                    self.data[key.strip()] = float(value.strip())
        except FileNotFoundError:
            print("Error: Sensor data file not found.")
            exit()

    # REFLEX RULES: Determine AQI category
    def determine_aqi(self, aqi_value):

        if aqi_value <= 50:
            return "Good"
        elif aqi_value <= 100:
            return "Moderate"
        elif aqi_value <= 150:
            return "Unhealthy for Sensitive Groups"
        elif aqi_value <= 200:
            return "Unhealthy"
        elif aqi_value <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

    # SIMPLIFIED AQI CALCULATION
    def calculate_aqi(self):

        pm25 = self.data.get("PM2.5", 0)
        pm10 = self.data.get("PM10", 0)
        co = self.data.get("CO", 0)
        no2 = self.data.get("NO2", 0)
        so2 = self.data.get("SO2", 0)

        # Simple weighted AQI calculation
        aqi = (
            (pm25 * 0.4) +
            (pm10 * 0.3) +
            (co * 10) +
            (no2 * 0.1) +
            (so2 * 0.1)
        )

        return round(aqi, 2)

    # AGENT EXECUTION
    def run_agent(self):

        print("\n--- AQI Monitoring Agent Activated ---\n")

        self.read_sensor_data()

        print("Sensor Data Received:")
        for k, v in self.data.items():
            print(f"{k} : {v}")

        aqi_value = self.calculate_aqi()

        category = self.determine_aqi(aqi_value)

        print("\nComputed AQI:", aqi_value)
        print("Air Quality Category:", category)

        print("\nAgent Decision:", end=" ")

        if category == "Good":
            print("Air quality is safe.")
        elif category == "Moderate":
            print("Air quality is acceptable.")
        elif category == "Unhealthy for Sensitive Groups":
            print("Sensitive individuals should take precautions.")
        elif category == "Unhealthy":
            print("Limit outdoor activities.")
        elif category == "Very Unhealthy":
            print("Health alert! Avoid outdoor exposure.")
        else:
            print("Hazardous air quality! Emergency conditions.")


# MAIN PROGRAM
if __name__ == "__main__":

    sensor_file = "sensor_data.txt"

    agent = AQIAgent(sensor_file)

    agent.run_agent()
