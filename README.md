# GitHub Actions Practice Guide for Beginners

## Introduction

This guide will help you learn GitHub Actions from scratch using Visual Studio Code and a simple Python calculator as an example project. No prior knowledge of GitHub Actions is required!

## What You'll Learn

- What GitHub Actions is and why it's useful
- How to create your first workflow
- How to run automated tests on your code
- How to view workflow results
- Advanced workflow patterns and optimization techniques

## Prerequisites

Before starting, make sure you have:

1. **Visual Studio Code** installed
2. **Git** installed on your computer
3. **Python 3.x** installed
4. A **GitHub account**

## What is GitHub Actions?

GitHub Actions is an automation tool built into GitHub that helps you automatically test, build, and deploy your code. Think of it as a robot that runs your code every time you make changes, checking that everything still works correctly.

### Key Concepts

- **Workflow**: An automated process that runs when something happens (like pushing code)
- **Event**: Something that triggers a workflow (like a push or pull request)
- **Job**: A set of steps that run on the same machine
- **Step**: An individual task (like running a test or checking out code)
- **Runner**: A server that runs your workflows (GitHub provides these for free)

---

## Part 1: Setting Up Your Project

### Step 1: Create a New Project Folder

1. Open Visual Studio Code
2. Create a new folder called `python-calculator`
3. Open this folder in VS Code (File → Open Folder)

### Step 2: Create the Calculator Code

Create a file called `calculator.py` and add this code:

```python
# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

This is our simple calculator with four basic operations.

### Step 3: Create Tests for the Calculator

Create a file called `test_calculator.py`:

```python
# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1

def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Test division function."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)
```

These tests verify that our calculator functions work correctly.

### Step 4: Create a Requirements File

Create a file called `requirements.txt`:

```
pytest==7.4.3
```

This tells Python which packages we need to install.

### Step 5: Test Locally (Optional but Recommended)

Before setting up GitHub Actions, let's make sure everything works on your computer:

1. Open the terminal in VS Code (Terminal → New Terminal)
2. Install pytest:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:
   ```bash
   pytest
   ```

You should see all tests pass! ✅

---

## Part 2: Setting Up GitHub Actions

### Step 6: Initialize Git Repository

In the VS Code terminal, run these commands:

```bash
git init
git add .
git commit -m "Initial commit: Add calculator and tests"
```

### Step 7: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the **+** icon in the top right
3. Select **New repository**
4. Name it `python-calculator`
5. Keep it **Public**
6. Click **Create repository**

### Step 8: Connect Your Local Project to GitHub

In the VS Code terminal, run these commands (replace `YOUR-USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR-USERNAME/python-calculator.git
git branch -M main
git push -u origin main
```

### Step 9: Create the Workflows Folder

Now comes the important part! GitHub Actions looks for workflows in a specific location.

1. In VS Code, create a folder structure: `.github/workflows`
   - Create a folder named `.github`
   - Inside `.github`, create a folder named `workflows`

**Tip**: In VS Code, you can create both folders at once by typing `.github/workflows` when creating a new folder.

### Step 10: Create Your First Workflow File

Inside the `.github/workflows` folder, create a file called `test.yml`:

```yaml
# .github/workflows/test.yml

name: Run Tests

# This workflow runs when you push code or create a pull request
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# Jobs are the work that gets done
jobs:
  test:
    name: Test Calculator
    runs-on: ubuntu-latest
    
    steps:
      # Step 1: Get the code from your repository
      - name: Checkout code
        uses: actions/checkout@v4
      
      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      # Step 4: Run the tests
      - name: Run pytest
        run: pytest -v
