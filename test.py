
import json
import random
from faker import Faker
from faker.providers import company, address, isbn

fake = Faker()
fake.add_provider(company)
fake.add_provider(address)
fake.add_provider(isbn)

class Address:
    def __init__(self):
        self.street = fake.street_address()
        self.city = fake.city()
        self.postcode = fake.postcode()
        self.country = fake.country_code()
    def __str__(self):
        return f"{self.street} {self.city} {self.postcode} {self.country}"
    def asJson(self):
        return json.JSONEncoder().encode(self.__dict__)

class Company:
    def __init__(self, Id, internal):
        self.Id = Id
        self.internal = internal
        self.name = fake.company()
        self.address = Address()
    def __str__(self):
        return f"Id={self.Id} name={self.name} address={self.address}"
    def asJson(self):
        return json.JSONEncoder().encode( { 'Id': self.Id, 'name': self.name, 'internal': self.internal, 'addresses': [self.address.__dict__]}) 

class Book:
    def __init__(self, Id):
        self.isbn = fake.isbn13()
        self.Id = Id
    def asJson(self):
        return json.JSONEncoder().encode(self.__dict__)

class BookSale:
    def __init__(self, Id, extCompanyId, intCompanyId, bookId):
        self.Id = Id
        self.extCompanyId = extCompanyId
        self.intCompanyId = intCompanyId
        self.bookId = bookId
    def asJson(self):
        return json.JSONEncoder().encode(self.__dict__)

def generateAddress(ct):
    return [Address() for item in range(1, ct)]

def generateBook(ct):
    return [Book(item) for item in range(1, ct)]

def generateCompany(ct, start, internal):
    return [Company(Id+start ,internal) for Id in range(1, ct)]

numberBooks = 5_000
books = generateBook(numberBooks)
intCompanies = 100
intCompany = generateCompany(intCompanies, 0, 'Y')
extCompany = generateCompany(200_000, len(intCompany), 'N')

def bookSaleGenerator():
    ct = 0
    for e in extCompany:
        for x in range(1,random.randint(1,3)):
            ct = ct + 1
            yield BookSale(ct, e.Id, random.randint(1,intCompanies), random.randint(1,numberBooks))

def generateBookSale():
    return [item for item in bookSaleGenerator()]

def writeJson(fileName, collection):
    print(f"writing to {fileName}")
    with open(fileName, 'w') as f:
        f.writelines(map(lambda x: x.asJson() + "\n", collection))
    print(f"{fileName} written")

writeJson('book.json', books)
writeJson('intCompany.json', intCompany)
writeJson('extCompany.json', extCompany)
writeJson('bookSale.json', generateBookSale())
