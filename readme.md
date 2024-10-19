[![Build Status](https://app.travis-ci.com/shub-garg/SWE1-app.svg?token=DxuCsKDqE3cxqKSyCKjn&branch=master)](https://app.travis-ci.com/shub-garg/SWE1-app)
[![Coverage Status](https://coveralls.io/repos/github/shub-garg/SWE1-app/badge.svg?branch=master)](https://coveralls.io/github/shub-garg/SWE1-app?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![flake8](https://img.shields.io/badge/code%20style-flake8-brightgreen.svg)](https://flake8.pycqa.org/)


# Django Poll Application

A simple web application to create and vote on polls, built with Django. This project is a step-by-step implementation following Django's official tutorial series.

![ScreenRecording2024-09-30at5 34 31AM-ezgif com-optimize](https://github.com/user-attachments/assets/d1d1a32a-2415-4158-97b4-3b6563cdd0dd)

## Table of Contents
 
 
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Deploying to AWS Elastic Beanstalk](#deploying-to-aws-elastic-beanstalk)
- [License](#license)

---

## Features

- Create new polls with multiple choices.
- Users can vote on polls and view real-time results.
- Admin panel to manage polls and choices.
- User-friendly interface with real-time voting results.

---

## Prerequisites

- Python 3.7 or higher
- Django 3.x or higher
- Virtualenv or Conda (for environment management)
- Optional: AWS CLI and AWS Elastic Beanstalk CLI for deployment

---

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/shub-garg/SWE1-app.git
   ```

2. **Navigate to the Project Directory**

   First, navigate to the root of your Django project directory where your `manage.py` file is located:

   ```bash
   cd mysite
   ```

3. **Set Up a Virtual Environment**

   Create and activate a virtual environment using either `virtualenv` or `conda`:

   - **Using `virtualenv`:**

     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

   - **Using `conda`:**

     ```bash
     conda create --name poll-env python=3.9
     conda activate poll-env
     ```

4. **Install Dependencies**

   Once the virtual environment is activated, install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Run Database Migrations**

   Before starting the server, apply the migrations to set up your database schema:

   ```bash
   python manage.py migrate
   ```

2. **Create a Superuser (for Admin Panel)**

   To access the Django admin panel, you need to create a superuser. This account will allow you to manage polls and other data in the admin interface:

   ```bash
   python manage.py createsuperuser
   ```
Follow the prompts to create a username, email, and password.

3. **Migrate the Database**

   If you haven't done so already, apply the database migrations to set up the initial database schema:

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**

   Start the Django development server by running:

   ```bash
   python manage.py runserver
   ```

5. **Access the Application**

   Once the development server is running, open your browser and navigate to:

   ```bash
    http://127.0.0.1:8000/polls/
   ```


You should now see your Django poll application up and running!

6. **Access the Admin Panel**

   To manage polls, users, and other data, you can access the Django admin panel by navigating to:

   ```bash
     http://127.0.0.1:8000/admin/
     ```

## Deploying to AWS Elastic Beanstalk

1. **Install the EB CLI**

   Install the AWS Elastic Beanstalk CLI using pip:

   ```bash
   pip install awsebcli --upgrade --user
   ```

2. **Initialize Elastic Beanstalk**

   Set up Elastic Beanstalk for deployment:

   ```bash
   eb init
   ```

Follow the prompts to configure your Elastic Beanstalk environment. During initialization, you will be asked to:

- Select the AWS region.
- Choose the application name.
- Select the platform (Python).
- Configure SSH settings (optional but recommended for accessing your EC2 instances).

3. **Deploy to Elastic Beanstalk**

   After initializing the environment, you can create and deploy your Elastic Beanstalk environment using the following command:

   ```bash
   eb create
   ```

Follow the prompts to create your environment. Once the environment is ready and all resources are provisioned, deploy your application by running:

```bash
eb deploy
```

After a successful deployment, Elastic Beanstalk will provide a URL where you can access your application.

4. **Monitor and Manage the Environment**

   You can use the Elastic Beanstalk CLI to monitor your environment, fetch logs, or make configuration changes. Here are some useful commands:

   - **Check the status of your environment**:

     ```bash
     eb status
     ```

   - **View application logs**:

     ```bash
     eb logs
     ```

     This will display logs from your application’s EC2 instances, helping you debug any issues.

   - **Open the application in your browser**:

     ```bash
     eb open
     ```

     This command will automatically open your deployed application in your default web browser.

   - **Update the environment configuration**:

     You can use the following command to update your environment with any changes you've made (e.g., to settings or configuration files):

     ```bash
     eb config
     ```

   - **Terminate the environment**:

     If you no longer need the environment and want to delete all associated resources, use:

     ```bash
     eb terminate
     ```
## Acknowledgments

This project follows the official [Django tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/). Special thanks to the Django team and community for providing such an excellent resource, which made the creation of this application possible.

We would also like to thank:

- The **open-source contributors** who maintain the Django framework and its surrounding ecosystem.
- The **AWS Elastic Beanstalk** team for simplifying the deployment process and making cloud hosting easy to manage.

---

## Contact

For any issues, questions, or feedback, feel free to reach out:

- Open a [GitHub issue](https://github.com/shub-garg/SWE1-app/issues) to report bugs or request features.
- Email me at [shubgarg17@gmail.com](mailto:shubgarg17@gmail.com) for any direct inquiries.

---

test change