```

### Understanding the Workflow File

Let's break down what each part does:

- **`name`**: A friendly name for your workflow that appears in GitHub
- **`on`**: Defines when the workflow runs
  - `push`: Runs when you push code to the main branch
  - `pull_request`: Runs when someone creates a pull request
- **`jobs`**: The work to be done
  - `test`: The name of our job
  - `runs-on: ubuntu-latest`: Uses Ubuntu Linux (a free runner provided by GitHub)
- **`steps`**: Individual tasks that run in order
  - Each step has a `name` (what it does)
  - `uses`: Uses a pre-built action from the GitHub Marketplace
  - `run`: Runs a command in the terminal

---

## Part 3: Running Your First Workflow

### Step 11: Push Your Workflow to GitHub

In the VS Code terminal:

```bash
git add .
git commit -m "Add GitHub Actions workflow"
git push
```

### Step 12: View Your Workflow in Action

1. Go to your repository on GitHub
2. Click on the **Actions** tab at the top
3. You should see your workflow running!
4. Click on the workflow run to see details
5. Click on the "Test Calculator" job to see each step

🎉 Congratulations! You've just created your first GitHub Actions workflow!

---

## Part 4: Understanding the Results

### What to Look For

In the Actions tab, you'll see:

- ✅ **Green checkmark**: All tests passed!
- ❌ **Red X**: Something failed
- 🟡 **Yellow dot**: Workflow is currently running

### Viewing Detailed Logs

Click on any step to see detailed logs of what happened. This is super useful for debugging if something goes wrong.

---

## Part 5: Practice Exercises

Now that you have a working workflow, try these exercises:

### Exercise 1: Break a Test

1. Change one of the functions in `calculator.py` to return the wrong value
2. Push your changes
3. Watch the workflow fail
4. Fix the function and push again
5. Watch it pass!

### Exercise 2: Add a New Function

1. Add a `power(a, b)` function to `calculator.py` that returns `a ** b`
2. Add a `test_power()` function to `test_calculator.py`
3. Push your changes
4. Watch the workflow run with your new test

### Exercise 3: Test Multiple Python Versions

Modify your workflow to test with multiple Python versions:

```yaml
jobs:
  test:
    name: Test Calculator
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run pytest
        run: pytest -v
```

This will run your tests on four different Python versions!

---

# INTERMEDIATE SECTION

## Part 6: Advanced Workflow Patterns

Now that you're comfortable with basic workflows, let's explore more advanced techniques that will make your CI/CD pipelines more powerful and efficient.

---

## 6.1 Caching Dependencies

Every time your workflow runs, it downloads and installs dependencies from scratch. This takes time! Caching lets you save dependencies between runs, speeding up your workflows significantly.

### Why Cache?

- **Faster builds**: Skip downloading the same packages over and over
- **Cost savings**: Reduce workflow execution time
- **Better experience**: Get feedback faster

### Add Caching to Your Workflow

Update your `test.yml` file to include caching:

```yaml
name: Run Tests with Caching

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Test Calculator
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      # Cache pip dependencies
      - name: Cache pip packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run pytest
        run: pytest -v
```

### Understanding the Cache Configuration

- **`path`**: Where pip stores downloaded packages (`~/.cache/pip`)
- **`key`**: A unique identifier for the cache
  - `${{ runner.os }}`: Operating system (ubuntu-latest)
  - `hashFiles('**/requirements.txt')`: Creates a hash of your requirements file
  - When requirements.txt changes, a new cache is created
- **`restore-keys`**: Fallback keys if exact match isn't found

### Testing the Cache

1. Push your updated workflow
2. First run will take normal time and create the cache
3. Second run will use the cache - watch it be much faster!

Look for "Cache restored successfully" in the logs to confirm it's working.

---

## 6.2 Using Environment Variables and Secrets

Sometimes your code needs configuration values or sensitive information like API keys. Never commit secrets to your repository!

### Create a Configuration File

Add a new file `config.py`:

```python
# config.py
import os

# Get configuration from environment variables
API_KEY = os.getenv('API_KEY', 'default-key-for-local-testing')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///local.db')
DEBUG_MODE = os.getenv('DEBUG_MODE', 'true').lower() == 'true'
```

### Update Calculator to Use Config

Modify `calculator.py` to demonstrate using environment variables:

```python
# calculator.py
import os

DEBUG = os.getenv('DEBUG_MODE', 'false').lower() == 'true'

