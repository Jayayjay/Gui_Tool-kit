import tkinter as tk

def create_floating_window():
    window = tk.Tk()
    window.title("Floating Window")
    window.geometry("200x80")
    window.attributes("-topmost", True)  # Makes the window stay on top
    window.overrideredirect(True)  # Removes the title bar

    # Add buttons and icons
    tools_button = tk.Button(window, text="Tools")
    tools_button.pack(side="left", padx=10)

    mic_button = tk.Button(window, text="🎤", bg="red", fg="white")
    mic_button.pack(side="left", padx=10)

    settings_button = tk.Button(window, text="Settings")
    settings_button.pack(side="left", padx=10)

    question_button = tk.Button(window, text="?")
    question_button.pack(side="left", padx=10)

    window.mainloop()

create_floating_window()
