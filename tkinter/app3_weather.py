import json
import requests
from tkinter import *

# Definning the window (root)
def set_root():
    root = Tk()
    root.title('')
    # root.iconbitmap('')
    # root.geometry('400x150')
    root.configure(background='green')

    return root

# Setting the loop
def loop(root):
    root.mainloop()


# Making an API requst and storing some specifics in variables
def api_request():
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=064B3608-B519-47DB-ACA6-D369D8A8A418")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
    except Exception:
        api = "Error..."

    return city, quality, category    

# Creating labels
def labeling(root, city, quality, category):
    main_lbl = Label(
        root,
        text= city + ", Air Quality " + str(quality) + " - " + category,
        font= ('Helvetica', 19),
        background='green'
        )
    main_lbl.grid(row=0, column=0, columnspan=3)

# Running
def main():
    root = set_root()
    city, quality, category = api_request()
    labeling(root, city, quality, category)
    loop(root)


if __name__ == "__main__":
    main()

# lbl_city = Label(root, text=city)
# lbl_city.grid(row=0, column=1)
# lbl_city_text = Label(root, text="City:")
# lbl_city_text.grid(row=0, column=0)

# lbl_quality = Label(root, text=quality)
# lbl_quality.grid(row=1, column=1)
# lbl_quality_text = Label(root, text="Quality:")
# lbl_quality_text.grid(row=1, column=0)

# lbl_category = Label(root, text=category)
# lbl_category.grid(row=2, column=1)
# lbl_category_text = Label(root, text="Category:")
# lbl_category_text.grid(row=2, column=0)




# print(api[0]['StateCode'])

# for item in api:
#     print(item)

