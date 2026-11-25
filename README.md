# WDLAB-LLMOps 상세 화면 (ISMA3SC003M6)

**Nov. 25, 2026**

AI·에이전트 서비스가 어떻게 답을 만들었는지 기록하고, 품질을 점수와 등급으로 진단하는 플랫폼을 소개하는 화면입니다.
에이쓰리시큐리티 「One Cycle Dev. Framework」 화면의 **02 품질 진단** 단계 카드에서 「자세히 보기」로 연결됩니다.

- Live: https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/
- One Cycle Dev. Framework: https://wdlab1958.github.io/a3sc/ ([저장소](https://github.com/wdlab1958/a3sc))
- 연동 대상 사이트: https://www.a3sc.co.kr/a3sc/ISMA3SC003M4.do (AI 플랫폼)

## 화면 구성

AI·보안 전문가가 아닌 독자도 읽을 수 있게, 비유 한 문장과 용어 풀이·자주 묻는 질문을 두었습니다.

| 구역 | 내용 |
|---|---|
| 히어로 | 5단계 자동 진단 흐름 · 4축 스코어카드 · 평가 기준 19종 · 한국어 가드레일 8종 |
| 개요 | 답은 나왔는데 어떻게 나온 답인가 — 운행기록계와 정기 검사 비유, 필요한 상황 4가지 |
| 동작 방식 | 자동 진단 5단계와 사람의 검토 |
| 주요 기능 | 4축 스코어카드, 실행 기록(trace), finding별 딥링크, SIMULATED 표시, 재진단 비교 |
| 설명·감사 증빙 | 기록이 설명 근거와 감사 증빙이 되는 방식, 보증 범위 |
| 결과물 | 스코어카드·finding 목록·보고서 등 6가지와 한계 주석 |
| One Cycle 연결 | 앞뒤 단계와 주고받는 것, 이전·다음 플랫폼 이동 |
| 용어·FAQ | 용어 12개, 질문 7개 |
| 도입 문의 | 기존 화면과 같은 연락처 부품 |

## One Cycle 화면과 연결되는 구조

- 디자인은 기존 사이트의 `b.css` 를 그대로 쓰고, 그 위에 공통 확장 `onecycle_product.css` 만 더합니다. 선택자는 모두 `.pd-` 로 시작하며 다섯 플랫폼 화면이 같은 파일을 씁니다.
- 머리글·바닥글은 기존 화면(003M4)의 것을 그대로 가져옵니다.
- 화면 안에서 One Cycle 로 돌아가는 길이 세 곳 있습니다: 히어로의 현재 위치 표시, 여섯 단계 띠(`.pd-loop`), 아래쪽 이전·전체·다음 이동(`.pd-nav`).

| 단계 | 플랫폼 | 운영 주소(제안값) | 검토용 공개 주소 |
|---|---|---|---|
| 전체 | One Cycle Dev. Framework | `/a3sc/ISMA3SC003M5.do` | https://wdlab1958.github.io/a3sc/ |
| 02 품질 진단 | WDLAB-LLMOps | `/a3sc/ISMA3SC003M6.do` | https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/ |
| 03 보안 분석·수정 | SSC | `/a3sc/ISMA3SC003M7.do` | https://wdlab1958.github.io/SSC-Platform-Webpage/ |
| 04 형식 검증 | WDLAB-Proof-Skills | `/a3sc/ISMA3SC003M8.do` | https://wdlab1958.github.io/webpage_proof_skills/ |
| 05 운영 감시 | ARGUS | `/a3sc/ISMA3SC003M9.do` | https://wdlab1958.github.io/ARGUS-Webpage/ |
| 06 지식 자산화 | MYELIN | `/a3sc/ISMA3SC003M10.do` | https://wdlab1958.github.io/webpage_myelin/ |

본문의 링크는 운영 주소로 적혀 있고, `build_preview.py` 가 `index.html` 을 만들 때만 `ROUTES` 표에 따라 공개 주소로 바꿉니다.

## 파일

```
.
├── fragment/ISMA3SC003M6_main.html   # 본문 (운영 화면의 <main> 안에 넣는 부분, 페이지 전용 스크립트 포함)
├── resources/css/A3/renewal/
│   ├── onecycle_product.css              # 플랫폼 상세 화면 공통 확장 (.pd-*)  ← 운영 서버에 올릴 파일
│   └── b.css                             # 기존 사이트 사본 (미리보기용, 올리지 않음)
├── resources/font, resources/images      # 기존 사이트 사본 (미리보기용, 올리지 않음)
├── reference/ISMA3SC003M4.html           # 머리글·바닥글을 가져오는 기존 화면 사본
├── build_preview.py                      # 미리보기·공개용 페이지 생성
├── ISMA3SC003M6.html                 # 미리보기 (운영과 같은 절대 경로)
├── legacy/                               # 이전 소개 페이지 (참고용 보존)
└── index.html                            # GitHub Pages 용 (상대 경로, noindex)
```

## 운영 사이트에 붙이는 방법

1. 003M4 화면의 JSP를 복사해 새 화면(`ISMA3SC003M6`)을 만들고, `<main>` 안쪽을 `fragment/ISMA3SC003M6_main.html` 로 바꿉니다.
2. `<head>` 의 `b.css` 다음 줄에 추가합니다. (다섯 화면 공통, 한 번만 올리면 됩니다)
   `<link rel="stylesheet" href="/resources/css/A3/renewal/onecycle_product.css">`
3. `<title>`, description, canonical, og 값을 바꿉니다. (값은 `build_preview.py` 상단)
4. 상단 메뉴는 「AI 플랫폼」에 `class="on"` 을 둡니다. (003M4·003M5와 같음)

화면 번호는 제안값입니다. 다른 번호를 쓰면 본문의 `/a3sc/ISMA3SC003M…` 링크와 `build_preview.py` 의 `PAGE`·`ROUTES` 를 함께 바꿉니다.

## 미리보기

    python3 build_preview.py            # 본문을 고친 뒤 다시 만들기
    python3 -m http.server 8765         # http://127.0.0.1:8765/ISMA3SC003M6.html

## 내용 출처와 확인할 점

프로젝트 폴더 `WDLAB-LLMOps/` 의 `Guide-WDLAB-LLMOps.md`, `WDLAB-LLMOps-Users-Guide_Rev1.0.docx`, `WDLAB-LLMOps-Users-Manual.md`, `README.md` 를 기준으로 썼습니다.
공개 화면이므로 가격·일정·내부 주소·고객 이름은 싣지 않았습니다.

- 프로젝트 문서에서 5단계는 진단 실행 흐름입니다. 이 화면과 One Cycle 화면 모두 「5단계 자동 진단」으로 통일했습니다.
- 프레임워크 어댑터 수는 문서마다 달라(39·47) 싣지 않았습니다.
- 에디션·요금, AI 기본법 조문 번호·과태료·일정은 싣지 않았습니다. Diagnosis 메뉴의 제공 범위는 「도입 구성에 따라 달라질 수 있다」고만 적었습니다.

## 이전 페이지

이 저장소에 있던 기존 랜딩 페이지(v2.0 Open Core 소개, 2026-10-01 판)는 지우지 않고 `legacy/` 로 옮겼습니다.
https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/legacy/ 에서 그대로 열립니다. 필요 없으면 폴더째 지우면 됩니다.

---

© 2026 A3 Security. All rights reserved.
