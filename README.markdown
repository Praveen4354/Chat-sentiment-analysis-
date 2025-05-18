# Chat Sentiment Analysis

A Streamlit web application that analyzes the sentiment of chat messages, classifying them as positive, negative, or neutral using a pre-trained Transformer model from Hugging Face. Users can input a chat message (e.g., "I love this app!"), view the sentiment score, and see a visual representation of the result. The project leverages a pre-trained model for efficient sentiment analysis and is deployable on Render’s free tier for public access.

## Table of Contents
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment on Render](#deployment-on-render)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Sentiment Analysis**: Classifies chat messages as positive, negative, or neutral using a Transformer model.
- **Interactive UI**: Streamlit interface with text input, sentiment display, and optional visualizations (e.g., confidence bars).
- **Pre-Trained Model**: Uses Hugging Face’s `distilbert-base-uncased-finetuned-sst-2-english` for efficient inference.
- **Error Handling**: Manages invalid inputs and API/model errors gracefully.
- **Render Deployment**: Optimized for Render’s free tier (512 MB RAM) with minimal memory usage.

## Repository Structure
- `app.py`: Main Streamlit application for sentiment analysis and UI.
- `requirements.txt`: Python dependencies for the project.
- `model.py` (optional): Helper script for model loading or inference logic.
- `utils.py` (optional): Utility functions for text preprocessing or visualization.
- `chat_data.csv` (optional): Dataset of chat messages for testing or fine-tuning (if included).

## Model
The project uses a pre-trained DistilBERT model (`distilbert-base-uncased-finetuned-sst-2-english`) from Hugging Face’s Transformers library, fine-tuned for sentiment analysis on the SST-2 dataset. It provides:
- **Input**: Text (chat messages).
- **Output**: Sentiment label (positive/negative) and confidence score.
- **No Local Training**: The model is pre-trained, requiring no GPU or extensive resources.

To fine-tune or use a different model, modify `model.py` or `app.py` to load custom weights or datasets (e.g., `chat_data.csv`).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/your_sentiment_analysis_repo.git
   cd your_sentiment_analysis_repo
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional: Hugging Face Setup**:
   - If using a gated model or API, create a Hugging Face account at [huggingface.co](https://huggingface.co).
   - Generate an API token at Settings > Access Tokens.
   - Set the environment variable:
     ```bash
     export HUGGINGFACE_TOKEN=your_api_token
     ```

4. **Optional: Dataset**:
   - If `chat_data.csv` is included, ensure it’s in the repo root.
   - Format: Columns like `message` (text) and `sentiment` (optional labels).

## Usage
1. **Run Locally**:
   ```bash
   streamlit run app.py
   ```
   Open [http://localhost:8501](http://localhost:8501) in your browser.

2. **Analyze Sentiment**:
   - Enter a chat message (e.g., "This is awesome!").
   - Click "Analyze Sentiment".
   - View the sentiment (e.g., Positive) and confidence score.
   - Optional: See visualizations (e.g., bar chart of sentiment probabilities).

3. **Troubleshooting**:
   - Ensure `HUGGINGFACE_TOKEN` is set if required.
   - Check internet connectivity for model downloads.
   - Verify dataset format if using `chat_data.csv`.

## Deployment on Render
Deploy the application on Render’s free tier for public access.

1. **Prepare Repository**:
   Ensure all files (`app.py`, `requirements.txt`, etc.) are committed:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create Render Web Service**:
   - Log in to [Render](https://render.com).
   - Go to Dashboard > New > Web Service.
   - Connect your GitHub repository.

3. **Configure**:
   - **Name**: `chat-sentiment-analysis`
   - **Environment**: Python
   - **Region**: Oregon (or closest)
   - **Branch**: `main`
   - **Root Directory**: (leave blank)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   - **Instance Type**: Free
   - **Environment Variables** (optional):
     - Key: `HUGGINGFACE_TOKEN`, Value: `your_api_token` (if needed)
   - **Auto-Deploy**: Enable
   - Click *Create Web Service*.

4. **Monitor Deployment**:
   - Build time: ~5-7 minutes.
   - Check logs in Render Dashboard for errors (e.g., missing dependencies).
   - Access the URL (e.g., `https://chat-sentiment-analysis.onrender.com`).

5. **Test**:
   - Open the Render URL.
   - Input a message (e.g., "I’m so happy!").
   - Verify sentiment output and UI.
   - Expect ~5-15 seconds for analysis (plus 30-60 second wake-up for free tier).

6. **Troubleshooting**:
   - **Memory Errors**: If logs show “OOM Killed”, reduce model size in `model.py` (e.g., use a smaller Transformer like `distilbert`).
   - **Timeouts**: Increase timeout in API calls or optimize inference in `app.py`.
   - **Bad Gateway**: Check [Render Status](https://status.render.com) or redeploy via Manual Deploy.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push: `git push origin feature-name`.
5. Open a pull request.

Please follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) and include tests where applicable.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.