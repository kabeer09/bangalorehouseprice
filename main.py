import tkinter as tk
from tkinter import Label, ttk
import pandas as pd
from PIL import ImageTk,Image
from sklearn.linear_model import LinearRegression
from tkinter import Label, messagebox

df = pd.read_csv('C:/Users/HP/Desktop/py/clean_data.csv')
window = tk.Tk()
window.title('bangalore house price')
#window.iconbitmap('OIP (1).jpg')
window.minsize(570,650)
window.configure(bg="#ECECEC")


img = Image.open('01_VillaSophia_CollColl_AIHouse.webp')
resized_img = img.resize((400,200))
img = ImageTk.PhotoImage(resized_img)


img_label = Label(window,image=img)
img_label.pack(pady=(10,10))
text_label = Label(window,text='Bangalore House Price Pridiction',fg='black',bg='#ECECEC')
text_label.pack(pady=(10,10))
text_label.config(font=('verdana',24))


label_location = tk.Label(window, text="Locations:")
label_location.pack(pady=(10,10))
location = df['location'].unique().tolist()
location_var = tk.StringVar(window)
location_dropdown = ttk.Combobox(window, textvariable=location_var)
location_dropdown['values'] = location
location_dropdown.pack()



label_bhk = tk.Label(window, text="Number of Bedrooms:")
label_bhk.pack(pady=(10,10))
bhk = df['bhk'].unique().tolist()
bhk_var = tk.StringVar(window)
bhk_dropdown = ttk.Combobox(window, textvariable=bhk_var)
bhk_dropdown['values'] = bhk
bhk_dropdown.pack()



label_total_sqft = tk.Label(window, text="total_sqft:")
label_total_sqft.pack(pady=(10,10))
total_sqft = df['total_sqft'].unique().tolist()
total_sqft_var = tk.StringVar(window)
total_sqft_dropdown = ttk.Combobox(window, textvariable=total_sqft_var)
total_sqft_dropdown['values'] = total_sqft
total_sqft_dropdown.pack()



label_bath = tk.Label(window, text="Number Of Bathrooms:")
label_bath.pack(pady=(10,10))
bath = df['bath'].unique().tolist()
bath_var = tk.StringVar(window)
bath_dropdown = ttk.Combobox(window, textvariable=bath_var)
bath_dropdown['values'] = bath
bath_dropdown.pack()

def predict_price():
    location = location_dropdown.get()
    total_sqft = float(total_sqft_dropdown.get())
    bhk = float(bhk_dropdown.get())

    # Filter dataset based on location
    df_location = df[df['location'] == location]

    # Create features (X) and target variable (y)
    X = df_location[['total_sqft', 'bhk']]
    y = df_location['price']

    # Create the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Perform prediction
    predicted_price = model.predict([[total_sqft, bhk]])

    # Show prediction in a message box
    messagebox.showinfo("Prediction Result", f"The predicted price for a house in {location} with {bhk} bHK and {total_sqft} sqft is: {predicted_price}")

# Create predict button
button_predict = tk.Button(window, text="Predict Price", command=predict_price)
button_predict.pack(pady=(10,10))



# Run the GUI event loop
window.mainloop()
