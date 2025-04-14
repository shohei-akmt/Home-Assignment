# Take-Home-Assignment

## 🚀 Usage

### Prerequisites
* Docker must be installed

### Execution Steps

1.  **Build the Docker image:**
    Execute the following command in the project's root directory (where the `Dockerfile` is located):

    ```bash
    docker build -t load-checker-api .
    ```

2.  **Run the Docker container:**
    Run the container using the built image:

    ```bash
    docker run --rm -p 8000:8000 load-checker-api
    ```
    * `-p 8000:8000`: Maps port 8000 of the host machine to port 8000 of the container.
    * `--rm`: Automatically removes the container when it stops.
    * If you want to run it in the background, add the `-d` option (`docker run -d --rm ...`).

3.  **Access the API:**
    Once the container is running, you can access the following URLs:
    * **API Documentation (Swagger UI):** `http://localhost:8000/docs`
    * **Example API Endpoint:** `http://localhost:8000/loads/REF09460` (Specify a `reference_number` found in the CSV file)


## ✅ ToDo List　

### 📦 Environment
- [x] Research FMCSA API specifications and authentication methods

### 🔧 REST API (Load Checker) Development
- [x] Create API skeleton with FastAPI ~~or Flask~~
- [x] Implement CSV file reading and search functionality
- [x] Create `/loads/{reference_number}` endpoint
- [x] Handle responses for 404 errors and invalid input
    - [ ] Write the validation logic out of main.py
- [ ] Implement API key authentication (Optional/Bonus)
- [x] Create Dockerfile and verify local operation
- [ ] Deploy to the cloud (e.g., Render, AWS, Vercel)

