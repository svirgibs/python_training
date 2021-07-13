from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, company=None,
                 title=None, address=None, homephone=None, mobile=None, workphone=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, address2=None, secondaryphone=None,
                 notes=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.nickname = nickname
        self.company = company
        self.title = title
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


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
