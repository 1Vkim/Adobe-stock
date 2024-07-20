# Discord Bot with Video Downloading Capability

This Discord bot is built using the `discord.py` library and includes functionality to download videos from a specified category and asset ID from Adobe Stock. The bot responds to certain commands and events, including a greeting and a video download command.

## Prerequisites

- Python 3.6+
- `discord.py` library
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or copy the code into a new directory.
2. Navigate to the directory containing the script.
3. Install the required packages using pip:

    ```sh
    pip install discord.py requests beautifulsoup4
    ```

## Usage

1. Set up your environment variable for the Discord bot token. You can do this by creating a `.env` file in the same directory as your script and adding the following line:

    ```env
    Token=YOUR_DISCORD_BOT_TOKEN_HERE
    ```

2. Run the bot:

    ```sh
    python your_script_name.py
    ```

## Bot Commands

- **Greeting Command**: The bot responds to a `$hello` command with a greeting message.
- **Download Command**: The bot can download a video using the `!download` command followed by the `asset_id` and optionally a `category`.

    ```sh
    !download [asset_id] [category]
    ```

## Example

1. Send a `$hello` message in any channel the bot has access to, and it will respond with a greeting.
2. Use the `!download` command:

    ```sh
    !download 123456 nature
    ```

    The bot will attempt to download the specified video and notify you of the status.
