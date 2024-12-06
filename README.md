# Know Me AI Bot

A customizable AI chatbot that represents your personal details, skills, and experiences. This project enables you to quickly set up a personal assistant bot by configuring a simple file-based setup.

---

## Initial Setup

Follow these steps to get started:

1. **Setup the `.env` File**:
   - Copy or rename the `env.template` file to `.env`:
     - On Linux/Mac:
       ```bash
       cp .env.template .env
       ```
     - On Windows:
       ```cmd
       copy .env.template .env
       ```
   - Update the following fields in `.env`:
     - `OPENAI_APIKEY`: Add your OpenAI API key here.
     - `OPENAI_MODEL`: Specify the OpenAI model you want to use (example: `gpt-3.5-turbo`).

2. **Setup the `config.py` File**:
   - Navigate to the `scripts/` directory and copy or rename `config_template.py` to `config.py`:
     - On Linux/Mac:
       ```bash
       cp scripts/config_template.py scripts/config.py
       ```
     - On Windows:
       ```cmd
       copy scripts\config_template.py scripts\config.py
       ```
   - Open `config.py` and fill in your personal information (example: name, skills, bio, etc.) based on your requirements.

---

## Note

### 1. About `config.py`

The `config.py` file is used to define personal details for the chatbot. This project uses a file-based configuration for simplicity.

**Why File-Based Configuration?**

- **Ease of Setup**: Users cloning this repository can quickly configure the bot by editing this file without needing to set up a database server or manage database connections.

- **Static Data**: The data used in this bot (such as name, skills, background) is static and does not require dynamic updates or scaling, which eliminates the need for a database.

- **Simplified Deployment**: By avoiding a database, the project is easier to deploy and run, especially for users with minimal technical expertise or limited infrastructure.

This approach demonstrates the flexibility of using the right tool for the right task.

**Security**

- The `config.py` file is included in `.gitignore`, so your personal details will not be committed to the repository, ensuring privacy and security.
- Since no database is utilized and no chat memory service feature has been added, the chat will have no history and no user interactions will be recorded.