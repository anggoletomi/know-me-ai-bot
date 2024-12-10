# Know Me AI Bot

A customizable AI chatbot that represents your personal details, skills, and experiences. This project enables you to quickly set up a personal assistant bot by configuring a simple file-based setup.

---

## Initial Setup

Follow these steps to get started:

1. **Set up the `.env` file**:
   - Copy or rename the `env.template` file to `.env`:
     - **On Linux/Mac**:
       ```bash
       cp .env.template .env
       ```
     - **On Windows**:
       ```cmd
       copy .env.template .env
       ```
   - Update the following fields in `.env`:
     - `OPENAI_APIKEY`: Add your OpenAI API key.

2. **Set up the `config.py` file**:
   - Open `config.py` and change current value to your public personal information (e.g., name, skills, bio).

3. **Install the requirements**:
   - Run the following command:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the main script**:
   - Navigate to the `scripts/` directory and execute the main script:
     ```bash
     python config.py
     ```

5. **Check local development**:
   - Open your web browser and go to:
     ```
     http://127.0.0.1:5000
     ```
---

## About `config.py`

The `config.py` file is used to define personal details for the chatbot. This project uses a file-based configuration for simplicity.

**Why File-Based Configuration?**

- **Ease of Setup**: Users cloning this repository can quickly configure the bot by editing this file without needing to set up a database server or manage database connections.

- **Static Data**: The data used in this bot (such as name, skills, background) is static and does not require dynamic updates or scaling, which eliminates the need for a database.

- **Simplified Deployment**: By avoiding a database, the project is easier to deploy and run, especially for users with minimal technical expertise or limited infrastructure.

This approach demonstrates the flexibility of using the right tool for the right task.

*) *Since no database is utilized and no chat memory service feature has been added, the chat will have no history and no user interactions will be recorded.*