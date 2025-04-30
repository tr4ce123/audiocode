# AudioCode VS Code Extension 🎙️

<div align="center">
  <img src="https://img.shields.io/badge/TypeScript-blue.svg" alt="TypeScript">
  <img src="https://img.shields.io/badge/VS%20Code-Extension-green.svg" alt="VS Code Extension">
  <img src="https://img.shields.io/badge/Version-0.0.1-blue.svg" alt="Version">
</div>

## Overview

AudioCode is a VS Code extension that allows you to write Python code using voice commands. Simply speak your instructions, and the extension will generate the corresponding Python code in your editor. Perfect for accessibility and hands-free coding! You can even specify the line number by saying "On line (line number)... (rest of command)".

## Installation

### With Keyboard Access

1. Open VS Code
2. Go to the Extensions view (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "AudioCode"
4. Click Install

### Without Keyboard Access

1. Use your operating system's built-in screen reader and voice control:

   - On Windows: Use Windows Speech Recognition
   - On macOS: Use Voice Control
   - On Linux: Use your preferred screen reader

2. Use voice commands to navigate to your desired file:

   - On Windows: "Open VS Code" then "Open file [filename]"
   - On macOS: "Open VS Code" then "Open [filename]"

3. Use your screen reader to navigate to the command palette:

   - On Windows: "Press Control Shift P"
   - On macOS: "Press Command Shift P"

4. Say "Record Audio" to start the recording interface

   - The browser will open automatically with a microphone recording page
   - Your screen reader will announce "Microphone Recording" as the page title
   - The page will automatically focus on the "Start recording from microphone" button

5. To start recording:

   - On Windows: Say "Click Start recording from microphone" or "Press Start recording from microphone"
   - On macOS: Say "Click Start recording from microphone" or "Press Start recording from microphone"
   - Your screen reader will announce "Recording in progress..."
   - The focus will automatically move to the "Stop recording and send audio" button

6. Speak your code command

   - Speak clearly and naturally
   - Keep commands simple and concise
   - Wait for the "Recording in progress..." status

7. To stop recording and send your command:

   - On Windows: Say "Click Stop recording and send audio" or "Press Stop recording and send audio"
   - On macOS: Say "Click Stop recording and send audio" or "Press Stop recording and send audio"
   - Your screen reader will announce "Processing recording..."
   - Then "Uploading recording..."
   - Finally "Recording uploaded successfully!"
   - The focus will return to the "Start recording from microphone" button

8. For multiple commands:

   - The browser window stays open
   - Simply say "Click Start recording from microphone" again
   - Repeat steps 6-7 for each command
   - The status messages will guide you through each step

9. To end your session:
   - Say "Stop Listening" in VS Code
   - On Windows: Say "Close window" or "Close tab"
   - On macOS: Say "Close window" or "Close tab"
   - Your screen reader will confirm the window closing

## Example Commands

Here are some example voice commands you can try:

### Basic Variable Creation

- "Create an empty list called results"
- "Make a dictionary called person with keys name and age"
- "Create a set called primes containing 2, 3, and 5"
- "Create a string variable called greeting and set it to hello world"

### Functions

- "Write a function called divide that takes parameters x and y and returns x divided by y"
- "Write a function named print_welcome that accepts a name and prints welcome plus the name"
- "Write a function called is_positive that checks if a number is greater than zero and returns true or false"

### Control Flow

- "Write an if-else block that checks if temperature is above 30. If it is, print hot. Otherwise, print cold"
- "Write a for loop that prints numbers from 5 to 10"
- "Create a while loop that runs while counter is less than 5. Inside the loop, increase counter by 2"

### Data Structures

- "Initialize a deque named history with no elements"
- "Create a Counter object based on a list named votes"
- "Make a default dictionary called scores with int as default value"

## Tips for Best Results

1. **Keep Commands Simple**: Break down complex operations into simpler commands
2. **Speak Clearly**: Enunciate your words clearly for better transcription
3. **Use Natural Language**: Speak as you would write the code, but in plain English
4. **One Command at a Time**: Wait for each command to be processed before giving the next one
5. **Check Generated Code**: Use your screen reader to review the generated code
6. **Practice Voice Commands**: Familiarize yourself with your OS's voice control commands
7. **Use Screen Reader**: Enable your screen reader to navigate VS Code effectively

## Requirements

- VS Code 1.99.0 or higher
- A working microphone
- Internet connection (for audio processing)
- Screen reader (recommended for voice-only navigation)

## Known Issues

- The extension requires an internet connection to process audio
- Complex or very long commands may not be processed correctly
- Background noise may affect transcription quality
- Some screen readers may need additional configuration for optimal VS Code navigation
- Deletion of code is currently not supported, but is planned in the near future.

## License

This extension is licensed under the MIT License.

## Author

**Gregory (Trace) Glasby**

- GitHub: [github.com/tr4ce123](https://github.com/tr4ce123)
- Website: [traceglasby.com](https://traceglasby.com)
