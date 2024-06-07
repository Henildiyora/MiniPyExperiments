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

    def enhanceImage(self, enhancerFactor: int):
        """
        Enhance the image by applying a contrast filter, converting to grayscale,
        and rotating the image.

        Args:
            enhancerFactor (int): The factor by which to enhance the contrast.

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
        image = enhancer.enhance(factor=enhancerFactor)

        return image

    def save_image(self, image):
        """
        Save the edited image to the specified save path.

        Args:
            image (PIL.Image.Image): The edited image to save.
        """
        # Get the cleaned image name by extracting the file name from the image path
        clean_name = os.path.splitext(os.path.basename(self.img_path))[0]

        # Save the edited image with the cleaned name and "_edited" suffix
        image.save(f"{self.img_save_path}/{clean_name}_edited.jpg")


if __name__ == "__main__":

    edit_photo = PhotoEdit(
        img_path="/Users/diyorahenils/Documents/personal work/MiniPyExperiments/simple_photoEditor/uploaded_images/person_1.jpg",
        img_save_path="/Users/diyorahenils/Documents/personal work/MiniPyExperiments/simple_photoEditor/saved_images",
    )
    image = edit_photo.rotate_image(rotation_angle=20)
    image = edit_photo.resize_image(size=(200, 200))
    image = edit_photo.enhanceImage(enhancerFactor=5)

    edit_photo.save_image(image=image)
