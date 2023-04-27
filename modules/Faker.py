import codecs
import random
from io import BytesIO

import requests
from PIL import Image
from allure import step
from faker import Faker  # https://faker.readthedocs.io/en/stable/

from config_file import ALLURE_RESULTS_DIR

fake = Faker()


class Fake:

    @staticmethod
    @step('get_fake_password')
    def password():
        return fake.password()

    @staticmethod
    @step('email')
    def get_fake_email() -> str:
        return fake.email()

    # todo add Mailinator module
    # @staticmethod
    # @step('get_fake_email')
    # def email():
    #     fake_email = fake.email()
    #     return f'{fake_email[0:fake_email.find("@")]}{fake.random_number(digits=3)}@{cfg.MAILINATOR_DOMAIN}'

    @staticmethod
    @step('get_fake_string')
    def string(charts: int = 10):
        letters_list = fake.random_letters(length=charts)
        string = ''.join([i for i in letters_list])
        return string

    @staticmethod
    @step('get_fake_number')
    def number(digits: int = 10):
        return fake.random_number(digits=digits)

    @staticmethod
    @step('get_fake_random_number')
    def random_number(min_num: int = 0, max_num: int = 9999):
        return fake.pyint(min_num, max_num)

    @staticmethod
    @step('random_float')
    def random_float(a: float, b: float, float_format=2):
        value = "{:." + str(float_format) + "f}"
        return value.format(random.uniform(a, b))

    @staticmethod
    @step('get_fake_sentence')
    def sentence(words: int = 10):
        return fake.sentence(nb_words=words)

    @staticmethod
    @step('get_fake_avatar')
    def file_avatar(size: int = 100):
        file_name = f'avatar_{Fake.number()}.jpg'
        path = f'{ALLURE_RESULTS_DIR}/{file_name}'
        url = f'https://i.pravatar.cc/{size}'
        content = requests.get(url).content
        i = Image.open(BytesIO(content))
        i.save(path)
        return dict({'path': path, 'file_name': file_name, 'content': content, 'md5': Files.create_md5(path)})

    @staticmethod
    @step('file_with_size')
    def file_with_size(size_in_bytes: int):
        file_name = f'{Fake.number()}-size-{size_in_bytes}bytes.txt'
        path = f'{ALLURE_RESULTS_DIR}/{file_name}'
        f = codecs.open(path, 'w+', '1251')
        f.write('0' * size_in_bytes)
        f.close()
        return dict({'path': path, 'file_name': file_name, 'md5': Files.create_md5(path)})

    @staticmethod
    @step("Get first name")
    def first_name():
        return fake.first_name()

    @staticmethod
    @step("Get last name")
    def last_name():
        return fake.last_name()

    @staticmethod
    @step("Get random url")
    def random_url():
        return fake.url()

    @staticmethod
    @step('Get random date of birth')
    def random_date_of_birth():
        return str(fake.date_of_birth())

    @staticmethod
    @step('Create random image')
    def create_image(size: tuple = (2880, 1920), img_format: str = 'png'):
        color_list = ['monochrome', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        color = random.choice(color_list)
        return fake.image(size=size, hue=color, luminosity='bright', image_format=img_format)

    @staticmethod
    @step('Get random image url')
    def random_img_url(width: int = None, height: int = None) -> str:
        return fake.image_url(width, height)

    @staticmethod
    @step
    def random_face_image():
        return requests.get("https://thispersondoesnotexist.com/image", stream=True)

    @staticmethod
    @step("Get random word")
    def random_word():
        return fake.word()

    @staticmethod
    @step("Generate uuid4")
    def random_uuid4():
        return fake.uuid4()

    @staticmethod
    @step("Generate Postal code")
    def random_postalcode():
        return fake.postcode()

    @staticmethod
    @step("Generate street address")
    def random_street_address():
        """
        :return: Ex: '778 Brown Plaza' '60975 Jessica Squares'
        """
        return fake.street_address()

    @staticmethod
    @step("Generate address")
    def random_address():
        """
        :return: Ex: '398 Wallace Ranch Suite 593\nIvanburgh, AZ 80818'
        """
        return fake.address()

    @staticmethod
    @step('Random phone')
    def random_phone():
        return f'{fake.country_calling_code()}{fake.random_number(digits=9)}'

    @staticmethod
    @step('Create Random list from list')
    def random_list_from_list(in_list: [list or tuple], num_elem: int) -> list:
        return random.SystemRandom().sample(in_list, num_elem)
