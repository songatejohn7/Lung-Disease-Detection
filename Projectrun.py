import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import Tk
from tensorflow.keras.models import load_model # type : ignore
from tensorflow.keras.applications.resnet50 import preprocess_input # type : ignore

model = load_model("./model/4_model_resnet50.h5")
print(" =================== Stage 1 =====================")

root = Tk()
root.withdraw()
print(" =================== Stage 2 =====================")
img_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg")])
print(img_path)
root.destroy()
print(" =================== Stage 3 =====================")
if img_path:
    #Read and preprocess the selected image
    img = cv2.imread(img_path)
    print(" =================== Stage 4 =====================")
    img = cv2.resize(img, (100, 100))
    print(" =================== Stage 5 =====================")
    x = np.expand_dims(img, axis=0)
    x = preprocess_input(x) 
    print(" =================== Stage 6 =====================")
    result = model.predict(x)
    
    print(" =================== Stage 7 =====================")
    categories = ['Cancer', 'Covid', 'Normal', 'Phenomena']
    percentages = [result[0][0], result[0][1],result[0][2],result[0][3]]
    
    print(" =================== Stage 8 =====================")
    sorted_data = sorted(zip(categories, percentages),key=lambda x: x[1], reverse=True)
    sorted_categories, sorted_percentages = zip(*sorted_data)
    print(" =================== Stage 9 =====================")
    
    predicted_category = categories[np.argmax(result)]
    text_color = 'green' if predicted_category == 'Normal ' else 'red'
    print(" =================== Stage 10 =====================")
    
    fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(12, 5))
    
    
    ax1.imshow(img)
    ax1.set_title("Predicted: " + predicted_category, color=text_color, fontsize=12)
    ax1.axis('off')
    
    
    ax2.axis('off')
    print(sorted_categories[0])
    # ax2.text(0, 0.5,   # adjust the text position
    #          f"{sorted_categories[0]} - {sorted_percentages[0] * 100:.2f}%\n"
    #          f"{sorted_categories[1]} - {sorted_percentages[1] * 100:.2f}%\n"
    #          f"{sorted_categories[2]} - {sorted_percentages[2] * 100:.2f}%\n"
    #          f"{sorted_categories[3]} - {sorted_percentages[3] * 100:.2f}%", fontsize=12, ha='left', va='center')
    
    plt.show()

else:
    print("No image selected:")
