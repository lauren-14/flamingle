from dataclasses import dataclass

class Profile :

    def __init__(self, id) :
        self.id = id

    username : str = ""
    groups : list[str] = []

    def read_feilds(self, feilds : dict) -> Profile:
        self.username = feilds["username"]
        self.groups = feilds ["groups"]
        return self
    
    def write_feilds(self) -> dict:
        return {"username":self.username, "groups":self.groups}
    
    def __str__(self) -> str :
        return f"{self.id}: {self.write_feilds()}"


mock_group_db = {
    "Group A" : ["001", "002"],
    "Group B" : ["001", "003"]
}

mock_person_db = {
    "001":{"username":"Jad", "groups":["Group A","Group B"]},
    "002":{"username":"Sophia", "groups":["Group B"]},
    "003":{"username":"Lauren", "groups":["Group C"]}
}

def get_username(id) -> str :
    return mock_person_db[id]["username"]

def get_profile(id) -> Profile :
    return Profile(id).read_feilds(mock_person_db[id])
    
def write_profile(profile : Profile) -> None:
    mock_person_db[profile.id] = profile.write_feilds()



person001 = get_profile("001")
print(person001.id, person001)
person001.username = "hello"
print(person001.id, person001)
write_profile(person001)
print(person001.id, person001)
print(mock_person_db)