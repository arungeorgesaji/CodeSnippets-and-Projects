from gpiozero import PWMLED
import sounddevice as sd
import aubio
import numpy as np
import matplotlib.pyplot as plt

# Constants
samplerate = 16000
hop_size = 256
LED_PIN = 21  # Replace with the GPIO pin connected to your LED
 
# Create pitch detection object
pitch_o = aubio.pitch("default", hop_size, hop_size, samplerate)

# Open a microphone stream
with sd.InputStream(channels=1, samplerate=samplerate) as stream:
    # Initialize PWMLED for controlling the LED
    led = PWMLED(LED_PIN)

    print("Listening... Press Ctrl+C to exit.")
    try:
        while True:
            # Read audio data from the microphone
            audio_data, overflowed = stream.read(hop_size)
            audio_data = np.mean(audio_data, axis=1)

            # Normalize to [-1, 1]
            max_abs = np.max(np.abs(audio_data))
            if max_abs > 0:
                audio_data = audio_data.astype(np.float32) / max_abs

            # Feed into Aubio pitch detection
            pitch = pitch_o(audio_data)

            # Get the pitch frequency
            pitch_freq = pitch[0]

            # Map pitch frequency to LED brightness
            brightness = pitch_freq / 10000.0
            brightness = max(0.0, min(1.0, brightness))  # Ensure brightness is in [0, 1]

            # Set LED brightness
            led.value = brightness

            # Display pitch frequency as a real-time graph on the OLED display
            plt.clf()
            plt.bar(1, pitch_freq, color='blue')
            plt.title('Pitch Frequency')
            plt.xlabel('Sample')
            plt.ylabel('Frequency (Hz)')
            plt.xticks([])
            plt.show(block=False)
            plt.pause(1.0)
            plt.close()

    except KeyboardInterrupt:
        print("Exiting...")
        led.off()  # Turn off the LED when exiting
