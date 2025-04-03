# contactList_with_Fixtures
# 📌 API Testing with Pytest - Contact List API

This repository contains API tests for the **Thinking Tester Contact List API**, implemented using **Python, Pytest, and Fixtures**. These tests cover user authentication, contact creation, retrieval, updating, and deletion.

## 🔧 Technologies Used
- **Python 3**
- **Pytest**
- **Requests**
- **JSON Handling**

## 📂 Project Structure
```
├── test_contact_list.py  # API tests using Pytest
├── README.md             # Project documentation
└── requirements.txt      # Dependencies list (optional)
```

## ✅ Test Cases Overview

### 🔹 User Authentication
1. **Create User** - Creates a new user with a unique email ID.
2. **Login User** - Logs in with the created user's credentials.

### 🔹 Contact Management
3. **Get Contacts** - Fetches the list of existing contacts.
4. **Add Contact** - Creates a new contact with personal details.
5. **Get Contacts After Adding** - Confirms the new contact appears in the list.
6. **Update Contact** - Modifies the details of an existing contact.
7. **Get Contacts After Updating** - Ensures the contact details have been updated.
8. **Delete Contact** - Removes the created contact from the database.

## 🚀 How to Run the Tests

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2️⃣ (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, install manually:
```bash
pip install pytest requests
```

### 4️⃣ Run the Tests
```bash
pytest test_contact_list.py -v
```

## 📌 Notes
- A valid **authorization token** is required for login and subsequent requests.
- Pytest **fixtures** are used to manage authentication tokens efficiently.
- Some test cases rely on API features that may require manual verification.

## 🔥 Future Enhancements
- Implement **parameterized tests** for different user inputs.
- Add **schema validation** with `jsonschema`.
- Integrate with **GitHub Actions** for automated test execution.
- Improve logging and reporting using `pytest-html`.

## 🤝 Contributions
Feel free to fork this repository, enhance test cases, and submit a PR! 🚀

