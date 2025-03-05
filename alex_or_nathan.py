import argparse
import numpy as np
import simpleaudio as sa
import wave

if __name__ == "__main__":
    # Load the audio file
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--audio", required=True,
                    help="path to the audio file")
    args = vars(ap.parse_args())
    audio_file = args["audio"]
    print(f"Playing audio file: audio_files/{audio_file}")
    wave_obj = sa.WaveObject.from_wave_file(f"audio_files/{audio_file}")
    play_obj = wave_obj.play()

    # Wait for the audio to finish playing
    play_obj.wait_done()
