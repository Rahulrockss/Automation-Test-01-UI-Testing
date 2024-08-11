# Automated UI Testing for Multiple Browsers and Resolutions

This project automates UI testing across multiple browsers and screen resolutions using Selenium WebDriver. The script checks for basic faults like page title mismatches, missing elements, broken links, and JavaScript errors. It also takes screenshots of web pages for different resolutions and saves them in a structured directory.

## Features

* **Cross-Browser Testing**: Tests are run on Chrome, Firefox, and Safari.
* **Multiple Resolutions**: Supports testing on common desktop and mobile resolutions.
* **Fault Detection**: Checks for:
  * Page title validation
  * Presence of key elements
  * Broken links
  * JavaScript errors in the browser console
* **Screenshots**: Takes full-page screenshots and organizes them by browser, resolution, and timestamp.

## Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3.x**: The script is written in Python.
* **pip**: Python package manager to install dependencies.

### Browser Requirements

* **Chrome**: Latest version installed.
* **Firefox**: Latest version installed. Download it [here](https://www.mozilla.org/firefox/).
* **Safari**: Pre-installed on macOS. For macOS users, ensure `Remote Automation` is enabled in Safari.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install Dependencies**: Install the required Python packages using `pip`.
    ```bash
    pip install selenium webdriver-manager
    ```

3. **Enable Safari’s Remote Automation** (macOS Only):
    * Open Safari and go to `Safari > Preferences > Advanced`.
    * Check "Show Develop menu in menu bar".
    * Then go to `Develop > Allow Remote Automation`.

## Usage

1. **Configure the Script**:
    * Open the script file (`resolution_test.py`) and update the `urls` list with the URLs you want to test.
    * Update the `expected_title` variable with the correct page title for validation.

2. **Run the Script**: Execute the script in your Python environment:
    ```bash
    python resolution_test.py
    ```

3. **Check the Results**:
    * **Screenshots**: Screenshots will be saved in a structured directory under the root folder. Example structure:
        ```bash
        Chrome/Desktop_1920x1080/example.com/20240811-101010/screenshot.png
        Firefox/Mobile_360x640/example.com/20240811-101010/screenshot.png
        Safari/Desktop_1366x768/example.com/20240811-101010/screenshot.png
        ```
    * **Fault Logs**: The script will print any faults found during the test to the console. Review these logs to identify issues.

## Customization

* **Adding More Browsers**: You can add support for additional browsers by configuring their WebDriver and adding them to the `perform_test` function.
* **Additional Fault Checks**: Modify the `check_faults` function to include more comprehensive checks based on your needs.
* **Resolutions**: Customize the `resolutions` dictionary to include or remove screen resolutions.

## Troubleshooting

* **NoSuchDriverException**: Ensure the respective browsers (Chrome, Firefox, Safari) are installed and updated.
* **SafariDriver Issues**: Ensure `Remote Automation` is enabled in Safari on macOS.
* **JavaScript Errors**: If the console log capture doesn't work in Safari, consider testing with Chrome or Firefox where this feature is supported.

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
