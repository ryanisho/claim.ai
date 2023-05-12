# claim.ai (2023 CDS Spring Datathon)

This is a Flask web application that utilizes machine learning models to detect anomalies and provide descriptions for uploaded files. The application is designed to analyze files, identify potential overpayment situations, and list the possible procedures involved.

## Features

- Upload files for analysis
- Detects anomalies and identifies if the user is overpaying
- Provides a detailed description of the file content
- Lists potential procedures

## Installation and Setup

*Note: Please create a config.py file within the model directory with your OPENAI_KEY.

1. Clone the repository:
```
git clone https://github.com/ryanisho/claim.ai.git
```

2. Navigate to the project folder:
```
cd backend
```

3. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:
```
pip install -r requirements.txt
```

5. Run the Flask application:
```
flask run
```

The web application will be available at `http://127.0.0.1:5000/`.

## Usage

1. Open the web application in your browser.

2. Click the "Choose File" button and select the file you want to analyze.

3. Click the "Upload" button to upload the file.

4. The application will process the file and display the results, including a description of the file, a list of potential procedures, and an indication of whether the user is overpaying or not.

## Contributing

Jerry Chen, Ryan Ho, Iram Liu, Andrew Chen

## License

This project is not licensed. 
