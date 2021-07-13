from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, address=None, homephone=None,
                 mobile=None, workphone=None, fax=None, secondaryphone=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.secondaryphone = secondaryphone
        self.email = email
        self.id = id

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
