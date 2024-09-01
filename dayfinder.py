'''
class Rectangle(object):
 """Represents a rectangle."""
box = Rectangle()
box.color = 'blue'
box.bbox = [[-100, -60],[100, 60]]
class Canvas(object):
 """Represents a canvas.
 attributes: width, height, background color"""
a_canvas = Canvas()
a_canvas.width = 500
a_canvas.height = 500
def draw_rectangle(canvas, rectangle):
 drawn_canvas = world.ca(canvas.width, canvas.height)
 drawn_canvas.rectangle(rectangle.bbox, fill=rectangle.color)
world = World()
draw_rectangle(a_canvas,box)
world.mainloop()'''
import tkinter as tk
import calendar

def find_day():
    date = entry.get()
    day, month, year = map(int, date.split('/'))
    year = year % 100  # Extract the last two digits of the year
    day_of_week = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_of_week]
    output_label.config(text="Day of Birth: " + day_name,font=font1)

    # if date==:

root = tk.Tk()
root.title("Day of Birth Finder")
root.geometry("500x500")

font=('times',35,'bold')
font1=('times',15,'bold')

tt=tk.Label(root,text="DAY FINDER")
tt.config(font=font)
tt.place(x=100,y=50)

label = tk.Label(root, text="Enter your date  (dd/mm/yy):")
label.config(font=font1)
label.place(x=50,y=150)

entry = tk.Entry(root)
entry.place(x=300,y=155)

button = tk.Button(root, text="Find Day", command=find_day)
button.config(font=font1)
button.place(x=200,y=300)

b2=tk.Button(root,text="Exit",command=root.quit)
b2.config(font=font1)
b2.place(x=220,y=400)

output_label = tk.Label(root, text="")
output_label.place(x=150,y=220)

root.mainloop()