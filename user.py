from enum import Enum
import datetime
 
class UserStatus(Enum):
    ACTIVE = 1
    DELETED = 2

class User:
    def __init__(self, first_name: str, last_name: str, external_id: str, address: Address)
        if not first_name or not last_name or not address:
            raise InvalidArgumentError("first_name, last_name & address cannot be empty")

        self.user_id = nil
        self.first_name = first_name
        self.last_name = last_name
        self.external_id = external_id
        self.created_at = datetime.datetime.Now()
        self.updated_at = datetime.datetime.Now()
        self.status = UserStatus.ACTIVE
        self.address = address

    def UpdateExternalId(external_id: str):
        self.external_id = external_id

