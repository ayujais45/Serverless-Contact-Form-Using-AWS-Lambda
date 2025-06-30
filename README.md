# Serverless-Contact-Form-Using-AWS-Lambda

A fully serverless contact form built using:

- **AWS Lambda (Python)**
- **API Gateway (HTTP API)**
- **DynamoDB** for storing messages
- **HTML + JavaScript frontend**

---

## 🚀 How It Works

✅ User submits a form on the frontend  
✅ JavaScript sends a POST request to API Gateway  
✅ API Gateway triggers a Lambda function  
✅ Lambda stores the data into DynamoDB  
✅ Response is returned to the frontend

---

## 🗂 Project Structure

<pre><code>
/serverless-contact-form
│
├── index.html # Frontend HTML form
├── lambda_function.py # AWS Lambda Python code
└── README.md # Project documentation

</code></pre>
