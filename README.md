# AI YOUTUBE VIDEO ANALYZER [MINOR PROJECT]
🎬 About The Project

YouTube AI Agent is a Streamlit web app that analyzes any YouTube video using an AI agent. You paste a video link and click a button. The agent reads the video data and returns a clean report with an overview and timestamps and organized topics.

Stop scrubbing through long videos to find the good parts. Let the agent do it for you.

✨ Features
🎥 Analyze any public YouTube video from just a link
🧠 Powered by the GPT OSS 120B model running on Groq
🛠️ Uses the Agno agent framework with built in YouTube tools
⏱️ Generates meaningful timestamps for major topic changes
📚 Groups related segments and tracks how topics progress
🏷️ Detects the video type such as tutorial or review or lecture
🎨 Modern dark glassmorphism interface with gradient styling
⚡ Cached agent for faster repeat usage
🔄 How It Works
<p align="center"> <img src="assets/flow.svg" alt="Workflow diagram" width="100%"> </p>
You paste a YouTube link into the input box
Streamlit sends the link to the Agno agent
The agent calls the YouTube tools to fetch video data and captions
The Groq hosted model analyzes the content using the expert instructions
A formatted markdown report appears on screen
🧰 Tech Stack
Python as the core language
Streamlit for the web interface
Agno for building the AI agent
Groq for fast model inference
YouTubeTools from Agno for fetching video data
python_dotenv for loading environment variables
📁 Project Structure
youtube_ai_agent/
    app.py                 Streamlit interface and styling
    youtube_analyzer.py    Agent definition and instructions
    .env                   Your private API keys
    requirements.txt       Python dependencies
    assets/
        banner.svg
        flow.svg
🚀 Getting Started
Prerequisites
Python 3.10 or higher
A free Groq API key from https://console.groq.com
Installation
Clone the repository
bash
git clone https://github.com/your_username/youtube_ai_agent.git
cd youtube_ai_agent
Optionally create a virtual environment using your favorite tool
Install the dependencies
bash
pip install streamlit agno groq python_dotenv youtube_transcript_api
Create a .env file in the project root and add your key
GROQ_API_KEY=your_groq_api_key_here
Run the app
bash
streamlit run app.py

The app opens in your browser at http://localhost:8501.

🖥️ Usage
Open the app in your browser
Paste a YouTube video link into the input box
Click Analyze Video
Wait a few seconds while the agent works
Read your structured analysis report
📊 What You Get In The Report
📌 A video overview with type and structure
⏱️ Timestamps with detailed summaries for each segment
🧩 Main themes and topic progression
💡 Key learning points and practical demonstrations
🔗 Important references mentioned in the video
🖼️ Screenshots

Add your own screenshots to the assets folder and link them here.

markdown
![Home Screen](assets/home_screen.png)
![Analysis Result](assets/analysis_result.png)
🔮 Future Improvements
🌍 Multi language video support
💾 Export reports as PDF or markdown
💬 Chat with the video after analysis
📜 History of previously analyzed videos
🧾 Playlist and channel level analysis
🤝 Contributing

Contributions are welcome. To contribute:

Fork the repository
Create a feature branch
Commit your changes
Push the branch and open a pull request
📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements
Agno for the agent framework
Groq for lightning fast inference
Streamlit for making data apps simple
