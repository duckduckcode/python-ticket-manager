from bottle import route, view, run, static_file
from itertools import count




# CLASSES ######################

class Ticket:

    _ids = count(0)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.checked_in = False
        self.id = next(self._ids)

    def get_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name




# CONSTANTS ####################

TICKETS_AVAILABLE = 30




# VARIABLES ####################

tickets = [
    Ticket("Fred", "Flintstone", "fred@flintstone.com"),
    Ticket("Wonder", "Woman", "wonderwoman@heroes.org"),
    Ticket("Justin", "Bieber", "justin@thebeebs.com")
]




# PAGES ########################

# Home Page
@route('/')
@view('index')
def index():
    pass


# Check In Page
@route('/check-in')
@view('check-in')
def check_in():

    data = dict(
        ticket_list = tickets
    )

    return data


# Check In Confirmation Page
@route('/check-in-confirmation/<ticket_id>')
@view('check-in-confirmation')
def check_in_confirmation(ticket_id):

    ticket_id_to_check_in = int(ticket_id)
    checked_in_ticket = None

    for ticket in tickets:
        if ticket.id == ticket_id_to_check_in:
            ticket.checked_in = True
            checked_in_ticket = ticket
    
    data = dict(
        ticket = checked_in_ticket
    )

    return data


# Sell Ticket Page
@route('/sell-ticket')
@view('sell-ticket')
def sell_ticket():
    pass


# Sale Confirmation Page
@route('/ticket-sold')
@view('sale-confirmation')
def ticket_sold():
    pass



@route('/css/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./css/')




# START THE WEBSITE ###########

run(host='localhost', port=8081, reloader=True, debug=True)