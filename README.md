# Introduction to Financial Markets (IFTE0001)

**Intro:** This prject introduces a dynamic and scalable end-to-end software solution that optimises carbon emissions data retrieval by reporting scope 1 and scope 2 emissions directly sourced from latest ESG reports. The goal of this prototype is to bring transparency and standardisation to ESG reporting by providing robust and low-cost emissions tracking infrastructure, making data retrieval faster and more accessible for investors and portfolio managers looking to incorporate ESG factors into financial decision making. The product aims to overcome the limitations and challenges concerning current ESG reporting ecosystems and contribute to effective climate-related risk management.

**Contributors:** [Iman Zafar](iman.zafar.24@ucl.ac.uk), [Balazs Bellus](balazs.bellus.24@ucl.ac.uk), [Esther Agossa](esther.agossa.24@ucl.ac.uk), [Saif Alarifi](saif.alarifi.24@ucl.ac.uk), [Aadhira Chavan](aadhira.chavan.24@ucl.ac.uk), [Neil Andreson](neil.anderson.24@ucl.ac.uk), [Kaitlinn Boisse](kaitlinn.boisse.24@ucl.ac.uk)


## Running the App

To set up a local instance of the app, follow these instructions carefully to ensure the environment is configured correctly. A local instance runs on your personal computer, allowing you to interact with the app in isolation.


### Prerequisites

- **Python Environment:** Create a virtual environment using Python 3.10.0 or higher. This ensures that your local environment is isolated and does not interfere with other projects.
  
- **Dependencies:** Install the necessary dependencies by running the command:
  ```bash
  pip install -r requirements.txt
  ```
  This will install all the required packages listed in the `requirements.txt` file, ensuring that your app has all the necessary libraries to run smoothly.

- **Environment Variables:** Create a `.env` file in the root directory of the project. This file will store sensitive information such as API keys and other configuration settings. You can use the `.env.template` file as a starting point and fill in the necessary values.

### Invoking the App
1. Activate your python environment. Below are some sample commands for different environment management tools:
  ```bash
  # For conda
  conda activate <your_environment_name>
  # For pyenv
  pyenv activate <your_environment_name>
  ```

2. Trigger the main script from the root directory:
  ```bash
  python src/main.py
  ```
