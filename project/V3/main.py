import sys
from . import sjvo, sjsrv
class SungJukV3Main:

    #성적서비스 객체 생성
    sjsrv = sjsrv.SungJukService()

    #메뉴표시-다량의 문자를 출력할때는 list로 사용하는게 좋다.
    def displayMenu(self):
        str_list = []
        str_list.append('---==성적 처리프로그램==---\n')
        str_list.append('------------------------\n')
        str_list.append('1 : 새로운 성적데이터 추가\n')
        str_list.append('2 : 전체 성적데이터 조회\n')
        str_list.append('3 : 상세 성적데이터 조회\n')
        str_list.append('4 : 성적데이터 수정\n')
        str_list.append('5 : 성적데이터 삭제\n')
        str_list.append('0 : 성적처리 프로그램 종료\n')
        str_list.append('------------------------\n')
        str_list.append('실행할 작업을 선택하세요 >> ')
        print(''.join(str_list))

    #메뉴 선택후 처리
    def newSungJuk(self):
        str_list = []
        str_list.append('\n\n추가할 성적데이터를 입력하세요.')
        str_list.append('\n\n데이터 입력순서는 이름/국어/영어/수학 입니다..')
        str_list.append('\n\n예) 수지 10 10 10')
        print(''.join(str_list))

        #성적데이터를 한줄에서 공백으로 구분해서 입력받음.
        #sj = sjvo.SungJuk(input(), input(), input(), input())
        n, k, e, m = input('').split() # 한번에 변수를 선언함.

        #입력받은 성적데이터로 성적객체 생성
        sj=sjvo.SungJuk(n, int(k), int(e), int(m))

        #성적객체를 추가함
        self.sjsrv.addSungJuk(sj)

        print('\n\n성적 데이터가 성공적으로 추가!!!\n\n')

    def showSungJuk(self):
        str_list = []
        str_list.append('\n\n-=전체 데이터 출력 =- \n')

        #리스트 형태로 결과가 return된 것을 for문으로 다시 한번씩 순환하며 출력
        for sj in self.sjsrv.getSungJuk():
            str_list.append(sj)
        str_list.append('\n\n')
        print(''.join(str_list))

    def showOneSungJuk(self):
        no = input('\n 검색할 성적번호를 입력하세요.\n>>')

        str_list = []
        str_list.append('\n\n-=상세 성적 데이터 출력 =- \n')
        str_list.append(self.sjsrv.getOneSungJuk(int(no)))
        str_list.append('\n\n')

        print(''.join(str_list))

    def updateSungJuk(self):
        no = input('수정할 성적번호를 입력하세요 \n>>')
        str_list = []
        str_list.append('\n\n수정할 성적데이터를 입력하세요.')
        str_list.append('\n\n데이터 입력순서는 이름/국어/영어/수학 입니다..')
        str_list.append('\n\n예) 수지 10 10 10')
        print(''.join(str_list))

        n, k, e, m = input('').split()

        sj=sjvo.SungJuk(n,int(k),int(e),int(m))
        sj.sjno = int(no)

        self.sjsrv.modifySungJuk(sj)
        print('\n\n수정완료!!\n\n')

    def deleteSungJuk(self):
        no = input('\n 삭제할 성적번호를 입력하세요.\n>>')

        self.sjsrv.removeSungJuk(int(no))
        print('삭제가 완료되었습니다.')

    def exitSungJuk(self):
        sys.exit(1)

    #파이썬 자료구조중 dictionary를 이용해서 메뉴 분기시 실행할 함수를 객체형태로 저장
    menus = {'1':newSungJuk, '2':showSungJuk, '3':showOneSungJuk,
             '4':updateSungJuk, '5':deleteSungJuk, '0':exitSungJuk}


    #메뉴 선택후 처리
    def selectMenu(self):
        menu = input('선택하시오.(1/2/3/4/5)')
        self.menus[menu](self)
        # if(menu == 1)
        #     newSungJuk()
        # elif (menu ==2)
        #     showSungJuk()
        # elif (menu ==3)
        #     showOneSungJuk()
        # elif (menu ==4)
        #     updateSungJuk()
        # elif (menu ==5)
        #     deleteSungJuk()
        # elif (menu ==0)
        #     exitSungJuk()





