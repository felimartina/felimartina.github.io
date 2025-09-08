# Snapshot Script

This script uses Playwright to take a screenshot of the trip timeline.

## Installation

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Install the Playwright browsers:
    ```bash
    playwright install
    ```

## Usage

1.  Start a local web server in the root directory of the project:
    ```bash
    python3 -m http.server
    ```
2.  Run the script:
    ```bash
    python scripts/take-screenshot.py
    ```
    This will save a screenshot named `timeline.png` in the root directory.

    You can also specify a different output file:
    ```bash
    python scripts/take-screenshot.py --output my-screenshot.png
    ```
