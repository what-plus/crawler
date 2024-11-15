# what-plus cralwer

what-plus에서 필요한 편의점 데이터를 수집하기 위해 제작하였습니다.

크롤링은 Github Action을 사용하여 매일 UPT 0시 (한국시간 9"00 A.M.)에 실행되도록 설정하였습니다.

# 크롤러에 사용된 기술 스택

-   Python 3.x, Selenium 2.x

---

[일관된 requirements.txt 포멧 출력 명령어]
:conda와 pip install을 둘다 할 경우에 포멧이 달라 에러 발생하기 때문에 아래와 같이 리스트로 받아와야 문제가 생기지않음
`pip list --format=freeze > requirement_pip_list.txt`
