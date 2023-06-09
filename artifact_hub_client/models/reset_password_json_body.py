from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ResetPasswordJsonBody")


@attr.s(auto_attribs=True)
class ResetPasswordJsonBody:
    """
    Attributes:
        code (str):
        password (str):
    """

    code: str
    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        password = d.pop("password")

        reset_password_json_body = cls(
            code=code,
            password=password,
        )

        reset_password_json_body.additional_properties = d
        return reset_password_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
