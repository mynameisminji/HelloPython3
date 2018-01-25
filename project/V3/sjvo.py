from datetime import datetime
class SungJuk:

    #생성자
    def __init__(self, name, kor, eng, mat):
        self.sjno = 0
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg= 0.0
        self.grd = '가'
        self.regdate = str(datetime.now())

    #toString. 결과값을 문자열로 반환해주는 역할을 만들기.
    def to_str(self):
        fmt = '[%s %s %d %d %d %d %.2f %s %s]'
        return fmt % (self.sjno, self.name, self.kor, self.eng, self.mat,
                      self.tot, self.avg, self.grd, self.regdate[0:19])

    #부분정보 출력 - 번호, 이름. 국어, 영어, 수학, 등록일(년월일)
    def to_str_list(self):
        fmt = '[%s %s %d %d %d %s]'
        return fmt % (self.sjno, self.name, self.kor, self.eng,
                      self.mat, self.regdate[:10])