import pygame
import os

# Initialize pygame
pygame.init()

# Create a function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Define the directory where your music files are stored
music_directory = r"directory path\"

# List all music files in the directory
music_files = [f for f in os.listdir(music_directory) if f.endswith(".mp3")]

# Display a list of available songs
print("Available songs:")
for i, music_file in enumerate(music_files):
    print(f"{i + 1}. {music_file}")

# Prompt the user to choose a song
while True:
    try:
        choice = int(input("Enter the number of the song you want to play (0 to quit): "))
        if choice == 0:
            pygame.mixer.music.stop()
            pygame.quit()
            break
        elif 1 <= choice <= len(music_files):
            selected_song = os.path.join(music_directory, music_files[choice - 1])
            play_music(selected_song)
            while True:
                action = input("Enter 'p' to pause, 'r' to resume, 'v' to set volume (0-1), or 'q' to quit: ")
                if action == 'p':
                    pygame.mixer.music.pause()
                elif action == 'r':
                    pygame.mixer.music.unpause()
                elif action == 'q':
                    pygame.mixer.music.stop()
                    pygame.quit()
                    break
                elif action == 'v':
                    try:
                        volume = float(input("Enter volume level (0-1): "))
                        if 0 <= volume <= 1:
                            pygame.mixer.music.set_volume(volume)
                        else:
                            print("Volume level must be between 0 and 1.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 1 for volume.")
                else:
                    print("Invalid action. Please enter 'p', 'r', 'v', or 'q'.")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
