
# 🖼️ Pic2Sketch

**Pic2Sketch** is a computer vision project that converts regular images into artistic pencil sketches using image processing techniques. Whether you’re a developer looking to add an artsy touch to your application or just want to turn your photos into cool line art, Pic2Sketch has you covered.

## ✨ Features

- Convert color or grayscale images into pencil-style sketches  
- Fast and lightweight processing  
- Simple and intuitive interface (CLI or GUI)  
- Option to adjust sketch intensity and details  

## 🛠️ Technologies Used

- Python  
- OpenCV  
- NumPy  
- Flask (for web interface - optional)  

## 📸 How It Works

1. Convert image to grayscale  
2. Invert the grayscale image  
3. Apply Gaussian blur to the inverted image  
4. Blend the grayscale image with the blurred inverted image using a dodge blend  
5. Output the sketch image  

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.6+ and the required libraries:

```bash
pip install opencv-python numpy
```

### Clone the Repository

```bash
git clone https://github.com/yourusername/Pic2Sketch.git
cd Pic2Sketch
```

### Run the Script

```bash
python pic2sketch.py --input your_image.jpg --output sketch_output.png
```

Or run the GUI version (if implemented):

```bash
python app.py
```
