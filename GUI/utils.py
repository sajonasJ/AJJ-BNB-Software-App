

def on_hover(sel, thePrices, theNames, theDates):
    index = sel.index
    sel.annotation.set_text(f'Price: {thePrices[index]}\nName:{theNames[index]}\nDate: {theDates[index]}')


def selectDate(startDate, endDate):
    """grab and store the start and end date for a user selected period from 2 calendars"""
    # date.config(text = "Selected Date is: " + cal.get_date())
    print(startDate.get_date(), endDate.get_date())
    return (startDate.get_date(), endDate.get_date())


def cleanUserInput(input):
    # clear the user input
    splitInput = [item.strip() for item in input.split(',')]
    return splitInput

def onHoverRatings(sel, theScore, theNames):
    index = sel.index
    sel.annotation.set_text(f'Rating: {theScore[index]}\nPlace Name: {theNames[index]}')


#clear search fields (button will be needed for it)
def clearSearchQuery():
    print("clear search fields")


#display error messages
def displayErrorMessage(errorMessage):
    print("display error message" + errorMessage)