def add(a, b):
    """Return the sum of two numbers."""
    result = a + b
    if DEBUG:
        print(f"DEBUG: {a} + {b} = {result}")
    return result

def subtract(a, b):
    """Return the difference of two numbers."""
    result = a - b
    if DEBUG:
        print(f"DEBUG: {a} - {b} = {result}")
    return result

def multiply(a, b):
    """Return the product of two numbers."""
    result = a * b
    if DEBUG:
        print(f"DEBUG: {a} × {b} = {result}")
    return result

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    if DEBUG:
        print(f"DEBUG: {a} ÷ {b} = {result}")
    return result
```

### Add Secrets to GitHub

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add a secret:
   - Name: `API_KEY`
   - Value: `test-api-key-12345`
5. Click **Add secret**

### Use Secrets in Your Workflow

Update `test.yml` to use environment variables:

```yaml
name: Run Tests with Secrets

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Test Calculator
    runs-on: ubuntu-latest
    
    # Set environment variables for the entire job
    env:
      DEBUG_MODE: 'true'
      DATABASE_URL: 'sqlite:///test.db'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Cache pip packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      # Run tests with secrets
      - name: Run pytest
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: pytest -v
```

### Important Security Notes

- Secrets are **masked** in logs (they show as `***`)
- Never print secrets directly
- Secrets are only available to workflows in the same repository
- Forked repositories don't have access to your secrets

---

## 6.3 Job Dependencies and Artifacts

As your project grows, you might want to split work into multiple jobs that depend on each other and share files.

### Creating Multiple Jobs

Update your workflow to have separate build and test jobs:

```yaml
name: Build and Test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  # Job 1: Build and package
  build:
    name: Build Package
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install build tools
        run: pip install build
      
      - name: Build distribution packages
        run: python -m build
      
      # Upload the built package as an artifact
      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: python-package
          path: dist/
          retention-days: 7
  
  # Job 2: Test (depends on build)
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    needs: build  # This job waits for 'build' to complete
    
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Cache pip packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run pytest
        run: pytest -v -s
  
  # Job 3: Deploy (depends on test)
  deploy:
    name: Deploy Package
    runs-on: ubuntu-latest
    needs: test  # This job waits for all 'test' jobs to complete
    if: github.ref == 'refs/heads/main'  # Only deploy on main branch
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      # Download the artifact from the build job
      - name: Download build artifacts
        uses: actions/download-artifact@v4
        with:
          name: python-package
          path: dist/
      
      - name: Display downloaded files
        run: ls -la dist/
      
      - name: Simulate deployment
        run: echo "Deploying package to production..."
```

### Understanding Job Dependencies

- **`needs`**: Specifies which jobs must complete before this job runs
- **`needs: build`**: Single dependency
- **`needs: [build, test]`**: Multiple dependencies
- Jobs run in **parallel** by default unless you specify dependencies

### Understanding Artifacts

- **Upload artifacts**: Save files from one job to use in another
- **Download artifacts**: Retrieve files uploaded by previous jobs
- **Retention**: Artifacts are kept for a specified number of days (default: 90, max: 400)
- **Use cases**: Build outputs, test reports, logs, compiled binaries

### Create the Setup File for Building

To make the build job work, create a `pyproject.toml` file:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "simple-calculator"
version = "0.1.0"
description = "A simple calculator for learning GitHub Actions"
authors = [{name = "Your Name"}]
requires-python = ">=3.9"

[tool.setuptools]
py-modules = ["calculator"]
```

---

## 6.4 Advanced Matrix Strategies

You've already used a simple matrix for Python versions. Let's explore more advanced matrix configurations.

### Matrix with Multiple Dimensions

```yaml
name: Cross-Platform Testing

on:
  push:
    branches: [ main ]

jobs:
  test:
    name: Test on ${{ matrix.os }} with Python ${{ matrix.python-version }}
    runs-on: ${{ matrix.os }}
    
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.9', '3.11', '3.12']
      fail-fast: false  # Continue running even if one job fails
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run pytest
        run: pytest -v
```

