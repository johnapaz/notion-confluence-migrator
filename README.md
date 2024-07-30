# Notion to Confluence Migration Tool

A Python application for migrating content from Notion to Confluence Cloud with a user-friendly graphical interface.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Requirements](#requirements)
- [Prerequisites](#prerequisites)
    - [Creating a Notion integration](#creating-a-notion-integration)
    - [Creating a Confluence Forge app](#creating-a-confluence-app)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Notion to Confluence: Transfer selected Notion pages to Confluence spaces.
- Confluence to Notion: (Currently broken; TODO: Fix this functionality).
- User Interface: A GUI that allows users to select content and destinations, with plans for a major UI overhaul.
- Content Creation: Create new Confluence spaces directly from the application.
- Security: Comprehensive security review planned.
- Cloud Deployment: Future plans include packaging this tool as a cloud service/app.
- Helper Text: Improve helper text for where to get the secrets.

## Requirements
- Python 3.7 or higher
- `python-dotenv` for handling environment variables

## Prerequisites
In order to use this app you'll need to have already:
1. Create a Notion Integration app
2. Create a Confluence app

### Creating a Notion Integration
1. Sign in to Notion: Go to Notion and sign in with your account.
2. Create an Integration:
    - Navigate to Notion Integrations.
    - Click on + New Integration. 
    - Fill in the required fields such as Name and Associated Workspace.
    - Select the necessary permissions for the integration.
    - Click Submit to create the integration.
3. Get Your Integration Token: After creating the integration, copy the Integration Token provided. This will be used in the `.env` file.

### Creating a Confluence App
1. Sign in to Atlassian: Go to Atlassian Developer and sign in with your Atlassian account.
2. Create a New App: 
    - Navigate to the Developer Console.
    - Click on Create New App.
    - Select OAuth 2.0 as the authentication method.
    - Fill in the required fields such as App Name and App Description.
3. Set Up OAuth 2.0:
    - After creating the app, navigate to the Authorization tab.
    - Add the following scopes: 
        ``` 
        read:me, write:confluence-space, read:confluence-content.permission, write:confluence-props, read:confluence-props, search:confluence, read:confluence-space.summary, write:confluence-content, read:confluence-content.
        ```
    - Add `http://localhost:8000/callback` as the Redirect URI.
    - Save the changes.

    4. Get Your Client ID and Client Secret: Go to the Credentials tab. Copy the `Client ID` and `Client Secret`. These will be used in the `.env` file.

## Directory Structure
```
notion-confluence/
├── .gitignore
├── .env.example
├── README.md
├── app.py
├── callback_server.py
├── dependency_checker.py
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_screen.py
│   │   ├── url_screen.py
│   │   ├── login_screen.py
│   │   ├── content_selection_screen.py
│   │   ├── destination_login_screen.py
│   │   ├── site_selection_screen.py
│   │   ├── space_selection_screen.py
│   │   ├── confirmation_screen.py
│   │   ├── progress_screen.py
│   │   ├── custom_dialog.py
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/johnapaz/notion-confluence.git
   cd notion-confluence 
   ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Copy the example environment file and fill in your credentials:
    ```bash
    cp .env.example .env
    ```

5. Edit the .env file and replace the placeholder values with your actual credentials.

## Environment Variables
The application uses environment variables to store sensitive information. These variables are loaded from a .env file located in the project root.

Example .env file:
```
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
REDIRECT_URI=http://localhost:8000/callback
AUTH_URL=https://auth.atlassian.com/authorize
TOKEN_URL=https://auth.atlassian.com/oauth/token
SCOPES=read:me write:confluence-space read:confluence-content.permission write:confluence-props read:confluence-props search:confluence read:confluence-space.summary write:confluence-content read:confluence-content
```

## Usage
1. Launch the application:
    ```bash
    python app.py
    ```

2. Follow the on-screen instructions to authenticate and select or create spaces in Confluence.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request. When contributing, please ensure you follow the coding standards and include appropriate tests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## TODO
These are things I hope to improve about this project:

```
# TODO: Enable Confluence >> Notion; current experience is broken
# TODO: Overhaul UI -- it's currently ugly
# TODO: Make this a cloud service/app
# TODO: Content improvements: helper text for where to get the secrets
# TODO: Security review
# TODO: Bug: Fix Notion content insertion for Create a space experience, currently does not add selected notion files into Confluence
# TODO: Add ability for Notion pages to select displaying actual page names
# TODO: Package as a downloadable asset that once downloaded can be executed from clicking, including dependency checking
```
