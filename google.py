from googlesearch import search
from tkinter import *
import webbrowser

def mysearch():
    gg = search(query = e.get(), tld = "com", num = 10, start = 0, stop = 10)
    r = []
    for i in gg:
        r.append(i)
    r = sorted(r)
    htmlcode = f"""
                    <html>
                        <head>
                            <title>Search Results</title>
                        </head>
                        <body style = "background-color: grey">
                            <a href = {r[0]} target = "_blank",style = "align: center">{r[0]}</a>
                            <br> <br>
                            <a href = {r[1]} target = "_blank">{r[1]}</a>
                            <br> <br>
                            <a href = {r[2]} target = "_blank">{r[2]}</a>
                            <br> <br>
                            <a href = {r[3]} target = "_blank">{r[3]}</a>
                            <br> <br>
                            <a href = {r[4]} target = "_blank">{r[4]}</a>
                            <br> <br>
                            <a href = {r[5]} target = "_blank">{r[5]}</a>
                            <br> <br>
                            <a href = {r[6]} target = "_blank">{r[6]}</a>
                            <br> <br>
                            <a href = {r[7]} target = "_blank">{r[7]}</a>
                            <br> <br>
                            <a href = {r[8]} target = "_blank">{r[8]}</a>
                            <br> <br>
                            <a href = {r[9]} target = "_blank">{r[9]}</a>
                            <br> <br>
                        </body>
                    </html>
               """
    with open("GoogleSearchResults.html", "wt") as file:
        file.write(htmlcode)
        webbrowser.open("GoogleSearchResults.html", new = 2)
win = Tk()
win.title("Google Search")
e = Entry(win)
e.pack()
b = Button(win, text = "search", command = mysearch)
b.pack()


mainloop()
