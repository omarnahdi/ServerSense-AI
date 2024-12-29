
# ServerSense-AI🤖

ServerSense-AI🚀 is an intelligent server recommendation assistant designed to help users select the most suitable server plan based on their specific requirements. Using AI, ServerSense-AI matches user inputs with available server plans to recommend the best fit, or directs users to customer support for customized solutions.

---

## Features
- AI-powered server plan recommendations.
- Dynamic matching based on user needs (CPU, RAM, GPU, storage).
- Fast and efficient backend using Python and FastAPI.
- User-friendly frontend powered by HTML, CSS (Tailwind).
- JSON-based database integration.
- Version 1.0

---

## Tech Stack
- **Backend:** Python (FastAPI)
- **Frontend:** HTML, CSS (Tailwind)
- **Database:** JSON
- **AI Model:** Gemini

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/omarnahdi/ServerSense-AI.git
   cd serversense-ai
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your environment variables in a `.env` file:
   ```
   GEMINI_API_KEY=<TOKEN HERE>
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

---

## Usage

1. Access the homepage and describe your server needs.
2. ServerSense-AI will analyze your request and recommend the most suitable plan.
3. If no plan fits your needs, you'll be directed to customer support for a customized solution.

---

## Example Query

- **User Input:** "I need a server for running a small LLM (like llama3.2 a 1B parameter model)."
- **Recommended Plan:** Graphics Starter
- **Summary:** The Graphics Starter plan is well-suited for running a small LLM like llama3.2 with 1B parameters. It provides 8 CPU cores, 16 GB of RAM, and an NVIDIA T4 GPU, which are adequate for handling light GPU workloads.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## Contact
For queries or feedback, contact:
- **Author:** Omar Nahdi
- **Email:** omarnahdi.ai@gmail.com
- **LinkedIn Link:** [LinkedIn](https://www.linkedin.com/in/omarnahdi/)
