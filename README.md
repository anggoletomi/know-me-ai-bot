# Know Me AI Bot

A customizable AI chatbot that represents your personal details, skills, and experiences. This project enables you to quickly set up a personal assistant bot by configuring a simple file-based setup.

---

## Initial Setup

Follow these steps to get started:

**1. Set up the `.env` file**
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
  - **`OPENAI_APIKEY`**: Add your OpenAI API key.
  - **`OPENAI_MODEL`**: Add your OpenAI API model.
  - **`FLASK_SECRET_KEY`**: Add a generated Flask secret key. You can generate one using Python:
    ```python
    import secrets
    print(secrets.token_hex(32))
    ```

> **Note**: If you don't want to generate a key, the app provides a default fallback for demonstration purposes. However, it is recommended to set your own `FLASK_SECRET_KEY` for better security.

**2. Set up the `config.py` file**:
   - Open `config.py` and change current value to your public personal information (e.g., name, skills, bio).

**3. Install the requirements**:
   - Run the following command:
     ```bash
     pip install -r requirements.txt
     ```

**4. Run the main script**:
   - Navigate to the `scripts/` directory and execute the main script:
     ```bash
     python config.py
     ```

**5. Check local development**:
   - Open your web browser and go to:
     ```
     http://127.0.0.1:5000
     ```

**6. Deployment**
- **Using Render Free Tier**:
  - I deployed this application using the **free tier** from [Render](https://render.com/).
  - **Limitation**: Render free-tier services automatically spin down due to inactivity after 15 minutes. This means the server will go to sleep and will need some time to spin up again when accessed.

- **Keeping the Server Alive**:
  - To ensure the server stays available, I set up a scheduled ping using:
    1. **`keep_alive.py`**:
       - This script sends regular HTTP GET requests to the deployed server URL to prevent it from being marked as idle.

    2. **GitHub Actions**:
       - To automate the pinging process, I use GitHub Actions with a workflow file located at `.github/workflows/schedule-keep-alive.yml`.
       - This workflow schedules the `keep_alive.py` script to run every 14 minutes to keep the server active.

    3. Go to the **Actions** tab on GitHub to verify the workflow is running correctly.

---

## About `config.py`

The `config.py` file is used to define personal details for the chatbot. This project uses a file-based configuration for simplicity.

**Why File-Based Configuration?**

- **Ease of Setup**: Users cloning this repository can quickly configure the bot by editing this file without needing to set up a database server or manage database connections.

- **Static Data**: The data used in this bot (such as name, skills, background) is static and does not require dynamic updates or scaling, which eliminates the need for a database.

- **Simplified Deployment**: By avoiding a database, the project is easier to deploy and run, especially for users with minimal technical expertise or limited infrastructure.

This approach demonstrates the flexibility of using the right tool for the right task.

*) *Since no database is utilized and no chat memory service feature has been added, the chat will have no history and no user interactions will be recorded.*