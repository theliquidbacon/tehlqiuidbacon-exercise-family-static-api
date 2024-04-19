from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 3443,
                "first_name": "Tommy",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 4446,
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 5522,
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                self._members.remove(member)
                return
        raise ValueError("Member not found")

    def update_member(self, member_id, member):
        for i, m in enumerate(self._members):
            if m["id"] == member_id:
                member["id"] = member_id
                self._members[i] = member
                return
        raise ValueError("Member not found")

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member
        raise ValueError("Member not found")
    def get_all_members(self):
        return self._members