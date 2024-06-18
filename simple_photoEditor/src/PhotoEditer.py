from PIL import Image, ImageEnhance, ImageFilter
import os


class PhotoEdit:

    def __init__(self, img_path, img_save_path) -> None:
        """
        Initializes the PhotoEdit class with the image path and save path.

        Args:
            img_path (str): The path to the image file.
            img_save_path (str): The path to save the edited image.
        """
        # Store the image path
        self.img_path = img_path

        # Store the image save path
        self.img_save_path = img_save_path

        # Open the image using PIL
        self.image = Image.open(self.img_path)

    def rotate_image(self, rotation_angle: int):
        """
        Rotate the image by the given rotation angle.

        Args:
            rotation_angle (int): The rotation angle in degrees.

        Returns:
            PIL.Image.Image: The rotated image.
        """
        # Rotate the image
        image = self.image.rotate(rotation_angle)
        return image

    def resize_image(self, size: tuple):
        """
        Resize the image by the given size.

        Args:
            size (tuple): The size to resize the image to. The tuple must
                have two elements: the width and the height.

        Returns:
            PIL.Image.Image: The resized image.
        """
        # Resize the image
        image = self.image.resize(size=size)
        return image

    def enhance_image(self, enhancer_factor: int):
        """
        Enhance the image by applying a contrast filter, converting to grayscale,
        and rotating the image.

        Args:
            enhancer_factor (int): The factor by which to enhance the contrast.

        Returns:
            PIL.Image.Image: The enhanced image.
        """
        # Apply a contrast filter to sharpen the image
        image = self.image.filter(ImageFilter.SHARPEN)

        # Convert the image to grayscale
        image = image.convert("L")

        # Rotate the image counterclockwise by 90 degrees
        image = image.rotate(-90)

        # Enhance the contrast of the image
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(factor=enhancer_factor)

        return image

    def adjust_brightness(self, brightness_factor: float):
        """
        Adjust the brightness of the image.

        Args:
            brightness_factor (float): The factor by which to adjust the brightness.

        Returns:
            PIL.Image.Image: The image with adjusted brightness.
        """
        enhancer = ImageEnhance.Brightness(self.image)
        image = enhancer.enhance(brightness_factor)
        return image

    def adjust_contrast(self, contrast_factor: float):
        """
        Adjust the contrast of the image.

        Args:
            contrast_factor (float): The factor by which to adjust the contrast.

        Returns:
            PIL.Image.Image: The image with adjusted contrast.
        """
        enhancer = ImageEnhance.Contrast(self.image)
        image = enhancer.enhance(contrast_factor)
        return image

    def adjust_sharpness(self, sharpness_factor: float):
        """
        Adjust the sharpness of the image.

        Args:
            sharpness_factor (float): The factor by which to adjust the sharpness.

        Returns:
            PIL.Image.Image: The image with adjusted sharpness.
        """
        enhancer = ImageEnhance.Sharpness(self.image)
        image = enhancer.enhance(sharpness_factor)
        return image

    def flip_image(self, direction: str):
        """
        Flip the image horizontally or vertically.

        Args:
            direction (str): The direction to flip the image ('horizontal' or 'vertical').

        Returns:
            PIL.Image.Image: The flipped image.
        """
        if direction == "horizontal":
            image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == "vertical":
            image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Direction must be 'horizontal' or 'vertical'")
        return image

    def save_image(self, image, suffix="_edited"):
        """
        Save the edited image to the specified save path.

        Args:
            image (PIL.Image.Image): The edited image to save.
            suffix (str): Suffix to append to the saved image file name.
        """
        # Get the cleaned image name by extracting the file name from the image path
        clean_name = os.path.splitext(os.path.basename(self.img_path))[0]

        # Save the edited image with the cleaned name and provided suffix
        image.save(f"{self.img_save_path}/{clean_name}{suffix}.jpg")


if __name__ == "__main__":

    edit_photo = PhotoEdit(
        img_path="/Users/diyorahenils/Documents/personal work/MiniPyExperiments/simple_photoEditor/uploaded_images/person_1.jpg",
        img_save_path="/Users/diyorahenils/Documents/personal work/MiniPyExperiments/simple_photoEditor/saved_images",
    )
    image = edit_photo.rotate_image(rotation_angle=20)
    image = edit_photo.resize_image(size=(200, 200))
    image = edit_photo.enhance_image(enhancer_factor=5)
    image = edit_photo.adjust_brightness(brightness_factor=1.2)
    image = edit_photo.adjust_contrast(contrast_factor=1.5)
    image = edit_photo.adjust_sharpness(sharpness_factor=2.0)
    image = edit_photo.flip_image(direction="horizontal")

    edit_photo.save_image(image=image)
