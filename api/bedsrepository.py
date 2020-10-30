from beds import Beds


class BedsRepositry:
    BedsList = []

    message = ""

    def changeLayout(layout):
        if layout == "left":
            return "right"
        else:
            return "left"

    def checklimit(initializer, floor):
        if initializer % 6 == 0:
            return floor + 1
        else:
            return floor

    def addBeds(numberofbeds):
        floor = 0
        initializer = 0
        if int(numberofbeds) <= 30:
            message = numberofbeds + " " + "beds are added"
            layout = "left"
            for i in range(0, int(numberofbeds)):
                bed = Beds(True, str(i + 1), str(floor), layout)
                layout = BedsRepositry.changeLayout(layout)
                initializer += 1
                floor = BedsRepositry.checklimit(initializer, floor)
                BedsRepositry.BedsList.append(bed)
        else:
            message = "Total Capacity is less as compared to need of beds"

        return message

    def checkVacantBed():
        for beds in BedsRepositry.BedsList:
            if beds.vacant is True:
                beds.vacant = False
                return beds.id
        return -1

    def emptyBed(id):
        for beds in BedsRepositry.BedsList:
            if beds.id == id:
                beds.vacant = True
