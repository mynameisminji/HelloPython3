class SungJukService:

    sjdb = [] #성적 데이터를 저장하는 리스트

    #성적처리 - 총점/평균/학점 계산
    def computeSungJuk(self, sj):
        grd_list = '가가가가가가양미우수수'
        sj.tot = sj.kor + sj.eng+ sj.mat
        sj.avg = float(sj.tot/3)
        sj.grd = grd_list[int(sj.avg/10)]

    def addSungJuk(self, sj):
        self.computeSungJuk(sj)
        sj.sjno = len(self.sjdb) +1
        self.sjdb.append(sj) #리스트에 성적데이터 추가
        print(sj.to_str()) #추가된 성적데이터 확인

    #전체 성적데이터 조회
    def getSungJuk(self):
        str_list= []
        for sj in self.sjdb:
            str_list.append(sj.to_str_list())
        return str_list

    # 상세 성적데이터 조회
    def getOneSungJuk(self, no):
        if no> len(self.sjdb) or no<0:
            return '\n잘못된 값 입력'

        result = ''
        for sj in self.sjdb: #sjdb에서 성적데이터를 하나씩 순환
            if sj.sjno == no: #만일 찾는 번호와 학생번호가 같을 때
                result = sj.to_str() #to_str로 불러오기!
                break

        return result

    # 성적데이터 수정
    def modifySungJuk(self, sj):
        self.computeSungJuk(sj) #성적 재계산
        self.sjdb[sj.sjno-1] = sj #성적데이터 수정

        return self.sjdb[sj.sjno-1].to_str  # 수정된 성적데이터 확인

    # 성적데이터 삭제
    def removeSungJuk(self, no):
        result =self.sjdb.pop(no-1)


