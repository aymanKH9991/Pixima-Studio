from abc import abstractmethod, ABCMeta
from rest_framework.serializers import Serializer
from Core.models import ImageModel
from PiximaStudio.settings import MEDIA_ROOT
from . import serializer
import os


class SerializerHandler(metaclass=ABCMeta):
    def __init__(self, serializer: Serializer) -> None:
        self.serializer = serializer
        self.errors = {}

    @abstractmethod
    def handle(self) -> bool:
        pass


class ImageSerializerHandler(SerializerHandler):
    def __init__(
        self,
        serializer: serializer.ImageSerializer,
        preview_optinos: list = None,
    ) -> None:
        super().__init__(serializer)
        if preview_optinos is None:
            self.preview_options = ["None", "Low", "Mid", "High"]

    def __image_index_exists(self):
        directory_id = self.serializer.data["id"]
        index = self.serializer.data["ImageIndex"]
        if index == -1:
            return True
        return (
            True
            if os.path.exists(
                os.path.join(
                    MEDIA_ROOT, "Images", str(directory_id), str(index) + ".jpg"
                )
            )
            else False
        )

    def handle(self) -> bool:
        res = self.serializer.is_valid()
        if res:
            if (
                self.serializer.data["id"] is None
                and self.serializer.data["Image"] is None
            ):
                self.errors = {"Message": "Both id and Image Can't Be Null"}
                return False
            try:
                query_set = ImageModel.objects.get(id=self.serializer.data["id"])
                if not query_set:
                    raise ImageModel.DoesNotExist()
            except ImageModel.DoesNotExist as ex:
                self.errors = {"Message": "Id Not Found"}
                return False
            if self.serializer.data["ImageIndex"] < -1:
                self.errors = {"Message": "ImageIndex Less Than -1"}
                return False
            if not self.__image_index_exists() and self.serializer.data["id"]:
                self.errors = {"Message": "ImageIndex Not Found"}
                return False
            if self.serializer.data["Preview"] not in self.preview_options:
                self.errors = {
                    "Message": f"Preview Should Be On Of This Values {self.preview_options}"
                }
                return False
        if not res:
            self.errors = self.serializer.errors
        return res
