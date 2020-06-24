class Service:
    def __init__(self):
        self._contact = []

    def add_contact(self, paylode):
        self._contact.append(paylode)

    def get_contact(self, paylode)->object:   # name 객체리턴하니까   ->object추가
        for i in self._contact:
            if paylode == i.name:
                return i


    def get_contacts(self)->[]:  # 배열을 리턴하니까 ->[]  을 써준다

        contact = []
        for i in self._contact:
            contact.append(i)
        return ' '.join(contact)

    def del_contact(self, paylode):   #name
        for i, t in enumerate(self._contact):
            if paylode == i.name:
                del self._contact[i]


