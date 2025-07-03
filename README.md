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

✅ How to Run Locally
---
If testing locally:

Start a local web server:
http.server 8000

Then open in browser:
http://localhost:8000

✅ Screenshots
---
1. API Gateway route /contact

 ![Screenshot (228)](https://github.com/user-attachments/assets/0b780f74-fb2f-4de5-9b3b-717f643c0013)
   

2. Lambda console with deployed code

![Screenshot (227)](https://github.com/user-attachments/assets/b4e18d03-d8e3-4880-b7fb-c8d9deb1766f)


3. DynamoDB table with data

![Screenshot (234)](https://github.com/user-attachments/assets/bedebde1-de20-4f5b-a89a-3a8c1e0d7e3e)

4. Browser form screenshot

![Screenshot 2025-06-30 215507](https://github.com/user-attachments/assets/e0eaebce-b26b-41d8-a2bc-b337f8ae6195)


📚 Learnings
---
How to build a fully serverless backend

Setting up CORS in API Gateway

Debugging Lambda errors in CloudWatch

Integrating AWS services end-to-end

💻 Author
---
Ayushi Jaiswal




