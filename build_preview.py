#!/usr/bin/env python3
"""미리보기용 전체 페이지와 GitHub Pages 용 index.html 을 만든다.

기존 화면(ISMA3SC003M4.do)의 머리글·바닥글을 그대로 가져와 본문만 fragment/ISMA3SC003M6_main.html 로 바꾼다.
본문을 고친 뒤 다시 실행하면 두 파일이 갱신된다.  사용: python3 build_preview.py
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_URL = "https://www.a3sc.co.kr/a3sc/ISMA3SC003M4.do"
CACHE = ROOT / "reference" / "ISMA3SC003M4.html"
PAGE_ID = "ISMA3SC003M6"
PAGE = "/a3sc/ISMA3SC003M6.do"
TITLE = "WDLAB-LLMOps · AI 서비스 품질 진단 | 에이쓰리시큐리티"
DESC = "AI·에이전트 서비스가 어떻게 답을 만들었는지 기록하고, 품질을 점수로 진단하는 WDLAB-LLMOps를 소개합니다. One Cycle Dev. Framework의 02 품질 진단 단계입니다."
HUB = "/a3sc/ISMA3SC003M5.do"  # One Cycle Dev. Framework 화면
PAGE_CSS = "/resources/css/A3/renewal/onecycle_product.css"
# 운영 주소 → 검토용 공개 주소(GitHub Pages). index.html 을 만들 때만 쓴다.
ROUTES = {'/a3sc/ISMA3SC003M6.do': 'https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/', '/a3sc/ISMA3SC003M7.do': 'https://wdlab1958.github.io/SSC-Platform-Webpage/', '/a3sc/ISMA3SC003M8.do': 'https://wdlab1958.github.io/webpage_proof_skills/', '/a3sc/ISMA3SC003M9.do': 'https://wdlab1958.github.io/ARGUS-Webpage/', '/a3sc/ISMA3SC003M10.do': 'https://wdlab1958.github.io/webpage_myelin/', '/a3sc/ISMA3SC003M5.do': 'https://wdlab1958.github.io/a3sc/'}


def source() -> str:
    if not CACHE.exists():
        CACHE.parent.mkdir(exist_ok=True)
        req = urllib.request.Request(SRC_URL, headers={"User-Agent": "Mozilla/5.0"})
        CACHE.write_bytes(urllib.request.urlopen(req, timeout=30).read())
    return CACHE.read_text(encoding="utf-8")


def must_sub(pattern: str, repl: str, text: str, flags: int = 0) -> str:
    out, n = re.subn(pattern, lambda _m: repl, text, count=1, flags=flags)
    if n != 1:
        sys.exit(f"기존 화면 구조가 바뀌어 치환하지 못했습니다: {pattern}")
    return out


def main() -> None:
    html = source().lstrip()
    body = (ROOT / "fragment" / f"{PAGE_ID}_main.html").read_text(encoding="utf-8")

    # 본문 교체
    html = must_sub(r"<main>.*?</main>", "<main>\n" + body + "</main>", html, re.S)
    # 머리: 제목·설명·주소, 페이지 전용 스타일 추가
    html = must_sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", html)
    html = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + DESC, html)
    html = must_sub(r'(?<=<meta property="og:title" content=")[^"]*', TITLE, html)
    html = html.replace("/a3sc/ISMA3SC003M4.do\">\n<meta property=\"al", PAGE + "\">\n<meta property=\"al")
    html = html.replace('rel="canonical" href="https://www.a3sc.co.kr/a3sc/ISMA3SC003M4.do"', f'rel="canonical" href="https://www.a3sc.co.kr{PAGE}"')
    html = html.replace('global_request_uri = "/a3sc/ISMA3SC003M4.do"', f'global_request_uri = "{PAGE}"')
    html = must_sub(r'<link rel="stylesheet" href="/resources/css/A3/renewal/b\.css">',
                    '<link rel="stylesheet" href="/resources/css/A3/renewal/b.css">\n'
                    f'<link rel="stylesheet" href="{PAGE_CSS}">', html)
    # 메뉴: 모바일 전체 메뉴와 바닥글의 「AI 플랫폼」 묶음에 One Cycle 화면 추가 (One Cycle 화면과 같은 메뉴)
    item = f'<li><a href="{HUB}">One Cycle Framework</a></li>'
    html = must_sub(r'(?<=<li><a href="/a3sc/ISMA3SC003M4\.do#lineup">플랫폼 9종</a></li>)(?=<li><a href="/a3sc/ISMA3SC003M4\.do#contact">)', item, html)
    html = must_sub(r'(?<=<li><a href="/a3sc/ISMA3SC003M4\.do#lineup">플랫폼 9종</a></li>)(?=<li class="fam-off">)', item, html)
    # 미리보기에서는 기존 화면 전용 스크립트(게시판·세션·통계)를 뺀다
    html = re.sub(r"<!-- jquery.*?</script>\n</head>", "</head>", html, flags=re.S)

    (ROOT / f"{PAGE_ID}.html").write_text(html, encoding="utf-8")
    print(f"written: {PAGE_ID}.html", len(html), "bytes")

    # GitHub Pages 용 index.html: 하위 경로에서 열리므로 자원은 상대 경로로,
    # One Cycle 화면과 다른 플랫폼 화면은 각자의 공개 주소로, 그 밖의 링크는 실제 사이트로 보낸다.
    pages = html.replace('"/resources/', '"resources/').replace("url(/resources/", "url(resources/")
    for path, live in sorted(ROUTES.items(), key=lambda kv: -len(kv[0])):
        pages = re.sub(r'href="' + re.escape(path) + r'(?=["#])', 'href="' + ("./" if path == PAGE else live), pages)
    pages = pages.replace('href="/a3sc/', 'href="https://www.a3sc.co.kr/a3sc/')
    pages = re.sub(r'<link rel="canonical"[^>]*>\n?', "", pages)
    pages = must_sub(r'(?<=<meta name="robots" content=")[^"]*', "noindex,nofollow", pages)
    (ROOT / "index.html").write_text(pages, encoding="utf-8")
    print("written: index.html", len(pages), "bytes")


if __name__ == "__main__":
    main()
