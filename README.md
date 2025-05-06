# AlphaBake Tryon API Testing

This repository contains a Python script for testing the AlphaBake Tryon API, along with a simple frontend to view AWS signed URLs.

## Project Structure

- `tryon-api-example.py`: Main Python script for interacting with the AlphaBake Tryon API
- `requirements.txt`: Python dependencies
- `frontend/`: Simple web interface to display the tryon results
- `inputs/`: Directory containing input images (human and garment)
- `outputs/`: Directory where generated tryon images are saved

## Setup

### Python Environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API key, get the API_KEY by signing up to [app.alphabake.io](https://app.alphabake.io)
   ```
   API_KEY=your_api_key_here
   ```

### Input Images

Place your input images in the `inputs/` directory:
- `inputs/human.jpg`: The person image for the tryon
- `inputs/garment.jpg`: The garment image to try on

## Usage

1. Run the Python script:
   ```bash
   python tryon-api-example.py
   ```

2. The script will:
   - Send the images to the AlphaBake Tryon API
   - Poll for the result until it's ready
   - Download the resulting tryon image to `outputs/tryon.png`

## Frontend Viewer

The frontend directory contains a simple web page to display AWS signed URLs:

1. Open `frontend/index.html` in a web browser
2. By default, it will display a sample image using a hardcoded AWS signed URL
3. To view your own image, modify the `signedUrl` in `frontend/script.js` with the URL returned by the API

## API Workflow

1. Submit human and garment images to the API
2. Receive a `tryon_pk` identifier
3. Poll the API with this identifier until the tryon process is complete
4. Download the resulting image from the provided AWS signed URL 