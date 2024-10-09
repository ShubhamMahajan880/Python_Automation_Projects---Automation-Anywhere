#Reqyired Libraries -
"""
pip install psutil
pip install plyer
"""

# Required Libraries
"""
pip install psutil
pip install plyer
"""

import psutil  # retrieve info on running processes & system utilization
from plyer import notification  # Python library for accessing hardware/platform features
import time

# User input for notification frequency
frequency = int(input('How often (in percentage change) would you like to be notified?: '))

# Get the initial battery percentage
battery = psutil.sensors_battery()
percent = battery.percent

# Initial notification
notification.notify(
    title="Current Battery Percentage",
    message=f"Initial Battery: {percent}% Battery Remaining",
    timeout=5
)

# Loop to check battery percentage and send notifications
while True:
    battery = psutil.sensors_battery()
    current_percent = battery.percent
    change = current_percent - percent
    diff = abs(change)  # absolute value for increase/decrease

    if diff >= frequency:
        notification.notify(
            title="Current Battery Percentage",
            message=f"{current_percent}% Battery Remaining",
            timeout=2
        )
        percent = current_percent  # Update the last notified percentage

    time.sleep(60)  # Sleep for 60 seconds before checking again