This creates **9 jobs** (3 operating systems × 3 Python versions)!

### Matrix with Include and Exclude

Sometimes you want to add specific combinations or exclude certain ones:

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.9', '3.11', '3.12']
        
        # Exclude specific combinations
        exclude:
          - os: macos-latest
            python-version: '3.9'
        
        # Include additional specific combinations
        include:
          - os: ubuntu-latest
            python-version: '3.13-dev'
            experimental: true
      
      fail-fast: false
    
    # Allow experimental jobs to fail without failing the workflow
    continue-on-error: ${{ matrix.experimental == true }}
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run pytest
        run: pytest -v
```

### Understanding Matrix Options

- **`fail-fast: false`**: All matrix jobs run even if one fails (default is `true`)
- **`exclude`**: Remove specific combinations from the matrix
- **`include`**: Add specific combinations with custom variables
- **`continue-on-error`**: Allow specific jobs to fail without failing the entire workflow
- **`max-parallel`**: Limit how many matrix jobs run simultaneously

---

## 6.5 Reusable Workflows

As you create more projects, you'll want to reuse workflow logic across repositories.

### Create a Reusable Workflow

Create `.github/workflows/reusable-test.yml`:

```yaml
name: Reusable Test Workflow

on:
  workflow_call:  # Special trigger for reusable workflows
    inputs:
      python-version:
        description: 'Python version to use'
        required: false
        type: string
        default: '3.11'
      test-command:
        description: 'Command to run tests'
        required: false
        type: string
        default: 'pytest -v'
    secrets:
      API_KEY:
        required: false
    outputs:
      test-result:
        description: 'Test execution result'
        value: ${{ jobs.test.outputs.result }}

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    outputs:
      result: ${{ steps.test-step.outcome }}
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
      
      - name: Cache pip packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run tests
        id: test-step
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: ${{ inputs.test-command }}
```

### Call the Reusable Workflow

Create a new workflow `.github/workflows/use-reusable.yml`:

```yaml
name: Use Reusable Workflow

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  # Call the reusable workflow with default settings
  test-default:
    uses: ./.github/workflows/reusable-test.yml
    secrets:
      API_KEY: ${{ secrets.API_KEY }}
  
  # Call the reusable workflow with custom settings
  test-custom:
    uses: ./.github/workflows/reusable-test.yml
    with:
      python-version: '3.12'
      test-command: 'pytest -v --cov'
    secrets:
      API_KEY: ${{ secrets.API_KEY }}
  
  # Use the output from reusable workflow
  report:
    needs: test-default
    runs-on: ubuntu-latest
    steps:
      - name: Display test result
        run: echo "Test result was ${{ needs.test-default.outputs.test-result }}"
```

### Benefits of Reusable Workflows

- **Consistency**: Same testing logic across all projects
- **Maintainability**: Update once, applies everywhere
- **Modularity**: Break complex workflows into manageable pieces
- **Sharing**: Can even call reusable workflows from other repositories

---

## Part 7: Intermediate Practice Exercises

Now it's time to practice what you've learned!

### Exercise 4: Add Coverage Reporting

1. Add `pytest-cov` to `requirements.txt`:
   ```
   pytest==7.4.3
   pytest-cov==4.1.0
   ```

2. Create a coverage step in your workflow:
   ```yaml
   - name: Run tests with coverage
     run: pytest -v --cov=calculator --cov-report=term-missing
   
   - name: Upload coverage artifact
     uses: actions/upload-artifact@v4
     with:
       name: coverage-report
       path: .coverage
   ```

3. Push and view the coverage report in your workflow logs

### Exercise 5: Create a Linting Job

1. Add `flake8` to `requirements.txt`

2. Create a new job in your workflow:
   ```yaml
   lint:
     name: Code Linting
     runs-on: ubuntu-latest
     
     steps:
       - uses: actions/checkout@v4
       
       - name: Set up Python
         uses: actions/setup-python@v5
         with:
           python-version: '3.11'
       
       - name: Install flake8
         run: pip install flake8
       
       - name: Run linter
         run: flake8 calculator.py test_calculator.py --max-line-length=100
   ```

3. Make the test job depend on successful linting:
   ```yaml
   test:
     needs: lint
     # ... rest of test job
   ```

### Exercise 6: Conditional Deployment

Create a workflow that only deploys when:
- All tests pass
- The push is to the `main` branch
- It's not a pull request

```yaml
deploy:
  name: Deploy to Production
  needs: [lint, test]
  runs-on: ubuntu-latest
  if: |
    github.ref == 'refs/heads/main' &&
    github.event_name == 'push' &&
    success()
  
  steps:
    - name: Simulate deployment
      run: |
        echo "Deploying to production..."
        echo "Environment: Production"
        echo "Version: ${{ github.sha }}"
