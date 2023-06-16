"""
parking_spot_manager 모듈은 주차장의 정보와 관련된 함수 및 클래스를 제공하는 모듈입니다.
parking_spot 클래스를 이용하여 주차장의 정보를 설정하고 참조하는 것을 수행합니다.
str_list_to_class_list 함수를 통해 parking_spot 클래스 객체 리스트를 반환합니다.
print_spots 함수를 통해 리스트의 원소 개수와 리스트에 저장된 모든 객체의 값을 출력합니다.
filter_by_name 함수, filter_by_city 함수, filter_by_district 함수, filter_by_ptype 함수,
filter_by_location 함수는 parking_spot 클래스 객체 리스트를 필터링한 후 생성된 새로운 리스트를 반환합니다.
"""
class parking_spot:
    """
    parking_spot 클래스는 주차장의 이름, 시도, 시군구, 주차장의 유형, 
    주차장의 경도, 주차장의 위도에 대해 저장하고 있는 클래스입니다.
    변수로는 외부에서 접근 불가능한 __item이 있으며,
    해당 변수의 생성과 설정은 생성자를 통해서만 이루어집니다.
    해당 변수를 접근하기 위한 메소드로는 get이 있습니다.
    """
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """
        생성자 초기 주차장의 이름, 시도, 시군구, 주차장의 유형,
        주차장의 경도, 주차장의 위도 값을 받아 __item 딕셔너리에 저장합니다.
        Args:
            name (str): 초기 주차장의 이름 값입니다.
            city (str): 초기 시도 값입니다.
            district (str): 초기 시군구 값입니다.
            ptype (str): 초기 주차장의 유형 값입니다.
            longitude (float): 초기 주차장의 경도 값입니다.
            latitude (float): 초기 주차장의 위도 값입니다.
        """
        self.__item = { 'name': name,
                       'city': city,
                       'district': district,
                       'ptype': ptype,
                       'longitude': longitude,
                       'latitude': latitude}
        
    def get(self, keyword):
        """
        객체가 저장하고 있는 정보를 반환합니다.
        Args:
            keyword (str): 객체의 __item 딕셔너리의 key 값을 받습니다.
                              객체에 저장된 정보 중에서 어떤 정보를 
                              반환할 것인지를 결정합니다.
        Returns:
            str or float: 저장하고 있는 주차장의 이름, 시도, 
                             시군구, 유형 값은 string으로
                             주차장의 경도, 위도 값은 float로 반환합니다.
        """
        if keyword == 'name':
            return self.__item['name']
        elif keyword == 'city':
            return self.__item['city']
        elif keyword == 'district':
            return self.__item['district']
        elif keyword == 'ptype':
            return self.__item['ptype']
        elif keyword == 'longitude':
            return self.__item['longitude']
        elif keyword == 'latitude':
            return self.__item['latitude']
        else:
            print("Invalid option")

    def __str__(self):
        """
        객체가 저장하고 있는 정보를 출력합니다.
        Returns:
            str: 저장하고 있는 주차장의 이름, 시도, 시군구, 유형, 
                    경도, 위도 값을 하나의 문자열로 묶어서 반환합니다.  
        """
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):
    """
    str_list_to_class_list 함수는 문자열 리스트[str_list]를 매개변수로 
    받아 parking_spot 클래스 객체의 리스트로 변환하는 함수입니다.
    Args:
        str_list (list): 문자열 리스트입니다.
    Returns:
        list: parking_spot 클래스 객체의 리스트를 반환합니다.
    """
    mylist = []
    for item in str_list:
        data = item.split(',')
        name = data[1]
        city = data[2]
        district = data[3]
        ptype = data[4]
        longitude = float(data[5])
        latitude = float(data[6])
        mylist.append(parking_spot(name, city, district, ptype, longitude, latitude))
    return mylist

def print_spots(mylist):
    """
    print_spots 함수는 리스트[mylist]를 받아 출력합니다.
    Args: 
        mylist (list): 입력받는 parking_spot 클래스 객체의 리스트입니다.
    """
    print(f"---print elements({len(mylist)})---")
    for i in range(len(mylist)):
        print(mylist[i].__str__())

