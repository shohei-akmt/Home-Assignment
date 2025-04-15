# Home-Assignment

## 🚀 Usage

### Prerequisites
* Docker must be installed
* You need an API Key (set as `API_KEY` environment variable)

### Execution Steps

1.  **Build the Docker image:**
    Execute the following command in the project's root directory (where the `Dockerfile` is located):

    ```bash
    docker build -t load-checker-api .
    ```

2.  **Run the Docker container:**
    Run the container using the built image, providing your API key as an environment variable.
    Replace `YOUR_SECRET_KEY` with your key.

    ```bash
    docker run --rm -p 8000:8000 -e API_KEY="YOUR_SECRET_KEY" load-checker-api
    ```
    * `-p 8000:8000`: Maps port 8000 of the host machine to port 8000 of the container.
    * `--rm`: Automatically removes the container when it stops.
    * If you want to run it in the background, add the `-d` option (`docker run -d --rm ...`).

3.  **Access the API:**
    Once the container is running, you can access the API endpoint. 
    Remember to include the API key in the `X-API-Key` header of your request.
    * **Example API Endpoint Request (using curl)::** 
    (Specify a `reference_number` found in the CSV file)

    ```bash
    curl -i -H "X-API-Key: YOUR_SECRET_KEY" http://localhost:8000/loads/REF09460
    ```


## ✅ ToDo List　

### 🔧 REST API (Load Checker) Development
- [x] Create API skeleton with FastAPI
- [x] Implement CSV file reading and search functionality
- [x] Create `/loads/{reference_number}` endpoint
- [x] Handle responses for 404 errors and invalid input
    - [x] Write the validation logic out of main.py
- [x] Return in JSON format (confirmed)
- [x] Implement API key authentication (Bonus)
- [x] Create Dockerfile and verify local operation (Bonus)
- [x] Deploy to the cloud (e.g., Render, AWS, Vercel)
    - AWS App Runner