```

### Exercise 7: Create a Matrix for Test Scenarios

Test your calculator with different scenarios:

```yaml
test-scenarios:
  name: Test ${{ matrix.scenario }}
  runs-on: ubuntu-latest
  
  strategy:
    matrix:
      scenario:
        - name: 'basic-operations'
          marker: 'not slow'
        - name: 'edge-cases'
          marker: 'edge'
        - name: 'performance'
          marker: 'slow'
  
  steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest-benchmark
    
    - name: Run ${{ matrix.scenario.name }} tests
      run: pytest -v -m "${{ matrix.scenario.marker }}"
```

(You'll need to add markers to your tests for this to work!)

---

## Part 8: Workflow Best Practices

### Performance Tips

1. **Use caching** for dependencies
2. **Parallelize jobs** when possible
3. **Use matrix strategies** efficiently
4. **Fail fast** when appropriate
5. **Cache Docker layers** for container-based workflows

### Security Best Practices

1. **Never commit secrets** to your repository
2. **Use repository secrets** for sensitive data
3. **Limit secret scope** (use environment secrets when possible)
4. **Review third-party actions** before using them
5. **Pin action versions** to specific commits for stability
   ```yaml
   uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab  # v4.1.0
   ```

### Maintainability Tips

1. **Name your workflows clearly**
2. **Add comments** to explain complex logic
3. **Use reusable workflows** for common patterns
4. **Keep workflows DRY** (Don't Repeat Yourself)
5. **Document required secrets** in README
6. **Set appropriate artifact retention** periods

### Debugging Tips

1. **Enable debug logging**:
   - Go to Settings → Secrets
   - Add `ACTIONS_STEP_DEBUG` = `true`

2. **Use conditional steps for debugging**:
   ```yaml
   - name: Debug information
     if: runner.debug == '1'
     run: |
       echo "Runner OS: ${{ runner.os }}"
       echo "Python version: ${{ matrix.python-version }}"
       env
   ```

3. **Add verbose flags** to commands:
   ```yaml
   run: pytest -vv -s  # Very verbose with print output
   ```

---

## Part 9: Common Workflow Patterns

### Pattern 1: Manual Workflow Triggers

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy to'
        required: true
        type: choice
        options:
          - development
          - staging
          - production
      version:
        description: 'Version to deploy'
        required: true
        type: string

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to ${{ inputs.environment }}
        run: |
          echo "Deploying version ${{ inputs.version }}"
          echo "Target: ${{ inputs.environment }}"
```

### Pattern 2: Scheduled Workflows

```yaml
on:
  schedule:
    - cron: '0 2 * * 1'  # Every Monday at 2 AM UTC
  workflow_dispatch:  # Also allow manual trigger

jobs:
  weekly-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run weekly security scan
        run: echo "Running security scan..."
      
      - name: Update dependencies
        run: echo "Checking for dependency updates..."
```

### Pattern 3: Conditional Steps

```yaml
steps:
  - name: Run only on main branch
    if: github.ref == 'refs/heads/main'
    run: echo "This is the main branch"
  
  - name: Run only on pull requests
    if: github.event_name == 'pull_request'
    run: echo "This is a pull request"
  
  - name: Run only on failure
    if: failure()
    run: echo "Previous step failed"
  
  - name: Always run (even on failure)
    if: always()
    run: echo "This always runs"
```

