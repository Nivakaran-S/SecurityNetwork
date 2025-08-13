# 🛡️ Network Security Threat Detection

A **machine learning–driven** network security monitoring system designed to **detect potential threats** by analyzing incoming network activity data.  
The project follows a **component-based modular architecture** to ensure scalability, maintainability, and ease of integration with other systems.

It uses **FastAPI** for serving prediction and training endpoints, **MongoDB** for data storage, and **MLflow** to track model training metrics and versions.

---

## 📌 Features

- **Modular ML Pipeline**  
  Separate components for:
  - Data Ingestion  
  - Data Validation  
  - Data Transformation  
  - Model Training

- **API Endpoints with FastAPI**  
  - `/train` → Triggers the ML pipeline for training.  
  - `/predict` → Upload a CSV file and get predictions with threat classification.

- **Database Integration**  
  - Uses MongoDB to store ingested network security data.
  - Configurable connection via environment variables.

- **MLflow Integration**  
  - Tracks experiments, metrics, and models during training.
  - Ensures reproducibility and easier model comparison.

- **CORS Enabled**  
  Fully accessible from different frontend applications.

- **Preprocessor & Model Persistence**  
  - Saves trained preprocessor and model objects as `.pkl` files.
  - Reloads them at prediction time for consistent data handling.

---

## 🏗️ Project Structure
```bash

networksecurity/
│
├── components/ # Core pipeline components
│ ├── data_ingestion.py
│ ├── data_validation.py
│ ├── data_transformation.py
│ └── model_trainer.py
│
├── constants/ # Static configuration constants
│
├── entity/ # Configuration and artifact entities
│
├── exception/ # Custom exception handling
│
├── logging/ # Centralized logging setup
│
├── pipeline/ # Orchestration for full training run
│ └── training_pipeline.py
│
├── utils/ # Utility functions (ML, file handling)
│
templates/
│ └── table.html # HTML template for prediction output
final_model/
│ ├── model.pkl # Trained ML model
│ └── preprocessor.pkl # Data transformation pipeline
prediction_output/
│ └── output.csv # CSV with predictions

```

---

## ⚙️ Tech Stack

- **Programming Language:** Python
- **Frameworks & Libraries:**  
  - FastAPI  
  - Pandas  
  - scikit-learn  
  - pymongo  
  - MLflow
- **Database:** MongoDB
- **Environment Management:** python-dotenv
- **Model Tracking:** MLflow
- **Web Templating:** Jinja2
- **Deployment Ready:** Uvicorn ASGI server

---

## 🚀 How It Works

1. **Training Phase**
   - Data is ingested from MongoDB.
   - Data validation checks for schema and quality.
   - Data is transformed and preprocessed.
   - Model is trained and tracked via **MLflow**.
   - Trained model and preprocessor are saved locally.

2. **Prediction Phase**
   - User uploads a `.csv` file through `/predict` endpoint.
   - Data is transformed using the saved preprocessor.
   - Predictions are generated using the trained model.
   - Results are displayed as an HTML table and saved as `prediction_output/output.csv`.

---

## 📂 API Endpoints

| Method | Endpoint    | Description |
|--------|------------|-------------|
| GET    | `/`         | Redirects to FastAPI docs |
| GET    | `/train`    | Triggers model training pipeline |
| POST   | `/predict`  | Upload CSV for predictions |

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```bash

git clone https://github.com/Nivakaran-S/SecurityNetwork.git
cd <your-project-folder>

```

### 2️⃣ Create a virtual environment

```bash

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

```

### 3️⃣ Install dependencies

```bash

pip install -r requirements.txt

```

### 4️⃣ Set up environment variables
Create a .env file in the project root:

```bash

MONGODB_URL_KEY=<your-mongodb-connection-string>

```
### 5️⃣ Run the application

```bash

python app.py

```

The API will be available at:

```bash

http://0.0.0.0:8000

```

You can explore interactive documentation at:

```bash

http://0.0.0.0:8000/docs

```

## 📊 MLflow Usage
1. Start MLflow Tracking UI:

```bash

mlflow ui

```

2. Open in browser:

```bash

http://127.0.0.1:5000

```

3. View experiments, compare metrics, and download models.

## 📌 Example Prediction Flow
1. Send a POST request to /predict with a CSV file.

2. The server:
- Loads saved preprocessor and model.
- Generates predictions.
- Returns results as an HTML table.

3. Output is also stored in prediction_output/output.csv.

## 🛡️ Error Handling
- All exceptions are wrapped in a custom NetworkSecurityException class.
- Detailed logs are maintained for debugging.
- Failures in any pipeline stage are reported clearly.

