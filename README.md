# Solar Data Discovery: Week 0 Challenge

With an emphasis on solar farm data analysis for Benin, Sierra Leone, and Togo, this repository includes the setup and analysis for the 10 Academy AIM Week 0 Challenge: Solar Data Discovery.

# Reproducing the Environment

To set up the development environment locally, follow these steps:

# Clone the Repository:

           ```bash
           git clone https://github.com/your-username/solar-challenge-week1.git

           cd solar-challenge-week1

# Create and Activate a Virtual Environment: 

python -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install Dependencies: 

pip install -r requirements.txt

# Verify Setup:
Check Python version: python --version
Ensure dependencies are installed: pip list
Git Workflow:
Create a branch for your work: git checkout -b <branch-name>
Commit changes and push: git commit -m "message" and git push origin <branch-name>

# Project Structure

├── .vscode/                # VS Code settings
├── .github/workflows/      # GitHub Actions workflows (CI and unit tests)
├── src/                    # Source code
├── notebooks/              # Jupyter notebooks for EDA
├── tests/                  # Unit tests
├── scripts/                # Utility scripts
├── .gitignore              # Ignored files (e.g., data/, *.csv)
├── requirements.txt        # Python dependencies
├── README.md               # This file

# Replace `your-username` with your GitHub username.

**Save and Commit:**

```bash

git add README.md

git commit -m "docs: update README with environment setup instructions"

git push origin setup-task