### Pattern 4: Dynamic Matrix from JSON

```yaml
jobs:
  generate-matrix:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - name: Generate matrix
        id: set-matrix
        run: |
          echo 'matrix={"python-version":["3.9","3.10","3.11"],"os":["ubuntu-latest"]}' >> $GITHUB_OUTPUT
  
  test:
    needs: generate-matrix
    runs-on: ${{ matrix.os }}
    strategy:
      matrix: ${{ fromJSON(needs.generate-matrix.outputs.matrix) }}
    steps:
      - uses: actions/checkout@v4
      - name: Test with Python ${{ matrix.python-version }}
        run: echo "Testing..."
```

---

## Part 10: Troubleshooting Guide

### Common Issues and Solutions

#### Issue 1: Cache Not Working

**Symptom**: Workflow always misses cache

**Solutions**:
- Verify the `path` is correct for your OS
- Check that `key` changes when dependencies change
- Ensure `restore-keys` are properly set
- Cache size limit is 10GB per repository

#### Issue 2: Secrets Not Available

**Symptom**: Workflow shows empty values for secrets

**Solutions**:
- Verify secret is created in correct location (repo/environment)
- Check secret name matches exactly (case-sensitive)
- Ensure workflow has permission to access environment secrets
- Remember: forked repos don't have access to secrets

#### Issue 3: Artifact Not Found

**Symptom**: Download artifact fails with "Artifact not found"

**Solutions**:
- Verify upload and download use the same artifact name
- Check that upload completed successfully
- Ensure jobs are properly linked with `needs`
- Artifacts expire based on retention settings

#### Issue 4: Matrix Jobs Failing

**Symptom**: Some matrix combinations fail unexpectedly

**Solutions**:
- Use `fail-fast: false` to see all failures
- Add `continue-on-error` for experimental combinations
- Check if certain OS/version combinations are incompatible
- Review logs for each specific failure

#### Issue 5: Workflow Not Triggering

**Symptom**: Workflow doesn't run when expected

**Solutions**:
- Verify the trigger event matches (push, pull_request, etc.)
- Check branch names in `on.push.branches`
- Ensure YAML syntax is correct (use a validator)
- Check workflow file is in `.github/workflows/` directory
- Verify workflow is enabled in repository settings

---

## Summary

You've now learned:

### **Beginner Level**
✅ What GitHub Actions is and how it works  
✅ How to create a workflow file  
✅ How to run automated tests  
✅ How to view and interpret workflow results  
✅ Basic matrix strategies

### **Intermediate Level**
✅ Dependency caching for faster builds  
✅ Environment variables and secrets management  
✅ Job dependencies and artifact sharing  
✅ Advanced matrix strategies with include/exclude  
✅ Reusable workflows for code reuse  
✅ Conditional execution and manual triggers  
✅ Performance optimization techniques  
✅ Security best practices  
✅ Common workflow patterns

### **Next Steps**

Ready to go even further? Explore:

1. **Advanced Topics**:
   - Container-based workflows
   - Self-hosted runners
   - GitHub Packages integration
   - Deployment environments with protection rules

2. **Real-World Applications**:
   - Multi-service deployments
   - Database migrations
   - End-to-end testing
   - Automated releases and changelogs

3. **Integration & Tools**:
   - Slack/Discord notifications
   - Code quality tools (SonarQube, CodeClimate)
   - Security scanning (Snyk, Dependabot)
   - Performance monitoring

---

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Awesome Actions (Community List)](https://github.com/sdras/awesome-actions)
- [GitHub Actions Cheat Sheet](https://github.github.io/actions-cheat-sheet/)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)

---

## Conclusion

GitHub Actions is a powerful tool that grows with your needs. You started with simple test automation and now understand sophisticated CI/CD patterns. The key is to start simple and gradually add complexity as your requirements evolve.

**Remember**: Every expert was once a beginner. Keep experimenting, make mistakes, learn from them, and soon you'll be creating sophisticated automation pipelines with confidence!

Happy automating! 🚀