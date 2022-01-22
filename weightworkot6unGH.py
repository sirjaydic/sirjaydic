
#// This is the rabbit hole idea started on 07JAN2022, 15JAN updated with code taken from jerms version and added in//
#// Waiting on james input to send updated version, Got duel list. one for weight one for workouts. Might do extra input line like jerm//
#
#Now would like to see some color to the webpages and some way to track progress on the weight page showing what progress is made/los
#This is the Github version. If your reading this know there will be mispellings and used code. It started years ago and many of the begining sources have gotten lost. 


from guizero import App,  Combo, Text, CheckBox, ButtonGroup, PushButton,  info, TextBox, Picture
import subprocess
import datetime
#// -stolen from Jeremy- Defined date and time to now
now = datetime.datetime.now()


def do_booking(): 
    info("Your Event as been reorded", "Thank you "+fuck_choice.value + " for recording"),
    print('\nYour client ' + fuck_choice.value)
    
    save()

#// Made a how to WTF how to use button to make sense
def WTFisThs():
    info("Select \"SaveEntry\" to save workout, \"WeightSave\" to save weight ", "Select pages to view recorded info")
 

    

#//Stole jerms date and <br> code to make multi lines//
#// added other to the value to input random stuff //
    
def save():
    if room_choice.value == str('B'):
        roomCho='Did Treadmill'
    elif room_choice.value == str('F'):
        roomCho='Did the Elliptical '
    elif room_choice.value == str('N'):
        roomCho='inputted '
    else:
        roomCho='Lifted Weights of '+fatasS.value 
    
    more_lines= [''+'<b>' +now.strftime("%Y-%m-%d %H:%M:%S") + ' </b><br>'+ fuck_choice.value+ ' with workout  ' + multi_fuck.value , roomCho + fuckE.value +' '+  xrthot.value+ '<br><br>' ,'']
    with open('HTML1/Page1.html','a')as f:
        f.writelines('\n'.join(more_lines))
    xrthot.clear()
    fatasS.clear()
    fuckE.clear()



    
def Wpage():
    subprocess.Popen(['open','HTML1/Page1.HTML'])# To show to log events. would like to be able to edit and change spacing

#Again stole jerms <b> spacing code
# for fat page remove leave just wieght entry and nothing else making workingout on page and a weight tracking page.
def Jusfatpage():
    
    more_lines= [''+'<b>' +now.strftime("%Y-%m-%d %H:%M:%S") + '</b><br>'+ fuck_choice.value + fuckE.value +' Weighed  '+ fatasS.value + '<br>', xrthot.value+'<br><br>','']
    with open('HTML1/FatPage.html','a')as f:
        f.writelines('\n'.join(more_lines))
    xrthot.clear()
    fatasS.clear()
    fuckE.clear()


def Fatpag():
    subprocess.Popen(['open','HTML1/FatPage.HTML'])# To show to log events. would like to be able to edit and change spacing
    

app = App(bg="PeachPuff",title="Workout and Weight Tracker", width=700, height=400, layout="grid")

# create widget here
message = Text(app,text = "Exercise person info",grid=[1,4], align="left")
fuckE = TextBox(app,grid=[1,5], align="left")
# attempt of a box for the weight.. got it on first run
message = Text(app,text = "Weights input",grid=[1,4], align="right")
fatasS  = TextBox(app,grid=[1,5],align="right")


fuck_description = Text(app, text="Person to input?", grid=[0,0], align="left")
fuck_choice = Combo(app, options=["You ", "Me ", "Them "], grid=[1,0], align="left")

multi_fuck = Combo(app, options= ["None", "Stretchers", "Boxing", "Game Exercise"], grid=[1,3], align="right")
multi_description = Text(app, text="Extra Finish / Start", grid=[1,3], align="left")
 
room_choice = ButtonGroup(app, options=[ ["Elliptical", "F"], ["Treadmill", "B"],["Weight", "O"],["Other","N"] ],
selected="M", horizontal=True, grid=[1,2], align="left")

book_goodfuck = PushButton(app, command=do_booking, text="Book Event", grid=[1,7], align="left")
inFo_butt = PushButton(app, command=WTFisThs, text="How to use", grid=[1,7], align="right")

# Button to book on text file
button= PushButton(app,command=save,text="Save\nEntry",grid=[1,9],align="left")
button= PushButton(app,command=Wpage,text="Open\nPage",grid=[1,10],align="left")
button= PushButton(app,command=Jusfatpage,text="Weight\nSave",grid=[1,9],align="right")
button= PushButton(app,command=Fatpag,text="Weight\nPage",grid=[1,10],align="right")

# Notes to be added to the string for more info of the input
message = Text(app,text ="Extra Infomation",grid=[1,12],align="bottom")
xrthot = TextBox(app,grid=[1,17],width=45,multiline=True,scrollbar=True)

app.display()