def filter_by_name(spots, name):
    """
    filter_by_name 함수는 parking_spot 클래스 객체의 리스트[spots]와 키워드[name]를 매개변수로 받아
    키워드가 리스트에 있을 때만 그 리스트를 새로운 리스트[mylist]에 추가하고
    생성된 새로운 리스트[mylist]를 반환합니다.
    주차장의 이름을 기준으로 데이터를 분석하여 추려냅니다.
    Args:
        spots (list): parking_spot 클래스 객체의 리스트입니다.
        name (str): 리스트를 필터링할 때 사용할 키워드입니다. 
    Returns:
        list: 필터링된 리스트를 반환합니다.
    """
    mylist = [e for e in spots if name in e.get('name')]
    return mylist

def filter_by_city(spots, city):
    """
    filter_by_city 함수는 parking_spot 클래스 객체의 리스트[spots]와 키워드[city]를 매개변수로 받아
    키워드가 리스트에 있을 때만 그 리스트를 새로운 리스트[mylist]에 추가하고
    생성된 새로운 리스트[mylist]를 반환합니다.
    주차장의 시도를 기준으로 데이터를 분석하여 추려냅니다.
    Args:
        spots (list): parking_spot 클래스 객체의 리스트입니다.
        city (str): 리스트를 필터링할 때 사용할 키워드입니다. 
    Returns:
        list: 필터링된 리스트를 반환합니다.
    """
    mylist = [e for e in spots if city in e.get('city')]
    return mylist

def filter_by_district(spots, district):
    """
    filter_by_district 함수는 parking_spot 클래스 객체의 리스트[spots]와 키워드[district]를 매개변수로 받아
    키워드가 리스트에 있을 때만 그 리스트를 새로운 리스트[mylist]에 추가하고
    생성된 새로운 리스트[mylist]를 반환합니다.
    주차장의 시군구를 기준으로 데이터를 분석하여 추려냅니다.
    Args:
        spots (list): parking_spot 클래스 객체의 리스트입니다.
        district (str): 리스트를 필터링할 때 사용할 키워드입니다. 
    Returns:
        list: 필터링된 리스트를 반환합니다.
    """
    mylist = [e for e in spots if district in e.get('district')]
    return mylist

def filter_by_ptype(spots, ptype):
    """
    filter_by_ptype 함수는 parking_spot 클래스 객체의 리스트[spots]와 키워드[ptype]를 매개변수로 받아
    키워드가 리스트에 있을 때만 그 리스트를 새로운 리스트[mylist]에 추가하고
    생성된 새로운 리스트[mylist]를 반환합니다.
    주차장의 유형을 기준으로 데이터를 분석하여 추려냅니다.
    Args:
        spots (list): parking_spot 클래스 객체의 리스트입니다.
        ptype (str): 리스트를 필터링할 때 사용할 키워드입니다. 
    Returns:
        list: 필터링된 리스트를 반환합니다.
    """
    mylist = [e for e in spots if ptype in e.get('ptype')]
    return mylist

def filter_by_location(spots, locations):
    """
    filter_by_name 함수는 parking_spot 클래스 객체의 리스트[spots]와 
    위치 정보에 대한 튜플[locations]를 매개변수로 받아
    리스트의 위도와 경도가 각각 최대 위도와 최소 위도, 최대 경도와 최소 경도 사이에 있는지 분석합니다. 
    조건에 부합한다면 그 리스트를 새로운 리스트[mylist]에 추가하며
    생성된 새로운 리스트[mylist]를 반환합니다.
    Args:
        spots (list): parking_spot 클래스 객체의 리스트입니다.
        location (tuple): 최대 위도, 최소 위도, 최대 경도, 최소 경도를 저장하는 튜플입니다.
    Returns:
        list: 필터링된 리스트를 반환합니다.
    """
    mylist = [e for e in spots if (e.get('latitude')  >= locations[0] \
                               and e.get('latitude')  <= locations[1] \
                               and e.get('longitude') >= locations[2] \
                               and e.get('longitude') <= locations[3])]
    return mylist

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)