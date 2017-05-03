# NOTE: Wekinator must already be running
read -p "Confirm that wekinator is already running."

# java -jar ~/Downloads/weki/WekiMini.jar &

# Start Tentacle Control (Stepper)
python ./control/TentacleControl.py &

# Myo Interface (Requires wekinator)
python ./myo-raw/own.py &
python ./myo-raw/own_with_weki.py &




