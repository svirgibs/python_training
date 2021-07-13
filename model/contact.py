from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, address=None, homephone=None,
                 mobile=None, workphone=None, fax=None, secondaryphone=None, email=None,
                 all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.secondaryphone = secondaryphone
        self.email = email
        self.all_phones_from_home_page = all_phones_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == self.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
