# Emotion Analysis API

The Emotion Analysis API is a RESTful web service that provides emotion analysis functionalities for text messages. It utilizes language models and transformers from [Hugging Face](https://huggingface.co/) to perform sentiment analysis, irony detection, and text generation.

## Prerequisites

Before using the API, make sure you have the following installed:

- Docker (to run the API in a containerized environment)

## Getting Started

1. Clone the repository to your local machine: https://github.com/luiscostalf/emotions-api.git
2. Change to the project directory: cd /emotions-api/docker
3. Build the Docker container: docker build . -t emotions-api
4. Run the Docker container: docker-compose up
5. The API will now be accessible at `http://localhost:8000/`.

## Endpoints

The Emotion Analysis API provides the following endpoints:

- `GET /`: Returns a simple JSON response indicating that the API is running.

- `POST /get_emotions`: Analyzes the emotions in a given text message and returns the emotions along with their scores as a JSON response.

- `POST /get_irony`: Detects irony in a text message and returns the irony score along with the corresponding label as a JSON response.

- `POST /get_sentiment`: Performs sentiment analysis on a text message and returns the sentiment scores along with the corresponding labels as a JSON response.

- `POST /get_bot`: Generates text responses using the T5 model for a given text message and returns the generated response as a JSON response.

## API Usage

To use the API, send a POST request to the respective endpoints with the required parameters:

- `/get_emotions`:
  - Endpoint: `http://localhost:8000/get_emotions`
  - Request Body: `{"message": "Your text message here"}`
  - Response: `{"love": float, "admiration": float, "approval": float, "neutral": float, "gratitude": float, "optimism": float, "caring": float, "joy": float,      "desire": float, "annoyance": float, "anger": float, "disapproval": float, "realization": float, "sadness": float, "excitement": float, "disappointment": float, "amusement": float, "confusion": float, "disgust": float, "curiosity": float, "remorse": float, "surprise": float, "fear": float, "nervousness": float, "pride": float, "grief": float, "embarrassment": float, "relief": float}`

- `/get_irony`:
  - Endpoint: `http://localhost:8000/get_irony`
  - Request Body: `{"message": "Your text message here"}`
  - Response: `{"non_irony": float, "irony": float}`

- `/get_sentiment`:
  - Endpoint: `http://localhost:8000/get_sentiment`
  - Request Body: `{"message": "Your text message here"}`
  - Response: `{"positive": float, "neutral": float, "negative": float}`

- `/get_bot`:
  - Endpoint: `http://localhost:8000/get_bot`
  - Request Body: `{"message": "Your text message here"}`
  - Response: `{"message": "Text response"}`

## Praise for Hugging Face

I want to express my heartfelt gratitude to Hugging Face for their exceptional work in the field of Natural Language Processing (NLP). 

Hugging Face's commitment to open-source contributions has been instrumental in democratizing AI and making it accessible to everyone. Their efforts have allowed developers, researchers, and enthusiasts alike to harness the power of AI and integrate it into various applications, enriching the lives of countless individuals.

The journey embarked upon by Hugging Face is truly inspiring, and their dedication to democratizing AI is honourable. 

Once again, thank you, Hugging Face, for your remarkable contributions, dedication, and tireless efforts to make AI more approachable and empowering for the global community.

## Important Notes

- The API uses language models and transformers from Hugging Face and it runs in a Docker container. Docker must be installed on your system to use the API.

- The API is designed as a singleton to ensure efficient resource management during emotion analysis and text generation processes.

- This API is meant to be used as an external service for your other projects. You can integrate it with your chat application or any other system that requires emotion analysis functionalities.

- For detailed usage examples, refer to the documentation of your chat application that uses this API.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute to the project and help improve the Emotion Analysis API! If you encounter any issues or have suggestions for enhancements, please create an issue or submit a pull request. Happy coding!
