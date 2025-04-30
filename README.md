# AudioCode

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/FastAPI-green.svg" alt="FastAPI Version">
  <img src="https://img.shields.io/badge/TypeScript-blue.svg" alt="TypeScript Version">
  <img src="https://img.shields.io/badge/AWS-EC2-orange.svg" alt="AWS EC2">
  <img src="https://img.shields.io/badge/PostgreSQL-blue.svg" alt="PostgreSQL">
</div>

## Overview

AudioCode is an innovative VS Code extension that transforms spoken instructions into precise Python code. Built with accessibility in mind, this project combines natural language processing with code generation to make programming more accessible to everyone.

## Features

- Real-time voice-to-code conversion
- FastAPI backend with PostgreSQL database
- Fine-tuned CodeT5 model for accurate code generation
- VS Code extension integration
- Asynchronous processing with status polling
- Secure database storage of transcriptions

## Example Commands

Here are some example voice commands you can try. Speak these commands clearly after clicking the "Start Recording" button:

### Basic Variable Creation

- "Create an empty list called results"
- "Make a dictionary called person with keys name and age"
- "Create a set called primes containing 2, 3, and 5"
- "Create a string variable called greeting and set it to hello world"
- "Initialize a boolean variable is_active and set it to false"
- "Make a tuple named position with three coordinates"

### Functions

- "Write a function called divide that takes parameters x and y and returns x divided by y"
- "Write a function named print_welcome that accepts a name and prints welcome plus the name"
- "Write a function called is_positive that checks if a number is greater than zero and returns true or false"
- "Write a function called subtract_ten that takes a number and returns it minus 10"

### Control Flow

- "Write an if-else block that checks if temperature is above 30. If it is, print hot. Otherwise, print cold"
- "Write a for loop that prints numbers from 5 to 10"
- "Create a while loop that runs while counter is less than 5. Inside the loop, increase counter by 2"
- "Write an if-elif-else block that checks if a number n is less than 0, equal to 0, or greater than 0 and prints a message"

### Data Structures

- "Initialize a deque named history with no elements"
- "Create a Counter object based on a list named votes"
- "Make a default dictionary called scores with int as default value"
- "Create a list called doubled containing numbers from 1 to 5 each multiplied by 2"

### Tips for Best Results

1. Keep commands simple and focused on one task
2. Speak clearly and at a normal pace
3. Use natural language but be specific about variable names
4. Wait for each command to be processed before giving the next one
5. The system will automatically stop polling after 5 minutes of inactivity

## Architecture

The project consists of three main components:

1. **VS Code Extension** (`/extension`)

   - TypeScript-based VS Code extension
   - Real-time audio recording and processing
   - User interface for code generation

2. **Backend Service** (`/backend`)

   - FastAPI server
   - PostgreSQL database integration
   - Audio processing and transcription

3. **ML Model** (`/model`)

   - Fine-tuned CodeT5 model
   - Custom training pipeline
   - Model evaluation and testing

4. **NextJS Website**

   - React frontend to capture microphone audio
   - Send audio to backend service

## Technologies Used

### Backend

- FastAPI
- PostgreSQL
- Python

### Frontend (VS Code Extension)

- TypeScript
- VS Code Extension API
- NextJS

### Machine Learning

- Hugging Face Transformers
- CodeT5 model

### Infrastructure

- AWS EC2
- AWS RDS (PostgreSQL)

## Deployment

The project is deployed on AWS infrastructure:

- Backend API and ML model are hosted on AWS EC2
- PostgreSQL database is managed through AWS RDS
- VS Code extension is published on the VS Code Marketplace
- NextJS website is deployed via Vercel

## Author

**Gregory (Trace) Glasby**

- Email: gglasby@unc.edu
- LinkedIn: [linkedin.com/in/gglasby04](https://linkedin.com/in/gglasby04)
- GitHub: [github.com/tr4ce123](https://github.com/tr4ce123)
- Website: [traceglasby.com](https://traceglasby.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
