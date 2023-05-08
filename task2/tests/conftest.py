# import pytest
#
# from task2.task2 import Bytes
#
# #B > KB > MB
# b1 = Bytes('1 KB')
# b2 = Bytes('1 MB')
# b3 = Bytes('1 B')
# # def test_bytes_comparison(first_data, second_data, operator, expected)
# operator = '>'
# expected = 'False'
# params = [(b1, b2, operator, expected )]
#
# @pytest.fixture(params=[(Response3, Request3), (Response4, Request4)], ids=['req3', 'req4'])
# async def parametrize_req(request):
#     return request.param