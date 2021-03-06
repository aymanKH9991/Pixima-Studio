from .serializer import (
    ContrastImageSerializer,
    CropImageSerializer,
    FlipImageSerializer,
    ResizeImageSerializer,
    RotateImageSerializer,
    SaturationImageSerializer,
)
from .serializerHandler import (
    CropImageSerializerHandler,
    FlipImageSerializerHandler,
    ResizeImageSerializerHandler,
    RotateImageSerializerHandler,
    ContrastImageSerializerHandler,
    SaturationImageSerializerHandler,
)
from PiximaTools.BasicTools import (
    ContrastTool,
    CropTool,
    FlipTool,
    ResizeTool,
    RotatTool,
    SaturationTool,
)
from Core.models import ImageModel, ImageOperationsModel
from PiximaStudio.AbstractView import RESTView


class CropToolView(RESTView):
    def post(self, request, format=None):
        crop_tool = CropTool()
        crop_serializer = CropImageSerializer(data=request.data)
        im_handler = CropImageSerializerHandler(crop_serializer)
        try:
            if "Image" in request.data.keys() and request.data["Image"] != "":
                crop_tool.request2data(request=request).apply()
                image_path = crop_tool.save_image()
                imagepreview_path = crop_tool.get_preview()
                return self.ok_request(
                    {
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
            if im_handler.handle():
                image_path = (
                    crop_tool.serializer2data(serializer=crop_serializer)
                    .read_image()
                    .apply()
                    .save_image()
                )
                imagepreview_path = crop_tool.get_preview()
                ImageObj = ImageModel.objects.get(id=crop_serializer["id"].value)
                ImageOperationsModel.objects.create(
                    image=ImageObj, operation_name="CropTool"
                ).save()
                return self.ok_request(
                    {
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
        except Exception as e:
            return self.bad_request({"Message": "Error During Crop Process"})
        return self.bad_request(im_handler.errors)


class FlipToolView(RESTView):
    def post(self, request, format=None):
        flip_tool = FlipTool()
        flip_serializer = FlipImageSerializer(data=request.data)
        im_handler = FlipImageSerializerHandler(flip_serializer)
        try:
            if "Image" in request.data.keys() and request.data["Image"] != "":
                flip_tool.request2data(request=request).apply()
                image_path = flip_tool.save_image()
                imagepreview_path = flip_tool.get_preview()
                return self.ok_request(
                    {
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
            if im_handler.handle():
                image_path = (
                    flip_tool.serializer2data(flip_serializer)
                    .read_image()()
                    .save_image()
                )
                imagepreview_path = flip_tool.get_preview()
                ImageObj = ImageModel.objects.get(id=flip_serializer["id"].value)
                ImageOperationsModel.objects.create(
                    image=ImageObj, operation_name="FlipTool"
                ).save()
                return self.ok_request(
                    {
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
        except Exception as e:
            return self.bad_request({"Message": "Error During Flip Process"})
        return self.bad_request(im_handler.errors)


class RotateToolView(RESTView):
    def post(self, request, format=None):
        rotate_tool = RotatTool()
        rotate_serializer = RotateImageSerializer(data=request.data)
        im_handler = RotateImageSerializerHandler(rotate_serializer)
        try:
            if "Image" in request.data.keys() and request.data["Image"] != "":
                rotate_tool.request2data(request=request).apply()
                image_path = rotate_tool.save_image()
                imagepreview_path = rotate_tool.get_preview()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
            if im_handler.handle():
                image_path = (
                    rotate_tool.serializer2data(rotate_serializer)
                    .read_image()()
                    .save_image()
                )
                imagepreview_path = rotate_tool.get_preview()
                ImageObj = ImageModel.objects.get(id=rotate_serializer["id"].value)
                ImageOperationsModel.objects.create(
                    image=ImageObj, operation_name="RotateTool"
                ).save()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
        except Exception as e:
            return self.bad_request({"Message": "Error During Rotate Process"})
        return self.bad_request(im_handler.errors)


class ResizeToolView(RESTView):
    def post(self, request, format=None):
        resize_tool = ResizeTool()
        resize_serializer = ResizeImageSerializer(data=request.data)
        im_handler = ResizeImageSerializerHandler(resize_serializer)
        try:
            if "Image" in request.data.keys() and request.data["Image"] != "":
                resize_tool.request2data(request=request).apply()
                image_path = resize_tool.save_image()
                imagepreview_path = resize_tool.get_preview()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
            if im_handler.handle():
                image_path = (
                    resize_tool.serializer2data(resize_serializer)
                    .read_image()()
                    .save_image()
                )
                imagepreview_path = resize_tool.get_preview()
                ImageObj = ImageModel.objects.get(id=resize_serializer["id"].value)
                ImageOperationsModel.objects.create(
                    image=ImageObj, operation_name="ResizeTool"
                ).save()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
        except Exception as e:
            return self.bad_request({"Message": "Error During Resize Process"})

        return self.bad_request(im_handler.errors)


class ContrastToolView(RESTView):
    def post(self, request, format=None):
        contrast_tool = ContrastTool()
        contrast_serializer = ContrastImageSerializer(data=request.data)
        im_handler = ContrastImageSerializerHandler(contrast_serializer)
        try:
            if "Image" in request.data.keys() and request.data["Image"] != "":
                contrast_tool.request2data(request=request)()
                image_path = contrast_tool.save_image()
                imagepreview_path = contrast_tool.get_preview()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
            if im_handler.handle():
                image_path = (
                    contrast_tool.serializer2data(contrast_serializer)
                    .read_image()
                    .apply()
                    .save_image()
                )
                imagepreview_path = contrast_tool.get_preview()
                ImageObj = ImageModel.objects.get(id=contrast_serializer["id"].value)
                ImageOperationsModel.objects.create(
                    image=ImageObj, operation_name="ContrastTool"
                ).save()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
        except Exception as e:
            return self.bad_request(
                {"Message": "Error During Contrast&Brightness Adjustment Process"}
            )

        return self.bad_request(im_handler.errors)


class SaturationToolView(RESTView):
    def post(self, request, format=None):
        saturation_tool = SaturationTool()
        saturation_serializer = SaturationImageSerializer(data=request.data)
        im_handler = SaturationImageSerializerHandler(saturation_serializer)
        try:
            if "Image" in request.data.keys() and request.data["Image"] != "":
                saturation_tool.request2data(request=request)()
                image_path = saturation_tool.save_image()
                imagepreview_path = saturation_tool.get_preview()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
            if im_handler.handle():
                image_path = (
                    saturation_tool.serializer2data(saturation_serializer)
                    .read_image()
                    .apply()
                    .save_image()
                )
                imagepreview_path = saturation_tool.get_preview()
                ImageObj = ImageModel.objects.get(id=saturation_serializer["id"].value)
                ImageOperationsModel.objects.create(
                    image=ImageObj, operation_name="SaturationTool"
                ).save()
                return self.ok_request({
                        "Image": image_path,
                        "ImagePreview": imagepreview_path,
                    }
                )
        except Exception as e:
            return self.bad_request(
                {"Message": "Error During Saturation Adjustment Process"}
            )
        return self.bad_request(im_handler.errors)
