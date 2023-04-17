desktop_validation = ValidationDeclarative()

@property
@desktop_validation
def expected_get_company(self):
    return {
        "company_id": str(self.first_company.mongo_id),
    }


from functools import cached_property


class Smth:

    def __init__(self):
        self.a = [1, 2, 3]

    @cached_property
    def my_gen(self):
        for i in self.a:
            yield i



s = Smth()
print(next(s.my_gen))
print(next(s.my_gen))

class ValidationDeclarative:

    def __init__(self):
        self.validation_data_map = {1: 2, 2: 3}

    def __call__(self, expected_data=None, step_number=1, *args, **kwargs):
        if not expected_data:
            return partial(self.__fill_validation_data_map, step_number=step_number)
        return self.__fill_validation_data_map(expected_data, step_number)

    @cached_property
    def validation_data(self):
        for step_number in sorted(self.validation_data_map.keys()):  # noqa: WPS526
            yield self.validation_data_map[step_number]

    def __fill_validation_data_map(self, expected_data, step_number):
        self.validation_data_map[step_number] = expected_data.__name__
        return expected_data

class LoginToCompanyContext(LoginCompanyContextBaseContext, DesktopGetCompanyBaseContext):
    desktop_validation = ValidationDeclarative()

    @property
    def test_id(self):
        return "Login to company positive flow"

    @property
    @desktop_validation(step_number=GetCompanyStepEnum.get_company_in_company_context.value)
    @desktop_validation(step_number=GetCompanyStepEnum.get_company_after_relogin.value)
    def expected_get_company(self):
        return super().expected_get_company



class MyClass:

    def __call__(self, func):
        def wrapper():
            print('test MyClass print')
            func()
        return wrapper

children = MyClass()

@children
def my_func():
    print('test my_func print')

my_func()