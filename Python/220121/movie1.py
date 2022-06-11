import json

def get_movie_info(movie):
    """movies.json의 한 요소(딕셔너리)를 이용하여 movies/ 폴더의 세부 정보를 읽어오는 함수

    Args:
        movie(dict)

    Returns:
        (dict)
    """
    movie_id = movie['id']
    f_name = 'data/movies/' + f'{movie_id}' + '.json'
    movie_json = open(f_name, encoding='UTF8')
    return json.load(movie_json)

def max_revenue(movies):
    """수익이 가장 높은 영화의 제목을 출력합니다.

    Args:
        movies(list)

    Returns:
        ret(str)
    """
    ret = ''    # 'title' 값 저장을 위한 변수
    max_rev = 0 # 'revenue' 값 비교를 위한 변수
    for movie in movies:
        # movie의 세부 정보 가져오기
        m_info = get_movie_info(movie)

        if max_rev < m_info['revenue']:
            max_rev = m_info['revenue']
            ret = m_info['title']
    return ret

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))