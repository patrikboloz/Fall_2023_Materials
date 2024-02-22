#!usr/bin/bash

# Prompt the user to enter the duration of the countdown in seconds
read -p "Enter the duration of the countdown (seconds): " countdown_duration

if [ $countdown_duration -le 0 ]
then
    echo "The countdown cannot be less or equal to zero. Try again."
else
    echo "Countdown started..."

    # Start the countdown
    while [ "$countdown_duration" -gt 0 ]; 
    do
        echo "Time remaining: $countdown_duration second(s)"
        countdown_duration=$((countdown_duration - 1))
        sleep 1
    done

    echo "Countdown complete!"
fi