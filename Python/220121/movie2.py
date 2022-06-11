import json
from movie1 import get_movie_info

def dec_movies(movies):
    """12월에 개봉한 영화들의 제목을 리스트로 출력합니다.

    Args:
        movies(list)

    Returns:
        ret(list)
    """
    ret = []
    for movie in movies:
        # movie의 세부 정보 가져오기
        m_info = get_movie_info(movie)

        # 12월에 개봉한 영화들을 리스트로 저장 
        if m_info['release_date'][5:7] == '12':
            ret.append(m_info['title'])
    return ret

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))