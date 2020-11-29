import datetime

onDate = lambda date, day: date + datetime.timedelta(days=(day - date.weekday()) % 7)

months = {  1: "січня", 
            2: "лютого", 
            3: "березня", 
            4: "квітня", 
            5: "травня", 
            6: "червня", 
            7: "липня", 
            8: "серпня", 
            9: "вересня", 
            10: "жовтня", 
            11: "листопада",
            12: "грудня"}

nextWednesday = onDate(datetime.datetime.now().date(), 2)

nextWednesdayDateInStandardFormat = nextWednesday.strftime('%d.%m.%Y')

nextWednesdayDateUA = str(nextWednesday.timetuple()[2]) + ' ' + months[nextWednesday.timetuple()[1]]