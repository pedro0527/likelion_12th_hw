from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'text': "2주차 Django 세션 HW",
        'patterns': ['1 : Request', '2 : URL Conf', '3 : View', '4 : Model', '5 : Template'],
        'info':{'1': 'URL을 요청한다.', '2': 'url과 view를 매핑한다.', '3': '요청이 들어오면 그것에 맞는 적절한 로직을 수행한다.',
                '4': '데이터', '5': '보여지는 부분이다(인터페이스)'}
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    context = {
        'text': "추가사항!",
        'info':{'1': '오타 발생 가능성 높음 조심하기.', '2': '폴더, 파일 생성 헷갈리지 않기.', '3': '템플릿 언어 사용하는법 익히기.',
                '4': '템플릿 상속 중요 -> 효율적인 코드가 가능하다.', '5': 'Static 활용하기.'}
    }
    return render(request, 'main/secondpage.html', context)