# 🐶🐱 Cat vs Dog Classifier

[![Streamlit App](https://img.shields.io/badge/Deployed-Streamlit-blue)](https://catxdog-classifier.streamlit.app/)

## 🔗 Live Demo

You can access the live web app here: [Cat vs Dog Classifier](https://catxdog-classifier.streamlit.app/)  
Clicking the link will take you directly to the landing page. Using this website, you can check whether a particular image is of a **Cat** or a **Dog**. On mobile, you can also take a picture for input.

---

## 📝 Project Description

This project is a **real-time Cat vs Dog image classifier** built using **Python**, **TensorFlow/Keras**, and **Streamlit**.  
The app uses a **Convolutional Neural Network (CNN)** trained on the Kaggle Dogs vs Cats dataset (25,000 images) to predict the class of an uploaded image.

Key features:

- Simple, clean web UI with **Streamlit**.
- Predicts whether an image is a **Cat** or **Dog**.
- Mobile-friendly input (upload or take a picture directly).
- Real-time predictions with confidence.

---

## 🛠 Technologies Used

- **Python 3.12**
- **TensorFlow / Keras** – for CNN model
- **NumPy** – numerical operations
- **Pillow (PIL)** – image processing
- **Streamlit** – web app deployment
- **OpenCV** – optional image preprocessing

---

## 📂 Project Structure

```
cat-dog-classifier/
│
├── app.py # Streamlit web app
├── cat_dog_model.keras # Trained CNN model
├── requirements.txt # Python dependencies
├── screenshots/ # App screenshots
│ ├── upload.png
│ └── prediction.png
└── README.md

```

---

## ⚡ How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/YourUsername/cat-dog-classifier.git
cd cat-dog-classifier
```

2. **Create a virtual environment (optional but recommended)**
```bash
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux / macOS
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
streamlit run app.py
```

5. **Open the provided URL in your browser (e.g., http://localhost:8501).**

---

## 📈 Model Info

- **Architecture**: Simple CNN (3 Conv2D + MaxPooling layers, Dense output)
- **Input Shape**: 128x128 RGB images
- **Output**: 1 neuron with sigmoid activation (0 = Cat, 1 = Dog)
- **Training**: 10 epochs on Kaggle Dogs vs Cats dataset
- **Accuracy**: ~90% on test images

---

## 📸 Screenshots
Upload Interface	Prediction Result

	

(Add screenshots in the screenshots/ folder for clarity)

---

## ✅ Usage

- Upload any JPG, JPEG, or PNG image of a cat or dog.
- Click **Predict**.
- View the result with confidence score.
- Works on desktop and mobile devices.

---

## 💡 Future Improvements

- Add **video classification** (live webcam feed).
- Increase **dataset size** or use **pre-trained models** for higher accuracy.
- Show **confidence percentage** and class probabilities in a graph.
- Add **data augmentation** during training to reduce overfitting.

---

## 👨‍💻 Author

**Humas Furquan**

* GitHub: [https://github.com/HumasFurquan](https://github.com/HumasFurquan)
* LinkedIn: [https://www.linkedin.com/in/humas-furquan-7b2961216](https://www.linkedin.com/in/humas-furquan-7b2961216)

---

## 📄 License

This project is licensed under the **MIT License**.
