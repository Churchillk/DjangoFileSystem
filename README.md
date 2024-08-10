# Django Project Generator

Welcome to the Django Project Generator! This utility script automates the creation of a new Django project and app structure, and prepares it for development with a few custom settings. It's designed to simplify the initial setup and configuration of Django projects, making it easier for developers to get started quickly.

## Features

- **Automatic Project Creation**: Generates a new Django project with the specified name.
- **App Initialization**: Creates `Home` and `Users` apps with basic file structures.
- **Custom Settings**: Updates Django settings to include static and media files configuration.
- **File Creation**: Automatically creates essential files like `urls.py` and `forms.py` in the newly created apps.
- **Zip Archive**: Packages the entire project into a zip file for easy distribution or backup.

## Getting Started

To use this script, you need to have Django installed and ensure that the script is executed in an environment where Django commands are available.

### Prerequisites

- Python 3.x
- Django 4.x or higher

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Churchillk/DjangoFileSystem.git
    cd DjangoFileSystem
    ```

2. **Install requirements:**

    Make sure Django is installed in your environment. If not, you can install it using pip:

    ```bash
    pip install django
    ```

### Usage

1. **Run the script:**

    Ensure your Django environment is set up correctly, then run the script to generate a new project:

    ```bash
    python path/to/your/script.py
    ```

2. **Fill out the form:**

    You’ll be prompted to enter the project name through a web form. Fill it out and submit.

3. **Download and Extract:**

    After submission, a zip file of your new Django project will be generated. Download and extract it to start working on your new project.

### Code Overview

- **Project Creation**: Uses `django-admin` to start a new project and apps.
- **Directory Setup**: Creates necessary directories and files for the `Home` and `Users` apps.
- **Settings Update**: Adds configuration for static and media files to the settings.py.
- **URL Configuration**: Updates `urls.py` with URL patterns for the new apps.
- **Packaging**: Compresses the project directory into a zip file for download.

### Contributing

If you have suggestions or improvements, feel free to open an issue or submit a pull request. Contributions are welcome!

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any inquiries, please reach out to [your-email@example.com](mailto:churchilkodhiambo@gmail.com).
