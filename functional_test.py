from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스는 멋진 자업목록 온라인 앱이 나왔다는 소식을 듣고 해당 사이트를 확인하러감
        self.browser.get('http://localhost:8000')

        # 웹페이지 타이틀과 헤더가 'To-Do'라고 표시하고 있음
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 작업을 추가함함

        # 공작깃털 사기 라고 텍스트에 입력

        # 엔터키를 치면 페이지가 갱신 되고 작업목록에
        # "1: 공작깃털 사기" 아이템이 추가

        # 추가 아이템을 입력 할 수 있는 여분의 텍스트 상자가 존재
        # 다시 "공작깃털을 이용해 그물 만들기" 라고 입력

        # 페이지가 갱신, 두 개의 아이템이 목록에서 노출
        # 에디스는 사이트가 입력한 목록을 저장하는지 궁금
        # 사이트는 그녀를 위한 특적 url을 생성
        # 이때 url에 대한 설명도 제공

        # 해당 url에 접속시 그녀가 만든 작업 목록이 그대로 있는것을 확인

        # 만족하고 잔다

if __name__ == '__main__':
    unittest.main(warnings='ignore')