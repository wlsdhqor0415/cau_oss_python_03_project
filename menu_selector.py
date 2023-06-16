"""
menu_selector 모듈은 메뉴와 관련된 함수를 제공하는 모듈입니다.
start_process 함수로 메뉴 화면을 불러오고 사용자의 선택에 따라 각 함수를 호출합니다.
"""
import file_manager
import parking_spot_manager

def start_process(path):
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    """
    strat_process 함수는 file_manager 모듈에서의 read_file 함수와 
    parking_spot_manager 모듈에서의 str_list_to_class_list 함수를 
    호출해 parking_spot_manger 모듈의 parking_spot 클래스 객체의 리스트를 생성합니다.
    사용자가 입력하는 select 값에 따라 함수를 불러옵니다.
    """
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            """
            menu의 1번 [print] 기능은 parking_spot_manager 모듈의 print_spots 함수를 이용해
            parking_spot 클래스 객체의 리스트 spots를 출력하는 것입니다.
            """
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            """
            menu의 2번 [fliter] 기능은 필터를 할 기준의 키의 종류 5개 중 하나를 선택하는 메뉴를
            출력하는 것입니다.
            """
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                """
                fliter의 1번 [name] 기능은 keyword를 입력받고
                parking_spot_manager 모듈의 filter_by_name 함수를 호출하는 것입니다.
                """
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            elif select == 2:
                """
                fliter의 2번 [city] 기능은 keyword를 입력받고
                parking_spot_manager 모듈의 filter_by_city 함수를 호출하는 것입니다.
                """
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            elif select == 3:
                """
                fliter의 3번 [district] 기능은 keyword를 입력받고
                parking_spot_manager 모듈의 filter_by_district 함수를 호출하는 것입니다.
                """
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            elif select == 4:
                """
                fliter의 4번 [ptype] 기능은 keyword를 입력받고
                parking_spot_manager 모듈의 filter_by_ptype 함수를 호출하는 것입니다.
                """
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            elif select == 5:
                """
                fliter의 5번 [location] 기능은 최대 경도, 최소 경도, 
                최대 위도, 최소 위도 값을 입력받고 그 값들을 locations 튜플에 저장하고
                parking_spot_manager 모듈의 filter_by_name 함수를 호출하는 것입니다.
                """
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations)
            else:
                print("invalid input")
        elif select == 3:
            """
            menu의 3번 [sort] 기능은 parking_spot_manager 모듈의 
            sort_by_keyword 함수를 호출하는 것입니다.
            """
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
            else: print("invalid input")
        elif select == 4:
            """
            menu의 4번 [exit] 기능은 "Exit"를 출력하고 프로그램을 종료하는 것입니다.
            """
            print("Exit")
            break
        else:
            print("invalid input")