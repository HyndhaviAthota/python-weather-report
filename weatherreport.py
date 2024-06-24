#for now()
import datetime as dt
#for sending http requests using python 
import requests
# for timezone()
import pytz
#drawing
import turtle
from pprint import pprint

def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=94337f826ff1729439c513de2bd404df&units=metric');
    return res.json();
def print_weather(result,city):
    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Humidity: {}%".format(result['main']['humidity']))
    print("Pressure: {} mbar".format(result['main']['pressure']))
    print("Description: {}".format(result['weather'][0]['description']))
    #report=print("Weather: {}".format(result['weather'][0]['main']))
    report=result['weather'][0]['main']
    print("Weather: {}".format(report))
    print("Sun Rises in {}: {} local time.".format(city,dt.datetime.utcfromtimestamp(result['sys']['sunrise']+result['timezone'])))
    print("Sun Sets in {}:  {} local time.".format(city,dt.datetime.utcfromtimestamp(result['sys']['sunset']+result['timezone'])))
    print()
    if(report=="Clear"):
            print("          ")
            print("   \_ _/        ")   
            print(" _ /   \ _     ")        
            print("   \_ _/      ")   
            print("   /   \       ")
            screen = turtle.Screen()
            # background color
            screen.bgcolor("lightblue")
 
            # turtle object
            y = turtle.Turtle()
 
            def drawFourRays(t, length, radius):
     
                for i in range(4):
                    y.penup()
                    y.forward(radius)
                    y.pendown()
                    y.forward(length)
                    y.penup()
                    y.backward(length + radius)
                    y.left(90)
                    y.penup()
 
            # Use the defined
            # function to draw rays
            y.penup()
            y.goto(85, 169)
            y.pendown()
            drawFourRays(y, 85, 54)
            y.right(45)
            drawFourRays(y, 85, 54)
            y.left(45)

            def filled_circle(radius, color):
                t.color(color,color)
                t.begin_fill()
                t.circle(radius)
                t.end_fill()
            def cloud(radius, cloud_color="white"):
                filled_circle(radius,cloud_color)
                t.forward(radius)
                filled_circle(radius,cloud_color)
                t.right(90)
                filled_circle(radius,cloud_color)
                t.right(90)
                filled_circle(radius,cloud_color)
                t.right(90)
                filled_circle(radius,cloud_color)
                t.right(90)

            y.penup()
            y.goto(85, 110)
            y.fillcolor("yellow")
            y.pendown()
            y.begin_fill()
            y.circle(45)
            y.end_fill()

            radius = 50
            cloud(radius)
 
            turtle.done()
            
    if (report=="Haze"):
        print("  _ - .--. _ - _ -")
        print("-_ .-(    ). - _ -")  
        print(" -(_._)) - _ -  ") 
        print(" _ - _ - _ -  ")

    if (report=="Clouds"):
        print("          ")
        print("   \ _/             .--.     ")   
        print(" _ /  .-.        .-(    ).      ")        
        print("   \(   ).     (_.)_)   ")   
        print("   /(_(__)                  ")
    

    if (report=="Mist" or report=="Smoke"):
        print("  _ - _ - _ -  ") 
        print("- _ - _   ←  _  ")
        print(" _ - _ - _ -  ")
        
    if (report=="Rain"):
        print("     .--. ")
        print("  .-(    ).  ")
        print(" (_._)_) ")
        print("  ⚡‘‘⚡‘‘   ")
        print("    ‘ ‘ ‘ ‘    ")
        '''z=turtle.Turtle()
        screens=turtle.Screen()
        screens.bgcolor("whitesmoke")

        def filled_circle(radius, color):
            z.color(color,color)
            z.begin_fill()
            z.circle(radius)
            z.end_fill()

        def rainbow(radius=200,interval=10):
            roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'whitesmoke']

        for r_color in roygbiv:
            filled_circle(radius,r_color)
            radius -= interval

        # Move turtle a up by a little
        z.pendown()
        z.left(90)
        z.forward(interval)
        z.right(90)
        z.penup()
        z.goto(0,0)
        rainbow(300,10)
        turtle.done()'''
        sc = turtle.Screen()
        pen = turtle.Turtle()
        def semi_circle(col, rad, val):
            pen.color(col)
        pen.circle(rad, -180)
        pen.up()
        pen.setpos(val, 0)
        pen.down()
        pen.right(180)
        col = ['violet', 'indigo', 'blue','green', 'yellow', 'orange', 'red']
        sc.setup(600, 600)
        sc.bgcolor('whitesmoke')
        pen.right(90)
        pen.width(10)
        pen.speed(7)
        for i in range(7):
            semi_circle(col[i], 10*(i + 8), -10*(i + 1))  
        pen.hideturtle()

        
def main():
        #current_time = dt.datetime.now()
        #print("Time now at greenwich meridian is:", current_time)
        # using now() to get current time
        current_time = dt.datetime.now(pytz.timezone('Asia/Kolkata'))
        print("The current time in India is :", current_time)
        print()
        city=input('Enter the city:')
        print()
        print("----------------------------------------------")
        try:
            query='q='+city;
            w_data=weather_data(query);
            print_weather(w_data, city)
            print()
        except:
            print('City name not found...')
if _name=='main_':
    main()
