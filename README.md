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
