# WDLAB-LLMOps_Webpage 감사 보고서 (2026-05-31)

## 개요

- 대상 경로: `/home/ubuntu-02/ai_project/WDLAB-LLMOps_Webpage`
- 유형: 빌드 단계 없는 순수 정적 단일 페이지 사이트 (확인). `package.json` 없음 (확인).
- 구성 파일 (확인):
  - `index.html` (624행) — 사이드바 + 본문 12개 `<section>`.
  - `css/style.css` (700행) — 뉴모피즘 디자인 시스템.
  - `js/app.js` (108행) — 스크롤 스파이, 부드러운 스크롤, to-top 버튼, reveal-on-scroll(IntersectionObserver), 카운터 애니메이션.
  - `README.md`, `assets/`(빈 디렉터리, 확인).
- 외부 의존: Google Fonts(Inter / JetBrains Mono / Noto Sans KR) CDN 링크만 사용 (확인). 로컬 이미지·아이콘 폰트 의존 없음 (확인, CSS 내 `url(...)` 참조 0건).
- 런타임 환경: `node v22.22.2` (확인).

## 실행·테스트 결과

- `node --check js/app.js` → 통과(문법 오류 없음) (확인).
- CSS 중괄호 균형: `{` 169개 / `}` 169개 일치 (확인).
- HTML `<section>` 여닫음: 12개 / 12개 일치 (확인).
- 로컬 자산·링크 참조 무결성 (확인):
  - `index.html` 내 비외부 참조는 `css/style.css`, `js/app.js` 2건뿐이며 두 파일 모두 실제 존재.
  - 깨진 로컬 자산 참조 없음.
- 내비게이션 일관성 (확인):
  - 사이드바 `data-target` 10종(hero, projects, observability, development, evaluation, production, compliance, system, architecture, roadmap) 모두 동일 id의 섹션이 존재.
  - 인라인 `onclick`의 `getElementById('pillars')`, `getElementById('architecture')` 대상 모두 존재.
  - `pillars`, `diff` 섹션은 내비 항목이 없으나 CTA/스크롤로 도달하도록 설계됨(결함 아님, 추정).
- 정상 빌드/타입체크/린트 대상 없음(정적 사이트) — 해당 단계 미수행 (확인).
- 서버 미기동(read-only 원칙 준수). 브라우저 렌더링 및 실제 JS 실행은 미관측 (추정 영역으로 분류).

## 발견된 문제점 (확인 vs 추정, 심각도)

1. (확인 · 정보성/낮음) README의 GitHub Pages·리포지토리 URL은 하이픈 표기
   `WDLAB-LLMOps-Webpage`(예: `https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/`)인데,
   실제 디렉터리명은 언더스코어 `WDLAB-LLMOps_Webpage`이다. 문서-실물 명명 불일치.
   영향: 페이지 자체 동작과 무관, 외부 배포 URL 문서 정합성 이슈에 한정.
2. (추정 · 낮음) 외부 폰트 CDN(`fonts.googleapis.com`) 의존. 오프라인/폐쇄망(온프레미스 지향 제품 컨셉)에서는 폰트가 폴백된다. 기능 손상은 아님(시각적 폴백만 발생).
3. (추정 · 정보성) 본문 통계 수치(73 Routes, 39 Frameworks, 18 Metrics 등)는 정적 마케팅 카피로, 백엔드 실측 연동이 아니다. 정적 페이지 특성상 정상.

CONFIRMED 기능 결함(깨진 링크/문법 오류/빌드 실패) 없음.

## 조치한 내용

- 브랜드 스크럽 잔존 검사 (확인): 대소문자 무시로
  `wdlab` / `WDLAB@2023-2026` / `wdlab` / `WDLAB@2023-2026` / `wdlab` / `wdlab` / `wdlab`
  패턴을 `*.html`, `*.js`, `*.css`, `*.md` 전체에서 검색 → **잔존 0건**.
- 보존 대상(A3DE/A3-ADE) 오변경 여부 확인: `a3` 매칭은 CSS 색상값 `#A3B1C6`,
  모델명 `gemma3`뿐으로 브랜드와 무관(확인). 별도 보존 조치 불필요.
- 잔존이 없어 수정·재검증 대상 없음. 파일 변경 0건 (`git status --porcelain` 비어 있음, 확인).
- 디렉터리명/`.git/` 미변경 (원칙 준수).

## 미해결·위험 항목

- (미해결, 낮음) README의 하이픈/언더스코어 명명 불일치(문제점 #1). 저위험이나 디렉터리·리포지토리 실명 확인 없이 임의 수정 시 외부 배포 링크를 잘못 바꿀 수 있어 **권고만** 한다: README URL을 실제 배포 리포지토리명에 맞춰 정정하거나, 반대로 디렉터리/리포 명명 규칙을 통일.
- (위험·권고) 폐쇄망 배포가 목표라면 폰트를 로컬 번들로 자가 호스팅 권고(문제점 #2). 디자인 자산 추가가 필요하므로 자동 수정하지 않음.
- (미관측) 실제 브라우저 렌더링·인터랙션(스크롤 스파이, 카운터 애니메이션 동작)은 서버 미기동으로 확인하지 못함(추정). 정적 검사·문법 검사 기준으로는 결함 없음.

## 종합 판단

정적 사이트로서 구조·문법·로컬 참조·내비게이션 정합성은 모두 양호하며(확인),
브랜드 스크럽 잔존은 0건이다(확인). CONFIRMED 기능 결함은 없다.
실질 이슈는 README의 URL 명명 불일치(저위험)와 외부 폰트 CDN 의존(폐쇄망 시 시각 폴백)뿐이며,
둘 다 페이지 동작을 저해하지 않는다. 코드 수정은 가하지 않았다(잔존·결함 없음).
